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

