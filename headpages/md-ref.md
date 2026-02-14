---
title: Markdown reference
subtitle: Reference for Markdown on this wiki.
---

This wiki uses an extended version of Markdown to generate pages. Here's a reference for how to do things in this extended Markdown format.

All of the following functionallity is provided entirely by [markdown2](https://github.com/trentm/python-markdown2).

<place-toc />

## Metadata

Various options may be in the metadata section of the file. Below is all metadata options available.

|    Name       |                                     Usage                                      | Required? |
|---------------|--------------------------------------------------------------------------------|-----------|
| `title`       | Sets the page title. Used for links and the page header.                       | Yes       |
| `subtitle`    | An additional title, sometimes used as a page description.                     | No        |
| `notoc`       | Disables the table of contents, defaults to false(table of contents is shown). | No        |
| `forcetitle`  | Force the tab title.                                                           | No        |
| `desc`        | Set the page description (open graph and normal meta).                         | No        |
This is an example of metadata section:
```
---
title: Markdown reference
subtitle: Reference for Markdown on this wiki.
---
```
## Basic formatting

| Usage | Example | Preview |
|-------|---------|---------|
| Bold  | `**Bold**` | **Bold** |
| Italics | `*Italics*` | *Italics* |
| Strike | `~~strike-through~~` | ~~strike-through~~ |
| Inline code | `` `Inline code` `` | `Inline code` |
## Headers
Headers allow you to group information in chunks.

Header above can be created with following markdown:
```
## Headers
```
## Paragraphs
To make a paragraph add an empty line between the two lines you want to separate:
```
Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah

Bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh
```
The above markdown outputs:

Blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah blah

Bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh bleh
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

## Code Blocks
Just like Inline code, but in a form of block.
````
```
"hello" + "world"
>> helloworld
```
````

The above markdown outputs: 

```
"hello" + "world"
>> helloworld
```

## Lists
Sometimes information looks nice as a list.

Unordered lists:
```
- Foo
- Fee
- Faa
```
The above markdown outputs: 

- Foo
- Fee
- Faa

Ordered lists:

```
1. Foo
2. Fee
3. Faa
```
The above markdown outputs: 

1. Foo
2. Fee
3. Faa

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

```latex
$$
y = \sqrt{x^2*\frac{z^3}{a*2}}+8
$$
```

$$
y = \sqrt{x^2*\frac{z^3}{a*2}}+8
$$

## TOC Placement

Although it'd be nice if the table of contents were to place itself directly after the first section, it unforchunately doesn't. If you would like to put it there, then you need to use the `<place-toc />` tag.

```md
Opening section

<place-toc />

## Next

## 2
```
