---
title: elements.css
subtitle: This guide covers the process of changing your site box, posts from your website's RSS feed and Follow button.
---

`elements.css` is a file that controls the appearance of several elements on
your website. It must be at maximum 1.5 kb for free users, or 7.5 kb for paid
users. Any Nekoweb site's `elements.css` can be access by entering
`/elements.css` after the site's domain.

<place-toc />

## Using images

All images used in `elements.css` must be &#8804; 1MB, and must be linked using
not only the full web address of the website, but should also use the full
canonical path to the image as seen in the dashboard. No other CSS files are
affected by this, it is only `elements.css`.

## Using fonts

Custom fonts cannot be used; this means only system fonts, or ones already
included in the explore page, are usable.

## Site box

Site boxes are small previews of sites on [Nekoweb's explore page](https://nekoweb.org/explore).

Please note, the follow button `[+]` that appears on site boxes is unaffected
by a `.follow` selector and needs to be accessed by a `.site-box .follow` selector
instead.

In order to change the appearance of a site box, you need to use the following
css selectors:

- `.site-box` to access the site box root
- `.site-box .sitefeature` to access the preview 
- `.site-box > a > p` to access the domain of the website (top line)
- `.site-box > a > span` to access the title of the website (bottom line)
- `.site-box .follow` to access the follow button `[+]`

Cute kitty or above users get the ability to overflow their site box's content,
making which means making it go outside the borders of the site box.

In the case of a site box's content not loading, the site box shows up with default
syling. The reason for this is to make sure broken site boxes don't show up.[^1]

There are also some tools used to preview site boxes without them needing to be
uploaded onto Nekoweb:

* [Nekobox](https://jbc.lol/utils/nekobox/),
* [remi's Sitebox Previewer](//github.com/fl0werpowers/nekoweb-sitebox-preview)

## RSS feed posts

Posts from your website's RSS feed appear in [Nekoweb's global RSS feed page](https://nekoweb.org/global-feed).

In order to change it's appearance you need to use the following css selectors: 

- `.post-box` to access the post itself
- `.post-box .post-box-inner` to access the contents of the post
- `.post-box .post-author` to access the author of the post
- `.post-box .post-dot` to access the dot-separator between the author and date
- `.post-box .post-date` to access the date of the post
- `.post-box .post-title` to access the title of the post
- `.post-box .post-description` to access the description of the post

There are also some tools used to preview them without the elements file
needing to be uploaded to Nekoweb:

* [Nekobox](https://jbc.lol/utils/nekobox/),

## Follow button

Follow buttons appear on pages where `<!--# follow -->` is put. This is done
using a system called [SSI](https://nekoweb.org/ssi). The follow button that
appears on [site boxes](#site-boxes) isn't the same as the follow button styled
with these selectors.
<!-- We should make an SSI guide. -->

In order to change the appearance of a Follow button, the following selectors
can be used: 

- `.follow` accesses the follow button
- `.following` accesses the follow button when visitors are following the site.

## Citations

[^1]: https://nekoweb.org/faq
      "Why my site box has default style despite styling it?"
