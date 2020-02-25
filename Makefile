test:
	python3 -c 'import dirly'
	pip3 install . --upgrade || pip install . --upgrade
	pytest tests/test_img_dirly.py
	#pytest tests/test_img_dirly.py