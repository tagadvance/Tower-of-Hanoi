default:
	echo "Nothing to do"

test:
	nosetests --nocapture --with-coverage --cover-package=hanoi
	coverage report -m --skip-covered