install:
	pip install -r requirements.txt

run:
	python app.py

test:
	python -m doctest app.py -v
	python -m unittest test_app.py

format:
	black app.py test_app.py

lint:
	flake8 app.py test_app.py

audit:
	pip-audit -r requirements.txt

check: lint test audit
