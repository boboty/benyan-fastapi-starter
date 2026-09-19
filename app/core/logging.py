import json
import logging
from contextvars import ContextVar
from datetime import UTC, datetime

from app.core.config import settings

request_id_context: ContextVar[str] = ContextVar("request_id", default="-")


class JsonFormatter(logging.Formatter):
    def format(self, record: logging.LogRecord) -> str:
        entry: dict[str, object] = {
            "timestamp": datetime.fromtimestamp(record.created, UTC).isoformat(),
            "level": record.levelname,
            "service": settings.service_name,
            "event": record.getMessage(),
            "request_id": request_id_context.get(),
        }
        for key in ("method", "path", "status_code", "duration_ms"):
            if hasattr(record, key):
                entry[key] = getattr(record, key)
        if record.exc_info:
            entry["exception"] = self.formatException(record.exc_info)
        return json.dumps(entry, ensure_ascii=False)


def configure_logging(json_output: bool) -> None:
    handler = logging.StreamHandler()
    handler.setFormatter(JsonFormatter() if json_output else logging.Formatter(
        "%(levelname)s %(name)s %(message)s"
    ))
    logger = logging.getLogger("app")
    logger.handlers = [handler]
    logger.setLevel(logging.INFO)
    logger.propagate = False
