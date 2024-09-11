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

const QueryParams = new URLSearchParams(location.search);

const SearchForm = document.querySelector("form");

const RandomButton = document.querySelector(".randompage");

const PageIndex = document.querySelector(".page-index");
const AllPages = PageIndex.querySelectorAll("li");

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
          parsed.push([
              AllPages[index].dataset.title,
              AllPages[index].dataset.href
          ]);
          if (parsed.length == AllPages.length) {
              res(parsed);
          }
      } 
  });
}

async function sortpagelist(searchtext) {
    const sortfunc = (a, b) => {
        if (
            a[0].toLowerCase() == searchtext.toLowerCase()
        ) return 1
        if (
            a[0].toLowerCase().includes(searchtext.toLowerCase()) &&
            !(b[0].toLowerCase().includes(searchtext.toLowerCase()))
        ) return -1;
        if (
            !(a[0].toLowerCase().includes(searchtext.toLowerCase())) &&
            b[0].toLowerCase().includes(searchtext.toLowerCase())
        ) return 1;
        return 0;
    };
    const Pages = await listpages();
    const sortedpages = Pages.toSorted(sortfunc);
    for (let index in sortedpages) {
        const element = sortedpages[index];

        const Append = document.createElement("li");
        Append.dataset.title = element[0];
        Append.dataset.href = element[1];

        const anchor = document.createElement("a");
        anchor.href = element[1];
        anchor.textContent = element[0];
        Append.appendChild(anchor);
        PageIndex.appendChild(Append);
    }
}

async function getrandompage(fullredirect=false) {
    const Pages = await listpages();
    const randomindex = Math.floor(Math.random() * Pages.length);
    const randompage = Pages[randomindex];
    if (fullredirect) {
        location.replace(randompage[1]);
        return;
    }
    location.href = randompage[1];
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
