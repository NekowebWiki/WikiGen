---
title: Markdown Reference
subtitle: Reference for Markdown on this wiki.
---

This wiki uses an extended version of Markdown to generate pages. Here's a reference for how to do things in this extended Markdown format.

All of the following functionallity is provided entirely by [markdown2](https://github.com/trentm/python-markdown2).

## Metadata

Various options may be in the metadata section of the file. Below is all metadata options available.

|    Name       |                                     Usage                                      | Required? |
|---------------|--------------------------------------------------------------------------------|-----------|
| `title`       | Sets the page title. Used for links and the page header.                       | Yes       |
| `subtitle`    | An additional title, sometimes used as a page description.                     | No        |
| `notoc`       | Disables the table of contents, defaults to false(table of contents is shown). | No        |
| `forcetitle`  | Force the tab title.                                                           | No        |

## Basic formatting

| Usage | Example | Preview |
|-------|---------|---------|
| Bold  | `**Bold**` | **Bold** |
| Italics | `*Italics*` | *Italics* |
| Strike | `~~strike-through~~`| ~~strike-through~~ |

## Links and Images

You can add links to pages using the usual Markdown syntax, that being `[text to display](https://example.com)`, which renders to [text to display](https://example.com).

Images can also be added to pages using Markdown syntax, however, for many cases, the best option is to use `<img />` tags, as they allow for flexibility. If you'd like to add a caption, consider using `<figure>` instead.

```html
<figure>
  <img src="/notanimage.png" alt="Wow! No image!" />
  <figcaption>Wow! No image!</figcaption>
</figure>

<img src="/notanimage.png" alt="Wow! No image!" />
```

Using HTML tags is better because it allows resizing of the image, as well as for `<figure>`, allowing a caption to be added (this may have unique stying at some point).

## Tables

Tables allow for information to be presented neatly.

```md
|       Name       |       Slug       |
|------------------|------------------|
| Tables           | tables           |
| Basic formatting | basic-formatting |
```

The above markdown outputs:

|       Name       |       Slug       |
|------------------|------------------|
| Tables           | tables           |
| Basic formatting | basic-formatting |

Note that tables don't need good formatting to work. This works just fine:

```md
|Name|Slug|
|-|-|
|Tables|tables|
|Basic formatting|basic-formatting|
```

## MathML

This wiki includes a way to render LaTeX equations to MathML. Simply surround LaTeX with `$$...$$` or `$...$`.

<!-- Nothing provided right now, if somebody does know how to use LaTeX to, I'd appriciate a PR! -->
