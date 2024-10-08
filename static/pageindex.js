/*
Copyright 2024 Nekoweb Wiki

This software is licensed under the 3-clause BSD license.
You should have recieved a copy of such license with this software,
if you did not, a copy can be found at the following

    https://opensource.org/license/BSD-3-Clause

Otherwise, a copy of the license can be found in the root directory
of the source files, see

    https://github.com/NekowebWiki/WikiGen
*/

import Fuse from "/fuse.mjs";

const PageIndex = document.querySelector(".page-index");
const AllPages = PageIndex.querySelectorAll("li");

const QueryParams = new URLSearchParams(location.search);

const SearchForm = document.querySelector("#search-form");

const RandomButton = document.querySelector(".randompage");

function formsubmit() {
    const searchtext = SearchForm.querySelector("#search").value;
    history.pushState({ search: searchtext }, document.title, "?q=" + encodeURIComponent(searchtext));
    sortpagelist(searchtext);
}

function listpages() {
  PageIndex.innerHTML = "";
  return new Promise((res, rej) => {
      let parsed = [];
      for (let index = 0; index < AllPages.length; index++) {
          parsed.push({
              "title": AllPages[index].dataset.title,
              "href":  AllPages[index].dataset.href,
              "desc": AllPages[index].dataset.desc
          });
          if (parsed.length == AllPages.length) {
              res(parsed);
          }
      } 
  });
}

async function sortpagelist(searchtext) {
    const Pages = await listpages();
    const fuse = new Fuse(
        Pages,
        {
            threshold: 1,
            keys: [
              "title",
              "desc"
            ]
        }
    );
    const sortedpages = fuse.search(searchtext)
    for (let index = 0; index < sortedpages.length; index++) {
        const element = sortedpages[index].item;

        const Append = document.createElement("li");
        Append.dataset.title = element.title;
        Append.dataset.href = element.href;
        Append.dataset.desc = element.desc

        const paragraph = document.createElement("p");
        paragraph.innerHTML = element.desc

        const strong = document.createElement("strong");
        const anchor = document.createElement("a");
        anchor.href = element.href;
        anchor.textContent = element.title;
        strong.appendChild(anchor);

        Append.appendChild(strong);
        Append.appendChild(paragraph);
        PageIndex.appendChild(Append);
    }
}

async function getrandompage(fullredirect=false) {
    const Pages = await listpages();
    const randomindex = Math.floor(Math.random() * Pages.length);
    const randompage = Pages[randomindex];
    if (fullredirect) {
        location.replace(randompage.href);
        return;
    }
    location.href = randompage.href;
}

SearchForm.addEventListener("submit", e => {
    e.preventDefault();
    formsubmit();
});
RandomButton.addEventListener("click", () => {
    getrandompage(false);
});

if (QueryParams.has("q")) {
    SearchForm.querySelector("input").value = decodeURIComponent(QueryParams.get("q"));
    formsubmit();
}
if (QueryParams.has("rand")) {
    getrandompage(true);
}
