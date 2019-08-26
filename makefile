objects := $(filter-out base.html,$(patsubst ./html/%.html,%.html, $(wildcard ./html/*)))
all : $(objects) index.html

index.html: Home.html
	cp Home.html index.html

%.html: ./python/%.py ./text/%.txt ./html/%.html ./html/base.html
	python render.py $(subst .html,,$@)
