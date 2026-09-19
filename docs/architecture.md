# 架构

请求经 RequestContextMiddleware 设置 request_id，进入 `/api/v1` Router；全局异常处理器输出统一错误体。数据库连接仅在需要时由 `get_session` 提供。当前无业务模型，因此没有空 Service/Repository。Demo Mode 可保持此结构；Product Mode 增加实际模型、迁移与业务层。
