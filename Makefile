all: Documents.html Home.html Members.html Suggestions.html index.html Calendar.html
%.html: sources/%.html
	make -C sources
	cp $< $@
index.html: sources/Home.html
	cp sources/Home.html index.html
