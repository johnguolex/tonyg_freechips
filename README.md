# tonyg_freechips
A Poker AI. 

Named after tonyg, a legendary online player who doubled both of our stacks one night by shoving pre-flop with air, not once, but twice. 

## Setting up the Virtual Environment 
Note that before running any tests, or any applications of any sort, we need to set up
a virtualenv. This can be done with 
``` 
    make env
```
or alternatively
``` 
	test -d venv || virtualenv venv
	./venv/bin/python -m pip install -r requirements_dev.txt
```
Note: if you have not already, you will need to have pip and virtualenv installed!

## Note on writing Tests
All files that want to be included in automated testing must be of the format `test_*.py`, and all methods in those files must be named in the format `test_*`, or else, pytest will 
not run those tests. 

## Linting and Testing
Provided the Makefile works, running
``` 
make test
```
will clean old files, lint current files, then run all tests in the `tests` folder (i.e. do all commands below consecutively). Otherwise, running 
``` 
	find . -name '*.pyc' -exec rm -f {} \;
```
will clean up old `.pyc` executable files. Then, running
```
	./venv/bin/flake8 --ignore=F401 pokerbot tests 
```
will check all files in both `pokerbot` and `test` for syntax. Finally, running 
``` 
    ./venv/bin/python -m pytest pokerbot tests
```

## Version Control 

Version control is handled in the `requirements_dev.txt` file. 

## Built With 
* OpenCV 
* Random other stuff
* Bad smash players

## Authors

John Guo (jg852@cornell.edu) and Jonathan Moon (hyun.0714@gmail.com). 