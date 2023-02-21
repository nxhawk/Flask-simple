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
  await fetch("/logout")
    .then((response) => {})
    .then((data) => {
      window.location.href = "/login";
    })
    .catch((error) => {
      console.error("Error:", error);
    });
});
