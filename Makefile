test:
	python3 -c 'import dirly'
	pip3 install . --upgrade
	pytest tests/ -v