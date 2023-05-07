VENV = ./venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

build: requirements.txt
	$(info `source $(VENV)` to activate the venv)
	python3 -m venv $(VENV)
	$(PYTHON) -m pip install --upgrade pip
	$(PIP) install -r requirements.txt

save: requirements.txt
	$(PIP) freeze > requirements.txt

run:
	$(PYTHON) ./src/openai.py

clean:
	$(info `deactivate` the venv)
	find . | grep -E "(__pycache__)" | xargs rm -rf
	rm -rf $(VENV)
