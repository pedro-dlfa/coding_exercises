.PHONY: lint test

lint:
	black src/
	black test/

test:
	python -m pytest test