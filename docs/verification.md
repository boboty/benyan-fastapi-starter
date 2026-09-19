# 验证

运行 `make check` 做 ruff、pyright、pytest 代码级门禁；运行 `make smoke` 实际启动 Uvicorn，验证 `/api/v1/health` 的 200 与 `/api/v1/not-found` 的 404、JSON 和 X-Request-ID。数据库需要单独启动 PostgreSQL 后验证 migration。独立验收应复查原始命令结果及错误边界。

测试依赖警告：原先 `httpx` 路径触发 Starlette 的 TestClient 弃用警告；按 Starlette 官方建议改用 `httpx2` 后该警告消失。当前仍有一条来自已安装 Starlette 1.6.0 的 `starlette/testclient.py` 类型别名：它引用已弃用的 `anyio.abc.BlockingPortal`。这是上游代码的导入时警告，13 个测试及 HTTP smoke 均通过；未屏蔽警告或锁旧版本，后续升级 Starlette 时复查。
