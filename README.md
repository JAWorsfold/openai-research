# OpenAI API Hack Day

## Installation

I recommend using [venv](https://docs.python.org/3/library/venv.html) to manage
python environments on your machine. I'm using Makefiles to speed this up.
Review the Makefile for additional commands like `save`, `run`, and `clean`.

### Build

```Bash
make setup
```

### .env

Copy the example .env and add your OpenAI API key to this file

```Bash
cp .example.env .env
```

## Run

```Bash
make run
```
