# Maintain the site

The site has been built [MkDocs](https://www.mkdocs.org/). You need to:

- create a virtualenv
- `pip install mkdocs-material`
- `pip install mkdocs-git-revision-date-localized-plugin`
- `pip install pymdown-extensions `

All the markdown files are in [docs](https://github.com/SegmOnto/SegmOnto.github.io/tree/master/docs).

To run a local server: `mkdocs serve` and go to `http://127.0.0.1:8000/` on your browser.

To deploy the new version on the `gh-pages` branch (on which the website is stored): `mkdocs gh-deploy `.
