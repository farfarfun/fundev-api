"""fundev-api 占位包。

当前仅用于在 PyPI 上保留 `fundev-api` 这个名字，尚无实际功能代码，
具体功能会在之后陆续补充。

版本号的唯一来源是 `pyproject.toml` 的 `[project].version`，这里通过发行
元数据读取，避免源码与打包配置两处硬编码产生漂移。
"""

from importlib.metadata import PackageNotFoundError
from importlib.metadata import version as _metadata_version

__all__ = ["__version__"]

try:
    __version__: str = _metadata_version("fundev-api")
except PackageNotFoundError:  # 直接从源码树导入、包未安装时
    __version__ = "0.0.0+unknown"
