all:
	$(error please pick a target)

env:
	#create venv directory if not exist
	test -d venv || virtualenv venv
	./venv/bin/python -m pip install -r requirements_dev.txt

test:
	#check pokerbot/tests files for syntax, then runs tests
	find . -name '*.pyc' -exec rm -f {} \;
	./venv/bin/flake8 --ignore=F401 pokerbot tests 
	./venv/bin/python -m pytest \
	--doctest-modules \
	--disable-warnings \
	--verbose \
	pokerbot tests