{{DESTINATION}}:
	{{ENGINE}} {{DESTINATION}}.tex
clean:
	rm \
		{{DESTINATION}}.aux \
		{{DESTINATION}}.dvi \
		{{DESTINATION}}.fdb_latexmk \
		{{DESTINATION}}.fls \
		{{DESTINATION}}.log \
		{{DESTINATION}}.out \
		{{DESTINATION}}.pdf \
		{{DESTINATION}}.synctex.gz
