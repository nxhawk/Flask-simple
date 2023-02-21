let stt = -1;
let edit = false;
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
  edit = false;
  document.getElementsByTagName("input")[0].value = "";
  document.getElementsByTagName("input")[1].value = "";
  document.getElementsByTagName("input")[2].value = "";

  document.getElementById("submit").innerText = "Add";
  document.querySelector("#modal h2").innerHTML = "New Movie";
  document.getElementById("modal").classList.add("open");
  document.querySelector("body").classList.add("stop-scrolling");
});

//add new
document.getElementById("submit").addEventListener("click", async () => {
  let name = document.getElementsByTagName("input")[0].value;
  let rate = document.getElementsByTagName("input")[1].value;
  let year = document.getElementsByTagName("input")[2].value;
  if (!edit) {
    await fetch("/movie", {
      method: "POST",
      body: JSON.stringify({ name, rate, year, user }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((response) => {})
      .then((json) => {
        window.location.href = `/${user}`;
      })
      .catch((err) => console.log(err));
  } else {
    await fetch("/movie", {
      method: "PUT",
      body: JSON.stringify({ name, rate, year, user, stt }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((data) => {
        //console.log(data);
        window.location.href = `/${user}`;
      })
      .catch((err) => console.log(err));
  }
});

//delete movie
const del = document.querySelectorAll(".del");
del.forEach((e, idx) => {
  e.addEventListener("click", async () => {
    await fetch("/movie", {
      method: "DELETE",
      body: JSON.stringify({ stt: idx }),
      headers: { "Content-type": "application/json; charset=UTF-8" },
    })
      .then((response) => response.json())
      .then((data) => {
        //console.log(data);
        window.location.href = `/${user}`;
      })
      .catch((err) => console.log(err));
  });
});

//edit move
const lname = document.querySelectorAll(".name");
const lrate = document.querySelectorAll(".rate");
const lyear = document.querySelectorAll(".year");

const ed = document.querySelectorAll(".edit");
ed.forEach((e, idx) => {
  e.addEventListener("click", async () => {
    edit = true;
    stt = idx;

    document.getElementById("submit").innerText = "Edit";
    document.querySelector("#modal h2").innerHTML = "Edit Movie";
    document.getElementById("modal").classList.add("open");
    document.querySelector("body").classList.add("stop-scrolling");

    document.getElementsByTagName("input")[0].value =
      lname[idx].querySelector("span").innerText;
    document.getElementsByTagName("input")[1].value =
      lrate[idx].querySelector("span").innerText;
    document.getElementsByTagName("input")[2].value =
      lyear[idx].querySelector("span").innerText;
  });
});
