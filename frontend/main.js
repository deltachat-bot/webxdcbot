function h(tag, attributes, ...children) {
  const element = document.createElement(tag);
  if (attributes) {
    Object.entries(attributes).forEach((entry) => {
      element.setAttribute(entry[0], entry[1]);
    });
  }
  element.append(...children);
  return element;
}

window.sendMsg = () => {
  const text = document.getElementById("input").value;
  document.getElementById("input").value = "";

  window.webxdc.sendUpdate(
    {
      payload: {
        request: {
          name: window.webxdc.selfName,
          text,
        },
      },
    },
    "",
  );
};

window.webxdc.setUpdateListener(function (update) {
  const chat = document.getElementById("chat-area");
  const msg = update.payload.request || update.payload.response;
  chat.append(
    h(
      "p",
      { class: "msg" },
      h("span", { class: "nick" }, msg.name, ": "),
      msg.text,
    ),
  );
});

window.deviceName.innerHTML = "You are: " + window.webxdc.selfName;
