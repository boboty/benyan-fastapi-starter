# 验证

运行 `make check`；启动 `make run` 后调用 `/api/v1/health` 与不存在的路径，检查状态、JSON、X-Request-ID 和日志。数据库需要单独启动 PostgreSQL 后验证 migration。独立验收应复查原始命令结果及错误边界。
