grammar:
	rm -rf ./pyottr/grammar/*
	cd antlr && java -jar antlr-4.12.0-complete.jar -Dlanguage=Python3 Turtle.g4 Stottr.g4 -o ../pyottr/grammar/