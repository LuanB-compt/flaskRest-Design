.DEFAULT_GOAL = help

help:
	@echo ""
	@echo "========== HELP =========="
	@echo ""
	@echo "Setup the System package"
	@echo "make install (install package and dependencies)"
	@echo "make setup (setup the database)"
	@echo ""
	@echo "=========================="
	@echo ""

install:
	@echo ""
	@echo "========== PYTHON REQUIREMENTS =========="
	pip install -r requirements.txt
	@echo ""
	@echo "========== INSTALLING PACKAGE =========="
	sudo apt install figlet
	pip install -e .
	@echo ""

setup:
	@echo ""
	@echo "========== DATABASES SETUP =========="
	chmod +x ./api/scripts/setup_mongo
	./api/scripts/setup_mongo
	@echo ""