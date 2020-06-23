SPHINX_SOURCES := index.rst conf.py
MATHJAX_URL := https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS_CHTML
SPHINX_OUT_DIR := ./html
GIT_COMMIT_HASH := $(shell git rev-parse HEAD)

all: sphinx

sphinx:
	sphinx-build . $(SPHINX_OUT_DIR)

# https://www.reddit.com/r/learnpython/comments/8dinw8/sphinx_github_pages_and_matplotlib/
publish: all
	ghp-import -n -m "publish-to-github from $(GIT_COMMIT_HASH)" -b gh-pages -p $(SPHINX_OUT_DIR)

clean:
	rm -rvf $(SPHINX_OUT_DIR)
