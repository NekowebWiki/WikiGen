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
const settings = document.querySelector("#layout-form");

function ValueOrLocalStorage(wanted, name, value) {
  if (name != wanted) return localStorage.getItem(wanted);
  return value;
}

settings.addEventListener("submit", (event) => {
  event.preventDefault();
  const submitter = event.submitter;
  SetOption(submitter.name, submitter.value);
});

