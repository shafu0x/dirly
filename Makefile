test:
	python3 -c 'import dirly'
	pip3 install . --upgrade || pip install . --upgrade
	pytest tests/test_img_dirly.py tests/test_video_dirly.py
install:
	pip3 install . --upgrade || pip install . --upgrade
	python3 tests/test_video_dirly.py
