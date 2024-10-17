---
title: Custom domains and subdomains
desc: Domains using Nekoweb
---
[Nekoweb](/w/nekoweb.html) allows for either a subdomain of `nekoweb.org` or your own domain to be used for your website.

<place-toc/>
## Custom domains
With Nekoweb, you have the ability to add your own custom domain(s) to your site. You need to be a donator to do this.

Free users only have access to one subdomain. However, donators can have multiple subdomains.[^faq-res] *Cat tier* donators get 1 subdomain, whereas *Cute kitty tier* donators get up to 10.[^max-domains]

## Subdomains
A subdomain is a prefix to a domain name, such as `https://subdomain.domainname.tld`.

On Nekoweb, when registering an account, your username becomes the subdomain of the domain nekoweb.org (like [wiki.nekoweb.org](/)), what points to your site.

As donator, you can multiple subdomains.[^faq-res] *Cat tier* donators get 1 subdomain, whereas *Cute kitty tier* donators get up to 10.[^max-domains]

### Types of subdomains on Nekoweb
Nekoweb supports 3 types of subdomains: Text only, Numbers only, Text and numbers, and dashed.[^has-dash]

<figure markdown="1" style="float:right;width:414px"><img src="/i/secure-conn-failed.png" width="414" height="178"/><figcaption markdown="1">`SSL_ERROR_NO_CYPHER_OVERLAP` error, as seen in Firefox, and Firefox derived, web browser.</figcaption></figure>
### Nested subdomains on Nekoweb

You can add nested subdomains as a Nekoweb subdomain (As of 14/5/24), but they're inaccessible, as most browsers prevent the page from loading. You'll likely see an error about the server, Nekoweb, and the client, your browser, not having a common encyption algorithm.[^has-dots]

### Character Limit

Nekoweb subdomains have a character limit of 32 characters.[^max-len]

### Punycode

Punycode is not supported in nekoweb subdomains.

## Resources used/Credits
* https://nekoweb.org/
* [Nekoweb Discord](https://discord.gg/hvfHKyVS6b)

## References
[^has-dots]: https://this.has.dots.nekoweb.org/ (non-functional), thanks to [Tepiloxtl](https://tepiloxtl.net/)!
[^has-dash]: https://this-has-dashes.nekoweb.org/, thanks to [Tepiloxtl](https://tepiloxtl.net/)
[^max-len]: https://thirtytwocharsnekoweborgdomains.nekoweb.org/, thanks to [Tepiloxtl](https://tepiloxtl.net/)
[^faq-res]: https://nekoweb.org/faq, *I don't have a domain but I want to host a second or more sites, is it possible?*
[^max-domains]: https://nekoweb.org/donate
