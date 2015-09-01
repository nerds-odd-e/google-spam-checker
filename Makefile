.PHONY: all tests pep8 pylint deps test-deps publish

all: extensive pylint
extensive: tests pep8

tests:
	nosetests tests

deps:
	pip install -r dev_requirements.txt

publish:
	python setup.py sdist upload

