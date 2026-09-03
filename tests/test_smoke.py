"""轻量冒烟测试（smoke tests）for fundev-api。

范围说明：
    fundev-api 目前是占位仓库，尚无实际功能代码，因此这里只覆盖
    唯一的公开契约——包能被正常导入，且暴露了版本号。后续补充
    实际功能时，应在此基础上补齐对应公开 API 的正常路径与边界测试。
"""


def test_import_top_level_package():
    """顶层包 fundev_api 可以正常导入。"""
    import fundev_api

    assert fundev_api is not None


def test_version_is_exposed_and_well_formed():
    """__version__ 存在且是 `主.次.修订` 形式的字符串。"""
    import fundev_api

    assert hasattr(fundev_api, "__version__")
    parts = fundev_api.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)
