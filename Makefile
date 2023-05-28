grammar:
	rm -rf ./pyottr/grammar/*
	cd antlr && \
		java -jar antlr-4.12.0-complete.jar \
		-Dlanguage=Python3 -visitor -no-listener -o ../pyottr/grammar/ \
		Turtle.g4 stOTTR.g4 

	touch ./pyottr/grammar/__init__.py

try:
	python3 -m pyottr
	

style:
	isort --multi-line 3 --profile black --skip ./pyottr/grammar ./pyottr	
	isort --multi-line 3 --profile black ./tests 
	black --exclude /grammar/ ./pyottr
	black ./tests
	flake8 --max-line-length=88 --select=C,E,F,W,B,B950 --extend-ignore=E203,E501,W503 --extend-exclude=*/grammar/* ./pyottr
	flake8 --max-line-length=88 --select=C,E,F,W,B,B950 --extend-ignore=E203,E501,W503 ./tests


upgrade: 
	pip list --outdated | grep -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install --upgrade   