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

### Star Qwen Image Ratio
- Select a ratio from the dropdown
- Connect the `latent` output to SD3.5/SD3 workflows expecting a LATENT dict (`{"samples": ...}`)
- Use the `width` and `height` outputs to configure downstream nodes
- Increase `batch_size` to generate batched latents in one step

### Star Apply Overlay (Depth)
- Provide `source_image` and a `filtered_image` to overlay
- Connect either a `mask` or a `depth_image` (greyscale or RGB will be converted)
- Optionally toggle `invert_mask`, enable `show_preview` to save a small mask preview, and adjust `blur_mask_px` for smoother transitions

## 🔄 Node Categories

All nodes are organized under:
- **⭐StarNodes/Image And Latent** – Image/latent utilities

Note: Previous beta nodes (image loaders, video frame tools, panorama saver, etc.) have been migrated to the main repository: `Starnodes2024/ComfyUI_StarNodes`.

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

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Submit bug reports
- Propose new node ideas
- Submit pull requests for improvements

## 📄 License

This project is open source. Please check the repository for specific licensing information.

---

⭐ **Happy beta testing!** Your feedback helps make these nodes better for everyone.
