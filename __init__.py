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

from .star_image_edit_qwen_kontext import (
    NODE_CLASS_MAPPINGS as STAR_IMAGE_EDIT_QWEN_KONTEXT_NODE_CLASS_MAPPINGS,
)
from .star_image_edit_qwen_kontext import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_IMAGE_EDIT_QWEN_KONTEXT_NODE_DISPLAY_NAME_MAPPINGS,
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

from .star_nano_banana import (
    NODE_CLASS_MAPPINGS as STAR_NANO_BANANA_NODE_CLASS_MAPPINGS,
)
from .star_nano_banana import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_NANO_BANANA_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_duplicate_model_finder import (
    NODE_CLASS_MAPPINGS as STAR_DUPLICATE_MODEL_FINDER_NODE_CLASS_MAPPINGS,
)
from .star_duplicate_model_finder import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_DUPLICATE_MODEL_FINDER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_qwen_edit_plus_conditioner import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_EDIT_PLUS_CONDITIONER_NODE_CLASS_MAPPINGS,
)
from .star_qwen_edit_plus_conditioner import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_EDIT_PLUS_CONDITIONER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_qwen_rebalance_prompter import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_REBALANCE_PROMPTER_NODE_CLASS_MAPPINGS,
)
from .star_qwen_rebalance_prompter import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_REBALANCE_PROMPTER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_qwen_regional_prompter import (
    NODE_CLASS_MAPPINGS as STAR_QWEN_REGIONAL_PROMPTER_NODE_CLASS_MAPPINGS,
)
from .star_qwen_regional_prompter import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_QWEN_REGIONAL_PROMPTER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_sampler import (
    NODE_CLASS_MAPPINGS as STAR_SAMPLER_NODE_CLASS_MAPPINGS,
)
from .star_sampler import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_SAMPLER_NODE_DISPLAY_NAME_MAPPINGS,
)

from .star_simple_filters import (
    NODE_CLASS_MAPPINGS as STAR_SIMPLE_FILTERS_NODE_CLASS_MAPPINGS,
)
from .star_simple_filters import (
    NODE_DISPLAY_NAME_MAPPINGS as STAR_SIMPLE_FILTERS_NODE_DISPLAY_NAME_MAPPINGS,
)


NODE_CLASS_MAPPINGS = {
    **STAR_QWEN_IMAGE_RATIO_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_WAN_RATIO_NODE_CLASS_MAPPINGS,
    **STAR_APPLY_OVERLAY_DEPTH_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_EDIT_ENCODER_NODE_CLASS_MAPPINGS,
    **STAR_IMAGE_EDIT_QWEN_KONTEXT_NODE_CLASS_MAPPINGS,
    **STAR_SAVE_FOLDER_STRING_NODE_CLASS_MAPPINGS,
    **STAR_OLLAMA_SYSPROMPTER_JC_NODE_CLASS_MAPPINGS,
    **STAR_NANO_BANANA_NODE_CLASS_MAPPINGS,
    **STAR_DUPLICATE_MODEL_FINDER_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_EDIT_PLUS_CONDITIONER_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_REBALANCE_PROMPTER_NODE_CLASS_MAPPINGS,
    # **STAR_RANDOM_LORA_LOADER_NODE_CLASS_MAPPINGS,
    **STAR_QWEN_REGIONAL_PROMPTER_NODE_CLASS_MAPPINGS,
    **STAR_SAMPLER_NODE_CLASS_MAPPINGS,
    **STAR_SIMPLE_FILTERS_NODE_CLASS_MAPPINGS,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    **STAR_QWEN_IMAGE_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_WAN_RATIO_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_APPLY_OVERLAY_DEPTH_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_IMAGE_EDIT_INPUTS_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_EDIT_ENCODER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_IMAGE_EDIT_QWEN_KONTEXT_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_SAVE_FOLDER_STRING_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_OLLAMA_SYSPROMPTER_JC_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_NANO_BANANA_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_DUPLICATE_MODEL_FINDER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_EDIT_PLUS_CONDITIONER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_REBALANCE_PROMPTER_NODE_DISPLAY_NAME_MAPPINGS,
    # **STAR_RANDOM_LORA_LOADER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_QWEN_REGIONAL_PROMPTER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_SAMPLER_NODE_DISPLAY_NAME_MAPPINGS,
    **STAR_SIMPLE_FILTERS_NODE_DISPLAY_NAME_MAPPINGS,
}

# Expose web assets (including docs) to ComfyUI
# ComfyUI will look for help pages under WEB_DIRECTORY/docs/
WEB_DIRECTORY = "web"

# Serve sprite assets directly so the front-end can fetch them robustly
try:
    import os
    import json
    from server import PromptServer
    from aiohttp import web

    _OTTERS_DIR = os.path.join(os.path.dirname(__file__), 'web', 'img', 'otters')
    _EDITPROMPTS_PATH = os.path.join(os.path.dirname(__file__), 'editprompts.json')

    @PromptServer.instance.routes.get("/starbetanodes/otters/{filename:path}")
    async def starbetanodes_serve_otter_sprite(request):
        filename = request.match_info['filename']
        safe_name = os.path.basename(filename)
        target = os.path.join(_OTTERS_DIR, safe_name)
        if os.path.isfile(target):
            return web.FileResponse(target)
        return web.Response(status=404)

    @PromptServer.instance.routes.get("/starbetanodes/editprompts")
    async def starbetanodes_editprompts(request):
        try:
            if os.path.isfile(_EDITPROMPTS_PATH):
                with open(_EDITPROMPTS_PATH, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return web.json_response(data)
        except Exception as e:
            print(f"Error serving editprompts: {e}")
        return web.json_response({"error": "not found"}, status=404)
except Exception:
    # If server or starlette isn't available yet, silently skip; ComfyUI will still load nodes.
    pass
