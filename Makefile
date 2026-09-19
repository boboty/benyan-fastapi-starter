VENV_BIN := .venv/bin

.PHONY: check smoke run
check:
	$(VENV_BIN)/ruff check .
	$(VENV_BIN)/pyright
	$(VENV_BIN)/pytest

run:
	$(VENV_BIN)/uvicorn app.main:app

smoke:
	./scripts/smoke_test.sh
