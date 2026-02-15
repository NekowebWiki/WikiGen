---
title: elements.css
subtitle: This guide covers the process of changing your site box, posts from your website's RSS feed and Follow button.
---
`elements.css` is a file that controls the appearance of several elements on your website. It can be accessed, either by adding `/elements.css` to the URL of any website hosted on Nekoweb, or by opening it in your website's directory.

<place-toc />
## Using images
All images used in `elements.css` must be under 1MB. Additionaly they should be linked like this: `https://your-username.nekoweb.org/your-username.nekoweb.org/rest-of-the-path-to-file`. The reason for that is because all of the files in your directory are stored in the folder called `your-username.nekoweb.org` (this only affects the `elements.css`, for different .css files, images and other files should be linked normally). You can store the images intended for `elements.css` in different folder if you want. Be aware that changing domain of your site might **not** change the name of `your-username.nekoweb.org` folder.
## Using fonts
You cannot link your own font and must use fonts that can be used without being linked (like `font-family: "Times New Roman"`).
## Site box
Site box is a small preview of your website on the [Nekoweb's Explore page](https://nekoweb.org/explore). You can use [Nekobox](https://jbc.lol/utils/nekobox/) or [remi's Sitebox Previewer for Nekoweb](https://github.com/fl0werpowers/nekoweb-sitebox-preview) to preview the sitebox in real time without the need to upload `elements.css` to Nekoweb.

Please note, the follow button `[+]` that appears on site boxes is unaffected by a `.follow` selector and needs to be accessed by a `.site-box .follow` selector  instead.

In order to change the appearance of a site box, you need to use the following css selectors: 
- `.site-box` to access the site box itself
- `.site-box .sitefeature` to access the image of website's preview 
- `.site-box > a > p` to access the domain of your website (top line)
- `.site-box > a > span` to access the title of your website (bottom line)
- `.site-box .follow` to access the follow button `[+]`

Additionally there are some things from [Nekoweb's FAQ](https://nekoweb.org/faq) that you should know about:

**Q: What are limits for elements.css?**

A: Max 1KB for free users or 5KB for donators. Additionally donators can overflow their site box 

**Q: Why my image is not loading in my site box?**

A: Make sure your image is less than 1MB. 

**Q: Why my site box has default style despite styling it?**

A: If any of images in your site box fail to load (too big, non-existent, etc), the entire site box style is reset to default. This is to prevent broken site box styles from being shown to users. 

**Q: My site is not appearing in Explore page**

A: You need to update your site a few times to appear in the explore page 

**Q: I updated my site but site preview didnt update**

A: site previews update every minute, if it still didnt update then there's 2 possible reasons:

- your index page is too big (dont forget to optimize ur assets) and takes more than 15 seconds to load
- chromium instance we use for screenshots died and u have to try again until it works 

**Q: I updated my site but its not updating on my page**

A: CTRL+SHIFT+R 
## RSS feed
Posts from your website's RSS feed appear in [Nekoweb's global RSS feed page](https://nekoweb.org/global-feed). You can use [Nekobox](https://jbc.lol/utils/nekobox/) to preview the style of the post in real time without a need to upload `elements.css` to Nekoweb.

In order to change it's appearance you need to use the following css selectors: 
- `.post-box` to access the post itself
- `.post-box .post-box-inner` to access the contents of the post
- `.post-box .post-author` to access the author of the post
- `.post-box .post-dot` to access the dot-separator between the author and date
- `.post-box .post-date` to access the date of the post
- `.post-box .post-title` to access the title of the post
- `.post-box .post-description` to access the description of the post
## Follow button
Follow button appears on your page if you put `<!--# follow -->` on it. You can read about it more [here](https://nekoweb.org/ssi). 

Please note, the follow button that appears on site boxes is unaffected by a `.follow` selector and needs to be accessed by a `.site-box .follow`.

In order to change the appearance of a Follow button, you need to use the following css selectors: 
- `.follow` to access the follow button for the website you are not following
- `.following` to access the follow button for the website you are already following