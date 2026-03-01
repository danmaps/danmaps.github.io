function _1(md){return(
md`# Virtual Numpad Qwerty Keyboard Mapping`
)}

function _caps(Inputs){return(
Inputs.toggle({ label: "Simulate Holding Down Caps Lock" })
)}

function _3(layout,caps){return(
layout(
  Object.fromEntries(
    ["M", ",", "J", "K", "L", "U", "I", "O", "7", "8", "9"].map((key) => [
      key,
      "numpad"
    ])
  ),
  caps
)
)}

function _layout(html,caps){return(
(set) => {
  let rows = ["1234567890-+", "qwertyuiop[]", "asdfghjkl;'", "zxcvbnm,./"].map(
    //todo only toUpperCase if caps is true!
    (s) => s.toUpperCase().split("")
  );

  const render = () => {
    const container = html`<div></div>`;

    // Add the reactive Caps Lock toggle button value (passed in as a parameter)
    // container.append(caps);

    const keyboardElement = html`<keyboard></keyboard>`;
    rows.forEach((row, i) => {
      const rowElement = html`<row style='padding-left:${i * 24}px'></row>`;
      row.forEach((key) => {
        const keyElement = html`<key class='${set[key]}'>
          ${caps ? remapKey(key) : key}
        </key>`;
        rowElement.append(keyElement);
      });
      keyboardElement.append(rowElement);
    });

    container.append(keyboardElement);

    container.append(html`<link href="https://fonts.googleapis.com/css?family=IBM+Plex+Mono:700&display=swap" rel="stylesheet">
    <style>
      keyboard {
        display: block;
        padding: 10px 0;
        background: black;
      }
      row {
        display: flex;
      }
      key {
        color: white;
        background: black;
        display: block;
        padding: 0px 10px;
        border: 1px solid grey;
        border-radius: 2px;
        margin: 5px;
        width: 18px;
        font-size: 30px;
        font-weight: 700;
        font-family: IBM Plex Mono;
      }
      .numpad {
        background: darkgrey;
        color: white;
      }
    </style>`);

    return container;
  };

  // Function to remap keys when CapsLock is active
  const remapKey = (key) => {
    const mapping = {
      M: "0",
      ",": "0",
      J: "1",
      K: "2",
      L: "3",
      U: "4",
      I: "5",
      O: "6"
    };
    return mapping[key] || key;
  };

  return render();
}
)}

export default function define(runtime, observer) {
  const main = runtime.module();
  main.variable(observer()).define(["md"], _1);
  main.variable(observer("viewof caps")).define("viewof caps", ["Inputs"], _caps);
  main.variable(observer("caps")).define("caps", ["Generators", "viewof caps"], (G, _) => G.input(_));
  main.variable(observer()).define(["layout","caps"], _3);
  main.variable(observer("layout")).define("layout", ["html","caps"], _layout);
  return main;
}
