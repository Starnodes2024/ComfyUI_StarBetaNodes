import os
from typing import List, Tuple
import numpy as np
from PIL import Image
import folder_paths


def tensor_to_pil(img_tensor) -> Image.Image:
    """Convert a ComfyUI IMAGE tensor [B,H,W,C] (float 0-1) to a PIL RGBA image (first batch).
    Adds opaque alpha if not present.
    """
    # IMAGE is expected as torch tensor, but we avoid importing torch to keep it light.
    # Use available tensor methods defensively.
    b, h, w, c = int(img_tensor.shape[0]), int(img_tensor.shape[1]), int(img_tensor.shape[2]), int(img_tensor.shape[3])
    # Take first in batch
    t = img_tensor[0]
    # Ensure CPU numpy
    if hasattr(t, 'detach'):
        t = t.detach()
    if hasattr(t, 'cpu'):
        t = t.cpu()
    np_img = np.clip(np.asarray(t), 0.0, 1.0)
    np_img = (np_img * 255.0).astype(np.uint8)  # H W C
    if c == 4:
        pil = Image.fromarray(np_img, mode='RGBA')
    else:
        pil = Image.fromarray(np_img, mode='RGB').convert('RGBA')
    return pil


def parse_extra_sizes(extra: str) -> List[int]:
    out: List[int] = []
    if not extra:
        return out
    for part in extra.replace(';', ',').split(','):
        part = part.strip()
        if not part:
            continue
        try:
            val = int(part)
            if 8 <= val <= 1024:
                out.append(val)
        except ValueError:
            pass
    # dedupe and sort
    return sorted(list({*out}))


class StarIconExporter:
    """
    Star Icon Exporter
    - Takes an IMAGE input and a save name
    - Exports resized PNGs at standard icon sizes
    - Packs an .ico file containing the sizes
    - Optional extra sizes via comma-separated input
    - Optional 256-color quantization for PNGs and ICO
    """

    CATEGORY = "⭐StarNodes/Image And Latent"
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("ico_path",)
    FUNCTION = "export_icons"
    OUTPUT_NODE = True

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "images": ("IMAGE", {"tooltip": "Image input (first image in batch will be used)."}),
                "save_name": ("STRING", {"default": "icon", "tooltip": "Base filename without extension."}),
            },
            "optional": {
                "quantize_to_256": ("BOOLEAN", {"default": True, "tooltip": "Quantize to 256 colors for smaller files."}),
                "extra_sizes": ("STRING", {"default": "", "tooltip": "Comma-separated extra sizes, e.g. 64,512"}),
                "subfolder": ("STRING", {"default": "", "tooltip": "Optional output subfolder under ComfyUI output."}),
            },
        }

    @staticmethod
    def _build_sizes(extra_sizes: str) -> List[int]:
        base = [16, 32, 48, 128, 256]
        extra = parse_extra_sizes(extra_sizes)
        sizes = sorted(list({*base, *extra}))
        return sizes

    @staticmethod
    def _ensure_subfolder(base_dir: str, subfolder: str) -> str:
        if subfolder:
            out_dir = os.path.join(base_dir, subfolder)
        else:
            out_dir = base_dir
        os.makedirs(out_dir, exist_ok=True)
        return out_dir

    @staticmethod
    def _save_png(img_rgba: Image.Image, path: str, size: int, quantize: bool):
        im = img_rgba.resize((size, size), resample=Image.LANCZOS)
        if quantize:
            # Convert to paletted 256 colors while preserving alpha via RGBA -> P conversion
            im = im.convert("P", palette=Image.ADAPTIVE, colors=256)
        im.save(path, format="PNG")

    @staticmethod
    def _save_ico(img_rgba: Image.Image, path: str, sizes: List[int], quantize: bool):
        base = img_rgba
        if quantize:
            base = base.convert("P", palette=Image.ADAPTIVE, colors=256).convert("RGBA")
        # Pillow will generate downscaled sizes internally when passing sizes
        base.save(path, format="ICO", sizes=[(s, s) for s in sizes])

    def export_icons(self, images, save_name: str = "icon", quantize_to_256: bool = True, extra_sizes: str = "", subfolder: str = ""):
        output_dir = folder_paths.get_output_directory()
        out_dir = self._ensure_subfolder(output_dir, subfolder)

        # Convert tensor to base RGBA image
        pil_rgba = tensor_to_pil(images)

        # Build sizes list
        sizes = self._build_sizes(extra_sizes)

        # Save PNGs per size
        saved_pngs: List[Tuple[str, int]] = []
        for s in sizes:
            png_path = os.path.join(out_dir, f"{save_name}_{s}.png")
            self._save_png(pil_rgba, png_path, s, quantize_to_256)
            saved_pngs.append((png_path, s))

        # Save ICO with all sizes
        ico_path = os.path.join(out_dir, f"{save_name}.ico")
        self._save_ico(pil_rgba, ico_path, sizes, quantize_to_256)

        # Build UI results for PNG previews
        ui_results = []
        for png_path, _ in saved_pngs:
            ui_results.append({
                "filename": os.path.basename(png_path),
                "subfolder": subfolder if subfolder else "",
                "type": "output"
            })

        return {"ui": {"images": ui_results}, "result": (ico_path,)}


NODE_CLASS_MAPPINGS = {
    "StarIconExporter": StarIconExporter,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "StarIconExporter": "⭐ Star Icon Exporter",
}
