objects := $(patsubst sources/%,%,$(patsubst %.shtml,%.html,$(wildcard ./sources/Sources/*.shtml)))
resources := $(patsubst sources/%,%,$(wildcard ./sources/Resources/*))
all: $(wildcard ./sources/*) Documents.html Home.html Members.html Suggestions.html index.html Calendar.html $(resources)
	make -C sources
%.html: sources/%.html
	cp $< $@
index.html: sources/Home.html
	cp sources/Home.html index.html
./Resources/%: sources/Resources/%
	cp $< $@
