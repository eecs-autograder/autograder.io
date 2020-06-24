# UI Documentation Source
This folder contains the source code for Autograder.io's UI documentation. It is written using [reStructuredText](https://docutils.sourceforge.io/docs/ref/rst/directives.html) and compiled using [Sphinx](http://www.sphinx-doc.org/).

## Setup and Build
First, install the required Python dependencies using
[Pipenv](https://pypi.org/project/pipenv/):
```
$ cd docs
$ pipenv install
```

To build the HTML output (resulting files will be in the `html` directory):
```
$ make
```

To build and publish the result to GitHub pages (admins only):
```
$ make publish
```

This uses the [`ghp-import`](https://pypi.org/project/ghp-import/)
tool to push the output to the `gh-pages` branch of this repository,
which is the branch used for publishing to
https://eecs-autograder.github.io/autograder.io/.
