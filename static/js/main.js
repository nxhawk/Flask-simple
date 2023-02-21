//get username
const user = document.querySelector("span").dataset.usr;

//scroll handel navbar
window.onscroll = function () {
  myFunction();
};

function myFunction() {
  if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20)
    document.querySelector("header").className = "active";
  else document.querySelector("header").className = "";
}

//logout
document.getElementById("logout").addEventListener("click", async () => {
  await fetch("/logout", {
    method: "POST",
    body: JSON.stringify({ user: user }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  })
    .then((response) => {})
    .then((json) => {
      window.location.href = "/login";
    })
    .catch((err) => console.log(err));
});
//close modal
document.getElementById("close").addEventListener("click", () => {
  document.getElementById("modal").classList.remove("open");
  document.querySelector("body").classList.remove("stop-scrolling");
});

//new movie
document.getElementById("new").addEventListener("click", async () => {
  document.getElementById("modal").classList.add("open");
  document.querySelector("body").classList.add("stop-scrolling");
});

//add new
document.getElementById("submit").addEventListener("click", async () => {
  let name = document.getElementsByTagName("input")[0].value;
  let rate = document.getElementsByTagName("input")[1].value;
  let year = document.getElementsByTagName("input")[2].value;
  await fetch("/newMovie", {
    method: "POST",
    body: JSON.stringify({ name, rate, year, user }),
    headers: { "Content-type": "application/json; charset=UTF-8" },
  })
    .then((response) => {})
    .then((json) => {
      window.location.href = `/${user}`;
    })
    .catch((err) => console.log(err));
});
