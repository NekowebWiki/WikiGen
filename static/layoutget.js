const defaults = {
  textsize: "16px",
  width: null
}

SetOpts({
  width: localStorage.getItem("width"),
  textsize: localStorage.getItem("textsize")
});

function SetOpts(opts) {
  for (let opt in opts) {
    let val = opts[opt];
    SetOption(opt, val);
  }
}

function ValueSet(opt, value) {
  switch (opt) {
    case "textsize":
      document.documentElement.style.fontSize = value;
      break;
    case "width":
      document.documentElement.dataset.width = value;
      break;
  }
}

function SetOption(opt, value) {
  if (value === null)
    return;
  var setvalue = value;
  if (value == "__unset__") {
    setvalue = defaults[opt];
    localStorage.removeItem(opt);
  } else
    localStorage.setItem(opt, value);
  ValueSet(opt, setvalue);
}
