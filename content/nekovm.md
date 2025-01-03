---
title: NekoVM
subtitle: This article covers the NekoVM.
---
NekoVM is a Linux emulator that runs in the browser used to build sites with static site generators or frameworks, and has (as stated by Dimden) support for any static site generator or framework.

It features Node.js, NPM, Python 3, and the ability to run additional programs via WebAssembly (WASM), all with full read/write access.

NekoVM can currently only be launched one time per minute (or 2 times per minute for donators), as it counts as a site export, which is rate limited.

<place-toc />

## History
- **08/04/24**: dimden announces that NekoVM is added:

  > most importantly, an actual gamechanger: introducing NekoVM, a Linux with Node.js and NPM running inside your browser, with full read/write access to your site filesystem.
  > 
  > what this means? you can now use any static site builder or framework to build your site. literally any framework, fr like actually! available to everyone too, not just donators!
  > theres also support for local port forwarding so you can for example run vite dev server with frameworks that support it :OOO
  >
  > this is still beta. report any bugs when u see them and backup ur site before doing anything in terminal. you can launch your site in terminal about once per minute (opening site in terminal counts to import/export zip rate limit which is currently 1 time per 1 minute (2 times for donators))
  >
  > i extremely recommend you watch video i made about me building demo Svelte app using Nekoweb Terminal to see how cool this thing is: https://lune.dimden.dev/4085d4ed0d4a.mp4 (video embed below)
  >
  > theres also 2 more cool features:
  > 
  > * you can now remove .html from your links! this was a very requested feature and now its here, you can enable this in site settings
  > * theres now support for setting custom HTTP headers for donators, also in settings!
  >
  > while NekoVM is still Beta, this update log marks Nekoweb Release&#x2122;, yea if u didnt notice nekoweb was still beta all this time. nekoweb has been running for almost 2 months now and most of issues have been fixed and things seem to run nicely. i hope itll continue to be this way
  >
  > thats all for now! check the video!!!!! its awesome

## Resources used
* https://nekoweb.org/
* [Nekoweb Discord](https://discord.gg/hvfHKyVS6b)
* https://lune.dimden.dev/4085d4ed0d4a.mp4
