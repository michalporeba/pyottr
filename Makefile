grammar:
	rm -rf ./pyottr/grammar/*
	cd antlr && \
		java -jar antlr-4.12.0-complete.jar \
		-Dlanguage=Python3 -visitor -no-listener -o ../pyottr/grammar/ \
		Turtle.g4 stOTTR.g4 

try:
	python3 -m pyottr