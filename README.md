# BenYan FastAPI Starter

BenYan Demo、原型和初始产品的可运行起点。继承 BenYan Engineering Standard v1.0.0；项目级例外写入 [AGENTS.md](AGENTS.md)。

## 快速开始

```bash
python3.12 -m venv .venv
.venv/bin/pip install -e '.[dev]'
cp .env.example .env
make check
make smoke
.venv/bin/uvicorn app.main:app
curl -i http://127.0.0.1:8000/api/v1/health
```

`make check` 是代码级门禁（ruff、pyright、pytest）；`make smoke` 实际启动 Uvicorn，从 HTTP 边界验证健康接口和 404 错误。

只运行健康接口无需 PostgreSQL；需要数据库时配置 `DATABASE_URL`，执行 `docker compose up -d db` 和 `alembic upgrade head`。镜像包含 Alembic，migration 应作为部署步骤显式执行，不在镜像构建阶段运行。Production 必须显式配置非开发默认值的 `DATABASE_URL`。示例本地凭据仅供开发。

Demo Mode 可以不使用数据库、不建 Repository；仍保留 request_id、异常、日志、测试和检查。Product Mode 根据真实需求引入数据库模型、迁移、Repository、Service 与更完整测试。架构复杂度由实际问题驱动。UI 可选，存在 UI 时遵循 [`ui/README.md`](ui/README.md)。
