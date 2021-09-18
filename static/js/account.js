const nav_header = document.querySelector(".nav__header");

nav_header.classList.add("account__header");

const changeButton = document.getElementById("changingEffect");
changeButton.style.display = "none"

function myFunction() {
    const desig = document.getElementById("designation");
        if (desig.style.display === "none") {
          desig.style.display = "block"
          
      } else {
        desig.style.display = "none"
        changeButton.style.display = "block"
      }
    }  

    const update = document.getElementById("updateButton")
    const desig = document.getElementById("designation")

    function newFun(){
        const input = document.getElementById("userInput").value
        desig.innerText = input
        if (changeButton.style.display === "none"){
            changeButton.style.display = "block"
        } else{
            changeButton.style.display = "none"
            desig.style.display = "block"
        }
    }

    const cancel = document.getElementById("cancelButton")

    function mySecondFunction(){
        desig.style.display = "block"
        if (changeButton.style.display === "block"){
            changeButton.style.display = "none"
        }else {
            changeButton.style.display = "block"
        }
    }