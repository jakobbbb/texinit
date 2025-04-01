{{DESTINATION}}:
	latexmk {{DESTINATION}}.tex
clean:
	latexmk -C
