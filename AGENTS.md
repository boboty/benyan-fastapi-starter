# 项目规则

技术栈：Python 3.12+、FastAPI、Pydantic v2、SQLAlchemy 2、Alembic、PostgreSQL、pytest、ruff、pyright。常用命令：`make check`、`make run`。

修改前阅读现有实现；不要不了解架构便大范围重构。`api/` 管 HTTP，`core/` 管通用运行机制，`db/` 管连接；模型、服务、仓储仅在真实业务出现时增加。Python 使用 snake_case / PascalCase / UPPER_SNAKE_CASE。不要创建无业务意义的抽象。

修改后必须运行 `make check`，测试业务正常、边界和失败路径；适用时实际调用 API。不要提交 Secret 或向客户端暴露内部错误。存在 UI 时必须使用 `ui/design-system/` 中官方 BenYan AI Design System。代码写完不等于完成；保留可复查验证证据并安排独立验收。项目例外在这里说明理由。
