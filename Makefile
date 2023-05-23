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
	