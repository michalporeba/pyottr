grammar:
	rm -rf ./ottrlib/grammar/*
	cd antlr && \
		java -jar antlr-4.13.0-complete.jar \
		-Dlanguage=Python3 -visitor -no-listener -o ../ottrlib/grammar/ \
		Turtle.g4 stOTTR.g4 

	touch ./ottrlib/grammar/__init__.py

style:
	isort --multi-line 3 --profile black --skip ./ottrlib/grammar ./ottrlib
	isort --multi-line 3 --profile black ./tests 
	black --exclude /grammar/ ./ottrlib
	black ./tests
	flake8 --max-line-length=88 --select=C,E,F,W,B,B950 --extend-ignore=E203,E501,W503 --extend-exclude=*/grammar/* ./ottrlib
	flake8 --max-line-length=88 --select=C,E,F,W,B,B950 --extend-ignore=E203,E501,W503 ./tests


upgrade: 
	pip list --outdated | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install --upgrade   