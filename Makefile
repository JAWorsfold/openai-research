VENV = ./venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

build: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run: build
	$(PYTHON) openai.py

clean:
	rm -rf __pycache__
	rm -rf $(VENV)
