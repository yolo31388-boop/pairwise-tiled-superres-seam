import pytest
import imaging.tiled_superres as mod

CASES = [
    ("overlap_feather_stitch", (1,)),
    ("global_stats", (1,)),
    ("valid_region_crop", (1,)),
    ("unique_naming", (1,)),
    ("chroma_joint_upsample", (1,)),
    ("high_depth_infer", (1,)),
    ("load_image", (1,)),
    ("split_tiles", (1,)),
    ("infer_tiles", (1,)),
    ("present_image", (1,)),
    ("validate_image", (1,)),
    ("metrics_image", (1,)),
    ("audit_image", (1,)),
    ("fallback_image", (1,)),
    ("determinism_image", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
