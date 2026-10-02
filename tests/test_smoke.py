"""轻量冒烟测试（smoke tests）for fundev-api。

范围说明：
    fundev-api 目前是占位仓库，尚无实际功能代码，因此这里只覆盖
    唯一的公开契约——包能被正常导入，且暴露了与 `pyproject.toml`
    一致的版本号。后续补充实际功能时，应在此基础上补齐对应公开
    API 的正常路径与边界测试。

重点是拦住版本号漂移：`pyproject.toml` 的 `[project].version` 是唯一
来源，`fundev_api.__version__` 必须与之完全相等——只断言「是三段数字」
挡不住 0.0.1 与 1.2.3 这类漂移。
"""

import re
from pathlib import Path

import fundev_api

PYPROJECT = Path(__file__).resolve().parent.parent / "pyproject.toml"


def _version_from_pyproject() -> str:
    """从 pyproject.toml 的 [project] 段里取出 version（兼容 3.10，不依赖 tomllib）。"""
    text = PYPROJECT.read_text(encoding="utf-8")
    match = re.search(r'^version\s*=\s*"([^"]+)"', text, flags=re.MULTILINE)
    assert match is not None, "pyproject.toml 里找不到 version"
    return match.group(1)


def test_import_top_level_package():
    """顶层包 fundev_api 可以正常导入。"""
    assert fundev_api is not None


def test_version_is_resolved_from_metadata():
    """包已安装（含 editable）时必须拿到真实版本，而不是回退占位值。"""
    assert fundev_api.__version__ != "0.0.0+unknown"


def test_version_matches_pyproject():
    """__version__ 必须与 pyproject.toml 的 [project].version 完全一致。"""
    assert PYPROJECT.is_file(), f"缺少 {PYPROJECT}"
    assert fundev_api.__version__ == _version_from_pyproject()


def test_version_is_well_formed():
    """__version__ 是 `主.次.修订` 形式的字符串。"""
    parts = fundev_api.__version__.split(".")
    assert len(parts) == 3
    assert all(part.isdigit() for part in parts)


def test_only_exposes_version():
    """占位包的公开接口只有 __version__。"""
    assert fundev_api.__all__ == ["__version__"]
