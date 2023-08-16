const socket = new WebSocket(`ws://${window.location.host}`);
const messagelist = document.querySelector("ul");
const nickform = document.querySelector("#nickname");
const messageform = document.querySelector("#message");

const makeMessage = (type, payload) => {
  const msg = { type, payload };
  return JSON.stringify(msg);
};

socket.addEventListener("open", () => {
  console.log("Connected to Server ✅");
});

socket.addEventListener("message", (message) => {
  const li = document.createElement("li");
  li.innerText = message.data;
  messagelist.append(li);
});

socket.addEventListener("close", () => {
  console.log("Disconnected from Server ❌");
});

const handleSubmit = (event) => {
  event.preventDefault();
  const input = messageform.querySelector("input");
  socket.send(makeMessage("new_message", input.value));
  input.value = "";
};

const handleNickSubmit = (event) => {
  event.preventDefault();
  const input = nickform.querySelector("input");
  socket.send(makeMessage("nickname", input.value));
  input.value = "";
};

messageform.addEventListener("submit", (event) => {
  handleSubmit(event);
});

nickform.addEventListener("submit", (event) => {
  handleNickSubmit(event);
});
