PYTEST = $(shell which pytest)

all: test_all

test_all:
	@for d in lec* ; do \
		if [ -d $$d ]; then \
			echo "Running tests in $$d..."; \
			cd $$d && ../../venv/bin/pytest || exit 1; \
			cd ..; \
		fi \
	done

clean:
	find . -name "__pycache__" -type d | xargs rm -rf
