# WikiGen

I bare bones static site generator made specifically for the Nekoweb wiki.

This is still being built, and doesn't yet produce usable output.

## Directories

| Repo        | On Nekoweb | Purpose |
|-------------|------------|---------|
| `images`    | `/i`       | Static directory; contains embeded content on the wiki, such as images in the main content of pages. |
| `content`   | `/w`       | Parsed/MD directory; contains primary wiki pages, these are all included in `pages.html`. |
| `headpages` | `/`        | Parsed/MD directory; pages not under `/w` that still adhear to the formatting: `index`, `about`, `notfound`.|
| `static`    | `/`        | Static direcotry; static content that doesn't fall under `/i`: wiki background, `style.css`, `elements.css`, favicon, etc. |
