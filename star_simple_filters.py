import torch
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

class StarSimpleFilters:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE", {"tooltip": "The input image to apply filters to."}),
                "sharpen": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1, "tooltip": "Increase image sharpness. 0 is no effect."}),
                "blur": ("FLOAT", {"default": 0.0, "min": 0.0, "max": 100.0, "step": 0.1, "tooltip": "Apply Gaussian Blur. 0 is no effect."}),
                "saturation": ("FLOAT", {"default": 0.0, "min": -100.0, "max": 100.0, "step": 1.0, "tooltip": "Adjust color intensity. 0: Neutral, -100: B&W, 100: Double saturation."}),
                "contrast": ("FLOAT", {"default": 0.0, "min": -100.0, "max": 100.0, "step": 1.0, "tooltip": "Adjust contrast. 0 is neutral."}),
                "brightness": ("FLOAT", {"default": 0.0, "min": -100.0, "max": 100.0, "step": 1.0, "tooltip": "Adjust brightness. 0 is neutral."}),
                "temperature": ("FLOAT", {"default": 0.0, "min": -100.0, "max": 100.0, "step": 1.0, "tooltip": "Adjust color temperature. -100: Cooler (Blue), 100: Warmer (Red)."}),
                "filter_strength": ("FLOAT", {"default": 100.0, "min": 0.0, "max": 100.0, "step": 1.0, "tooltip": "Global opacity of the effect. 100 is full effect, 0 is original image."}),
                "color_match_method": (['None', 'mkl', 'hm', 'reinhard', 'mvgd', 'hm-mvgd-hm', 'hm-mkl-hm'], {"default": 'None', "tooltip": "Method for color matching."}),
            },
            "optional": {
                "color_match_image": ("IMAGE", {"tooltip": "Reference image for color matching."}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("image",)
    FUNCTION = "apply_filters"
    CATEGORY = "⭐StarNodes/Image And Latent"

    def apply_filters(self, image, sharpen, blur, saturation, contrast, brightness, temperature, filter_strength, color_match_method, color_match_image=None):
        result_images = []
        
        # Check for ColorMatcher availability if needed
        if color_match_method != 'No':
            try:
                from color_matcher import ColorMatcher
            except ImportError:
                raise Exception("Can't import color-matcher, did you install requirements.txt? Manual install: pip install color-matcher")

        # Iterate over batch
        for i in range(image.shape[0]):
            img_tensor = image[i]
            
            # 0. Color Match
            if color_match_method != 'None' and color_match_image is not None:
                try:
                    cm = ColorMatcher()
                    # Handle batch size mismatch for reference image
                    ref_idx = i % color_match_image.shape[0]
                    ref_img = color_match_image[ref_idx]
                    
                    target_np = img_tensor.cpu().numpy()
                    ref_np = ref_img.cpu().numpy()
                    
                    matched_np = cm.transfer(src=target_np, ref=ref_np, method=color_match_method)
                    
                    # Ensure consistency
                    matched_np = np.clip(matched_np, 0.0, 1.0)
                    img_tensor = torch.from_numpy(matched_np)
                except Exception as e:
                    print(f"Color Match error on image {i}: {e}")
                    # Continue with original image if fails
            
            # Convert tensor [H, W, C] to PIL
            # Ensure range 0-255 and uint8
            img_np = (img_tensor.cpu().numpy() * 255.0).clip(0, 255).astype(np.uint8)
            pil_img = Image.fromarray(img_np)
            
            # Start processing
            processed_img = pil_img
            
            # 1. Blur
            if blur > 0:
                processed_img = processed_img.filter(ImageFilter.GaussianBlur(radius=blur))
            
            # 2. Sharpen
            # Pillow Sharpness: 1.0 is original. We assume 'sharpen' parameter adds sharpness.
            # Mapping: 0.0 input -> 1.0 factor (no change).
            if sharpen > 0:
                factor = 1.0 + sharpen
                enhancer = ImageEnhance.Sharpness(processed_img)
                processed_img = enhancer.enhance(factor)
            
            # 3. Saturation
            # Input: -100 to 100. 0 is neutral.
            # Mapping: 0 -> 1.0. -100 -> 0.0 (BW). 100 -> 2.0 (Double).
            if saturation != 0:
                factor = 1.0 + (saturation / 100.0)
                # Clamp to 0 minimum just in case
                factor = max(0.0, factor)
                enhancer = ImageEnhance.Color(processed_img)
                processed_img = enhancer.enhance(factor)
            
            # 4. Contrast
            # Input: -100 to 100. 0 is neutral.
            if contrast != 0:
                factor = 1.0 + (contrast / 100.0)
                factor = max(0.0, factor)
                enhancer = ImageEnhance.Contrast(processed_img)
                processed_img = enhancer.enhance(factor)
                
            # 5. Brightness
            # Input: -100 to 100. 0 is neutral.
            if brightness != 0:
                factor = 1.0 + (brightness / 100.0)
                factor = max(0.0, factor)
                enhancer = ImageEnhance.Brightness(processed_img)
                processed_img = enhancer.enhance(factor)
            
            # 6. Temperature
            # Input: -100 to 100. 0 is neutral.
            if temperature != 0:
                processed_img = processed_img.convert("RGB")
                r, g, b = processed_img.split()
                
                # Mapping: max shift 0.5 for 100 input.
                shift = (temperature / 100.0) * 0.5
                
                r_factor = 1.0 + shift
                b_factor = 1.0 - shift
                
                # Apply point transform to channels
                r = r.point(lambda x: int(min(255, max(0, x * r_factor))))
                b = b.point(lambda x: int(min(255, max(0, x * b_factor))))
                
                processed_img = Image.merge("RGB", (r, g, b))
                
            # Filter Strength Blend
            if filter_strength < 100.0:
                blend_factor = max(0.0, min(1.0, filter_strength / 100.0))
                
                # True original for blending
                true_original_tensor = image[i]
                true_original_np = (true_original_tensor.cpu().numpy() * 255.0).clip(0, 255).astype(np.uint8)
                true_original_pil = Image.fromarray(true_original_np)
                
                processed_img = Image.blend(true_original_pil, processed_img, blend_factor)
            
            # Convert back to tensor
            res_np = np.array(processed_img).astype(np.float32) / 255.0
            res_tensor = torch.from_numpy(res_np).unsqueeze(0)
            result_images.append(res_tensor)
            
        if len(result_images) > 0:
            final_tensor = torch.cat(result_images, dim=0)
        else:
            final_tensor = image
            
        return (final_tensor,)

NODE_CLASS_MAPPINGS = {
    "StarSimpleFilters": StarSimpleFilters
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StarSimpleFilters": "⭐ Star Simple Filters"
}
