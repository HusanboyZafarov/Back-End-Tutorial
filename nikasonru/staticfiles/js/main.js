window.addEventListener("scroll", () => {
  let header = document.querySelector("header")
  header.classList.toggle("scrolled", window.scrollY > 0)
})


let header_burger = document.querySelector(".header_burger"),
  lines = document.querySelectorAll(".line"),
  header_list = document.querySelector(".header_list"),
  body = document.body
header_burger.addEventListener("click", () => {
  for (let i = 0; i < lines.length; i++) {
    lines[i].classList.toggle("opened")
  }
  header_list.classList.toggle("opened")
})

let header_item = document.querySelectorAll(".header_item")
for (let i = 0; i < header_item.length; i++) {
  header_item[i].addEventListener("click", () => {
    for (let i = 0; i < lines.length; i++) {
      lines[i].classList.toggle("opened")
    }
    header_list.classList.toggle("opened")
  })
}
let form_btn = document.querySelector(".form_btn"),
  message_for_user = document.querySelector(".message_for_user"),
  form_wrapper = document.querySelector(".form_wrapper"),
  my_form = document.querySelector(".my_form"),
  opener_btn = document.querySelector(".opener_btn")
opener_btn.addEventListener("click", () => {
  form_wrapper.classList.toggle("opened")
})
form_btn.addEventListener("click", () => {
  if (my_form.valid()) {
    message_for_user.style.display = "block"
  }
  form_wrapper.classList.add("closed", my_form.valid())
  setTimeout(closed_func, 2000)
  function closed_func() {
    message_for_user.classList.add("closed")
  }
})