objects := $(patsubst Sources/%,%,$(patsubst %.shtml,%.html,$(wildcard ./sources/Sources/*.shtml)))
all: $(wildcard ./sources/*) Documents.html Home.html Members.html Suggestions.html index.html Calendar.html
	make -C sources
%.html: sources/%.html
	cp $< $@
index.html: sources/Home.html
	cp sources/Home.html index.html
