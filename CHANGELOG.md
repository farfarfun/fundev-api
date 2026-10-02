# Changelog

本项目遵循[语义化版本](https://semver.org/lang/zh-CN/)，版本记录按倒序排列。

## [未发布]

### 新增

- `[dependency-groups] dev` 声明 `pytest` / `ruff`，并补上 `[tool.ruff]`、`[tool.ruff.lint]`、
  `[tool.pytest.ini_options]` 配置。此前仓库没有开发依赖组，`uv run pytest` 会落到环境里
  的全局 pytest、看不到 `src/`，测试直接 `ModuleNotFoundError: No module named 'fundev_api'`。
- `[project.urls].Homepage` 指向 `https://pypi.org/project/fundev-api/`（包已发布且属本组织）。
- 测试补上版本漂移拦截：断言 `fundev_api.__version__` 与 `pyproject.toml` 的
  `[project].version` 完全相等，并断言未回退到 `0.0.0+unknown` 占位值。

### 变更

- `__version__` 改为通过 `importlib.metadata` 读取发行元数据，让 `[project].version`
  成为版本号唯一来源，不再在源码里硬编码。

### 修复

- 修正下面 0.0.1 条目的年份：该版本实际在 2026-09-20 发布，原先写的是 2025。

## [0.0.1] - 2026-09-20

### 新增

- 占位包骨架，用于在 PyPI 上保留 `fundev-api` 包名。

### 修复

- 无

### 变更

- 无

### 废弃

- 无
