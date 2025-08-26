import os
from .star_qwen_image_ratio import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_IMAGE_RATIO_NODE_CLASS_MAPPINGS,
)
from .star_qwen_image_ratio import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_IMAGE_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
)
from .star_qwen_wan_ratio import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_WAN_RATIO_NODE_CLASS_MAPPINGS,
)
from .star_qwen_wan_ratio import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_WAN_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
)
from .star_apply_overlay_depth import (
    NODE_CLASS_MAPPINGS as STAR_APPLY_OVERLAY_DEPTH_NODE_CLASS_MAPPINGS,
)
from .star_apply_overlay_depth import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_APPLY_OVERLAY_DEPTH_NODE_DISPLAY_NAME_MAPPINGS,
)
from .star_qwen_image_edit_inputs import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_CLASS_MAPPINGS,
)
from .star_qwen_image_edit_inputs import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_DISPLAY_NAME_MAPPINGS,
)
from .star_qwen_edit_encoder import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_EDIT_ENCODER_NODE_CLASS_MAPPINGS,
)
from .star_qwen_edit_encoder import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_EDIT_ENCODER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_save_folder_string import (
    NODE_CLASS_MAPPINGS as STAR_SAVE_FOLDER_STRING_NODE_CLASS_MAPPINGS,
)
from .star_save_folder_string import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_SAVE_FOLDER_STRING_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_ollama_sysprompter_jc import (
    NODE_CLASS_MAPPINGS as STAR_OLLAMA_SYSPROMPTER_JC_NODE_CLASS_MAPPINGS,
)
from .star_ollama_sysprompter_jc import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_OLLAMA_SYSPROMPTER_JC_NODE_DISPLAY_NAME_MAPPINGS,
)

NODE_CLASS_MAPPINGS = {
    **STAR_QWEN_IMAGE_RATIO_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_WAN_RATIO_NODE_CLASS_MAPPINGS,
    **STAR_APPLY_OVERLAY_DEPTH_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_EDIT_ENCODER_NODE_CLASS_MAPPINGS,
    **STAR_SAVE_FOLDER_STRING_NODE_CLASS_MAPPINGS,
    **STAR_OLLAMA_SYSPROMPTER_JC_NODE_CLASS_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **STAR_QWEN_IMAGE_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_WAN_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_APPLY_OVERLAY_DEPTH_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_EDIT_ENCODER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_SAVE_FOLDER_STRING_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_OLLAMA_SYSPROMPTER_JC_NODE_DISPLAY_NAME_MAPPINGS,
}

# Expose web assets (including docs) to ComfyUI
# ComfyUI will look for help pages under WEB_DIRECTORY/docs/
WEB_DIRECTORY = "web"

# Serve sprite assets directly so the front-end can fetch them robustly
try:
    import os
    from server import PromptServer
    from starlette.responses import FileResponse, Response

    _OTTERS_DIR = os.path.join(os.path.dirname(__file__), 'web', 'img', 'otters')

    @PromptServer.instance.routes.get("/starbetanodes/otters/{filename:path}")
    async def starbetanodes_serve_otter_sprite(filename: str):
        safe_name = os.path.basename(filename)
        target = os.path.join(_OTTERS_DIR, safe_name)
        if os.path.isfile(target):
            # Rely on Starlette to set content-type by extension
            return FileResponse(target)
        return Response(status_code=404)
except Exception:
    # If server or starlette isn't available yet, silently skip; ComfyUI will still load nodes.
    pass
