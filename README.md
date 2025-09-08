# ⭐ Star Beta Nodes for ComfyUI

Welcome to **Star Beta Nodes** – a staging ground for experimental custom nodes for ComfyUI. Most beta nodes have now been released to the main `ComfyUI_StarNodes` repository. This beta repo currently contains the nodes listed below.

## 🚀 Available Nodes

### ⭐StarNodes/Image And Latent

- **⭐ Star Qwen Image Ratio** (`StarQwenImageRatio`)
  - Dropdown-driven aspect ratio selector that outputs:
    - An empty SD3 latent sized for the selected ratio (dict with `samples` tensor)
    - Width and height integers
  - Supported ratios:
    - `1:1` → 1328 × 1328
    - `16:9` → 1664 × 928
    - `9:16` → 928 × 1664
    - `4:3` → 1472 × 1104
    - `3:4` → 1104 × 1472
    - `3:2` → 1584 × 1056
    - `2:3` → 1056 × 1584
    - `5:7` → 1120 × 1568
    - `7:5` → 1568 × 1120
  - Inputs:
    - `batch_size` (INT, default 1): latent batch dimension
    - `custom_width`, `custom_height` (INT): used when selecting "Free Ratio (custom)", both enforced to be divisible by 16

- **⭐ Star Apply Overlay (Depth)** (`StarApplyOverlayDepth`)
  - Blends a filtered image over a source image using either a provided mask or a depth/greyscale image converted to a mask
  - Options include strength, invert mask, preview, and pixel-based Gaussian blur of the mask
  - Outputs: composited `IMAGE`
  - Inputs (required): `source_image`, `filtered_image`, `strength`
  - Inputs (optional): `depth_image` or `mask` (one required), `invert_mask`, `show_preview`, `blur_mask_px`

- **⭐ Star Qwen Image Edit Inputs** (`StarQwenImageEditInputs`)
  - Prepares multiple input images for Qwen editing models by intelligently stitching them into a single canvas
  - Supports up to 4 input images arranged in various grid layouts
  - Automatically handles aspect ratio optimization and resizing
  - Outputs: stitched `IMAGE`, `LATENT`, and dimensions
  - Inputs: `image1` (required), `qwen_resolution`, `batch_size`, `custom_width/height`, `image2-4` (optional)

- **⭐ Star Qwen / WAN Ratio** (`StarQwenWanRatio`)
  - Unified ratio selector supporting both Qwen and WAN video models
  - Automatically calculates optimal dimensions for target pixel counts
  - Can match image aspect ratio automatically
  - Supports HD (1280x720) and Full HD (1920x1080) for WAN models
  - Outputs: `LATENT`, `width`, `height`
  - Inputs: `model` (Qwen/Wan HD/Wan Full HD), ratio selections, `use_nearest_image_ratio`, `image` (optional)

### ⭐StarNodes/Image Generation

- **⭐ Star Nano Banana (Gemini Image Gen)** (`StarNanoBanana`)
  - Advanced image generation using Google's Gemini 2.5 Flash model
  - Supports both generation and editing with up to 5 input images
  - 30+ ready-made prompt templates optimized for image editing tasks
  - Flexible aspect ratios (1:1, 16:9, 9:16, 4:3, 3:4) and megapixel sizes (1-15 MP)
  - Outputs: generated/edited `IMAGE` and final `prompt` string
  - Inputs: `prompt`, `model`, `ratio`, `megapixels`, `prompt_template`, `image1-5` (optional)

### ⭐StarNodes/Prompts

- **⭐ Star Image Edit for Qwen/Kontext** (`StarImageEditQwenKontext`)
  - Dynamic prompt builder for Qwen and Kontext image editing models
  - Loads customizable templates from `editprompts.json`
  - Supports parameter interpolation with fillable fields
  - Outputs: interpolated `prompt` and `params_hint`
  - Inputs: `model`, `task`, plus various parameter fields (subject, color, style, etc.)

- **⭐ Star Ollama Sysprompter (JC)** (`StarOllamaSysprompterJC`)
  - Builds structured prompts for Ollama-style image generation
  - Supports multiple art styles loaded from `styles.json`
  - Configurable token limits and custom style options
  - Outputs: `system_prompt`, `detail_prompt`, `style_name`
  - Inputs: `max_tokens`, `style`, `own_style`, `additional_system_prompt`, `fit_composition_to_style`

### ⭐StarNodes/Conditioning

- **⭐ Star Qwen Edit Encoder** (`StarQwenEditEncoder`)
  - Advanced CLIP text encoder optimized for Qwen image editing models
  - Supports reference latents and multi-image conditioning
  - Performance optimizations with caching and timing controls
  - Outputs: `CONDITIONING` tensor
  - Inputs: `clip`, `prompt`, `vae`, `image`, `reference_latent`, plus various quality/speed controls

### ⭐StarNodes/IO

- **⭐ Star Save Folder String** (`StarSaveFolderString`)
  - Flexible path builder for organized file saving
  - Supports preset folders, date-based organization, and custom naming
  - Cross-platform path compatibility
  - Outputs: formatted `path` string
  - Inputs: `preset_folder`, `date_folder`, `custom_folder/subfolder`, `filename`, plus various formatting options

## 📦 Installation

### Method 1: Git Clone (Recommended)

1. Navigate to your ComfyUI custom nodes directory:
   ```bash
   cd ComfyUI/custom_nodes
   ```

2. Clone this repository:
   ```bash
   git clone https://github.com/Starnodes2024/ComfyUI_StarBetaNodes
   ```

3. Restart ComfyUI to load the new nodes.

### Method 2: Manual Installation

1. Download the ZIP file from the repository
2. Extract to `ComfyUI/custom_nodes/ComfyUI_StarBetaNodes/`
3. Restart ComfyUI

## 🎯 Usage Examples

### Star Qwen Image Edit Inputs
- Connect up to 4 input images to intelligently stitch them for Qwen editing models
- Select resolution from Qwen-supported options or use "Use Best Ratio from Image 1"
- The node automatically handles aspect ratio optimization and creates appropriate latents

### Star Nano Banana (Gemini)
- Choose from 30+ editing templates like "Style Transfer", "Color Enhancement", "Background Change"
- Select aspect ratio and megapixel size, then connect input images for editing
- Use "Use Own Prompt" for custom prompts or pick from the editing-focused templates

### Star Qwen Edit Encoder
- Connect your CLIP model and enter prompts optimized for Qwen editing
- Optionally provide reference images and latents for enhanced conditioning
- Enable caching and timing controls for performance optimization

### Star Save Folder String
- Set up organized folder structures with date-based organization
- Choose from preset folder names or create custom paths
- Enable timestamps and custom separators for unique filenames

## 🔄 Node Categories

All nodes are organized under these StarNodes categories:
- **⭐StarNodes/Image And Latent** – Image processing, latent generation, and dimension utilities (4 nodes)
- **⭐StarNodes/Image Generation** – AI-powered image generation and editing (1 node)
- **⭐StarNodes/Prompts** – Dynamic prompt building and template management (2 nodes)
- **⭐StarNodes/Conditioning** – Advanced text encoding and conditioning (1 node)
- **⭐StarNodes/IO** – File and path management utilities (1 node)

## 🐛 Beta Testing & Feedback

As this is a beta testing repository, your feedback is crucial! Please:
- Report any bugs or issues
- Suggest new features or improvements
- Share your use cases and workflow examples

## 📋 Requirements

- ComfyUI (latest version recommended)
- Python 3.8+
- PyTorch (bundled with ComfyUI env)
- PIL/Pillow (for preview saving in overlay node)
- Standard ComfyUI dependencies
- **External Dependencies**: See `requirements.txt` for additional packages needed:
  - `google-generativeai>=0.8.3` (for Star Nano Banana node)

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Propose new node ideas
- Submit pull requests for improvements

## 📄 License

This project is open source. Please check the repository for specific licensing information.

---

⭐ **Happy beta testing!** Your feedback helps make these nodes better for everyone.
