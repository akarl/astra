clean:
	@echo 'Cleaning .pyc and __pycache__ files'
	$(shell find * -name "*.pyc" -delete)
	$(shell find * -name "__pycache__" -delete)

install: clean
	pip install -r requirements.txt

test: clean flake8
	coverage run --source astra -m py.test tests/
	coverage report -m

flake8: clean
	flake8 .
