# WikiGen

I bare bones static site generator made specifically for the Nekoweb wiki.

All content should be fully ported over now. However, more stuff may need to be
done.

## Contributing

* For contributing to the static site generator, please read [`CONTRIBUTING.md`](CONTRIBUTING.md).
* A contributing guide for the wiki itself is still WIP.

## Local Development

Before you can develop this locally, you'll need a few programs:

* Python
* PIP

### Get Dependencies

```bash
pip install -r requirements.txt
```

### Build

```bash
python main.py
```

### Dev Server

I do not currently know a good development server for Nekoweb sites,
bear with me.

## Directories

<!-- This table is a complete formatting nightmare lol -->

| Repo        | On Nekoweb | Purpose                                                                                   |
|-------------|------------|-------------------------------------------------------------------------------------------|
| `images`    | `/i`       | Static directory; contains embeded content on the wiki, such as images in the main content of pages.|
| `content`   | `/w`       | Parsed/MD directory; contains primary wiki pages, these are all included in `pages.html`. |
| `headpages` | `/`        | Parsed/MD directory; pages not under `/w` that still adhear to the formatting: `index`,`about`, `notfound`.|
| `static`    | `/`        | Static direcotry; static content that doesn't fall under `/i`: wiki background, `style.css`, `elements.css`, favicon, etc. |

## Licensing

* `main.py`, `RenderUtils.py` and `MiscUtils.py` all use the GPL v3-or-later. A copy of this license can be
  found at `/GPLv3.txt` in the source repository.
* `config.py` is under the Unlicense. A copy of this license can be found within the file itself.
* Wiki content is not currently licensed, this is still actively in discussion.
* Views are not currently licensed, this hasn't been discussed yet, but should be.
