# ⭐ Star Beta Nodes for ComfyUI

Welcome to **Star Beta Nodes** - a collection of experimental custom nodes for ComfyUI designed for beta testing and feedback. These nodes provide enhanced functionality for image processing, video handling, and workflow automation.

## 🚀 Available Nodes

### Video Processing
- **⭐ Star Frame From Video** (`StarFrameFromVideo`)
  Extracts a specific frame from a batch of images (e.g., from video loaders). Choose between first frame, last frame, or a specific frame number for precise control over video frame extraction.

### Image Loading & Management
- **⭐ Star Image Loader 1by1** (`StarImageLoader1by1`)
  Loads images sequentially from a folder, one image per workflow run. Features persistent state between runs, automatic counter reset, subfolder support, sorting options, and progress tracking.

- **⭐ Star Random Image Loader** (`StarRandomImageLoader`)
  Loads a random image from a specified folder. Supports subfolder inclusion and optional seed-based randomization for reproducible results.

### Image Saving
- **⭐ Star Save Panorama JPEG** (`StarSavePanoramaJPEG`)
  Saves images as JPEG with embedded XMP metadata for 360° panoramas. Supports both cylindrical and equirectangular projection types for proper panorama viewing applications.

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

### Star Image Loader 1by1
Perfect for batch processing workflows where you want to process images one at a time:
- Set your image folder path
- Enable reset_counter to restart from the first image
- Use the progress outputs to monitor processing

### Star Frame From Video
Ideal for extracting specific frames from video sequences:
- Connect video loader output to the images input
- Select "Frame Number" and specify the exact frame you need
- Or use "First Frame"/"Last Frame" for quick extraction

### Star Save Panorama JPEG
Essential for 360° content creation:
- Connect your panorama image
- Choose appropriate projection type
- Files will be saved with proper metadata for panorama viewers

## 🔄 Node Categories

All nodes are organized under:
- **⭐StarNodes/Video** - Video processing nodes
- **⭐StarNodes/Image And Latent** - Image loading and saving utilities

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
