# ⭐ Star Beta Nodes for ComfyUI

Welcome to **Star Beta Nodes** – a staging ground for experimental custom nodes for ComfyUI. Most beta nodes have now been released to the main `ComfyUI_StarNodes` repository. This beta repo currently contains only the new ratio helper node described below.

## 🚀 Available Nodes

### Image Ratios
- **⭐ Star Qwen Image Ratio** (`StarQwenImageRatio`)
  Dropdown-driven aspect ratio selector that outputs:
  - An empty SD3 latent sized for the selected ratio (tensor in dict: `{ "samples": torch.zeros([batch_size, 4, H//8, W//8]) }`)
  - Width and height integers
  Supported ratios:
  - `1:1` → 1328 × 1328
  - `16:9` → 1664 × 928
  - `9:16` → 928 × 1664
  - `4:3` → 1472 × 1104
  - `3:4` → 1104 × 1472
  - `3:2` → 1584 × 1056
  - `2:3` → 1056 × 1584
  - `5:7` → 1120 × 1568
  - `7:5` → 1568 × 1120
  Inputs:
  - `batch_size` (INT, default 1): latent batch dimension
  - `custom_width`, `custom_height` (INT): used when selecting "Free Ratio (custom)", both enforced to be divisible by 16

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
Use this node to quickly configure SD3-compatible empty latents and dimensions:
- Select a ratio from the dropdown
- Connect the `latent` output to SD3.5/SD3 workflows expecting a LATENT dict (`{"samples": ...}`)
- Use the `width` and `height` outputs to configure downstream nodes
 - Increase `batch_size` to generate batched latents in one step

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
- PIL/Pillow for image processing
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
