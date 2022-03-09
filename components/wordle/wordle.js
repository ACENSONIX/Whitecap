let enter = document.getElementById("enter");
let keys = document.querySelectorAll("button.keys");
let backspace = document.getElementById("Backspace");
let guess1 = document.getElementById("guessTable");
let container = document.getElementsByClassName("container");
let answer = null;
// let attempt = "";
let count_correct = 0;
let i = 1,
  j = 1;

keys.forEach((key) => {
  key.addEventListener("click", () => {
    if (j > 5 && j != 6) {
      alert("Cannot enter more words");
    } else if(j==6){
      container.classList.add("unclickable");
    } else {
      console.log(keys.innerText);
      guess1.rows[i - 1].cells.item(j - 1).innerHTML = key.innerHTML;
      // attempt += key.innerHTML;
      j++;
    }
  });
});

enter.addEventListener("click", () => {
  if (j == 6 && i < 7) {
    //#region comment
    // console.log(enter.textContent);
    // for (let x = 0; x < 5; x++) {
    //   if (guess1.rows[i - 1].cells.item(x).innerHTML == answer[x]) {
    //     guess1.rows[i - 1].cells.item(x).classList.add("bg-green");
    //   } else if (
    //     guess1.rows[i - 1].cells.item(x).innerHTML == answer[0] ||
    //     guess1.rows[i - 1].cells.item(x).innerHTML == answer[1] ||
    //     guess1.rows[i - 1].cells.item(x).innerHTML == answer[2] ||
    //     guess1.rows[i - 1].cells.item(x).innerHTML == answer[3] ||
    //     guess1.rows[i - 1].cells.item(x).innerHTML == answer[4]
    //   ) {
    //     guess1.rows[i - 1].cells.item(x).classList.add("bg-yellow");
    //   } else {
    //     guess1.rows[i - 1].cells.item(x).classList.add("bg-wrong");
    //   }
    // }
    //#endregion
    attempt =
      guess1.rows[i - 1].cells.item(0).innerHTML +
      guess1.rows[i - 1].cells.item(1).innerHTML +
      guess1.rows[i - 1].cells.item(2).innerHTML +
      guess1.rows[i - 1].cells.item(3).innerHTML +
      guess1.rows[i - 1].cells.item(4).innerHTML;
    axios
      .get("http://127.0.0.1:8000/" + attempt)
      .then((response) => {
        answer = response.data;
        for (let x = 0; x < 5; x++) {
          if (answer[x] == "g") {
            guess1.rows[i - 1].cells.item(x).classList.add("bg-green");
            count_correct++;
            
          } else if (answer[x] == "y") {
            guess1.rows[i - 1].cells.item(x).classList.add("bg-yellow");
          } else if (answer[x] == "w") {
            guess1.rows[i - 1].cells.item(x).classList.add("bg-wrong");
          }
        }
        i++;
        j = 1;
        if(count_correct == 5){
             j = 6;
        }
      })
      .catch((error) => console.log(error));
  } else {
    alert("Enter the full word");
  }
});

backspace.addEventListener("click", () => {
  if (j > 1) {
    guess1.rows[i - 1].cells.item(j - 2).innerText = "";
    j--;
  }
});

//console.log(j);
//console.log(key.textContent);
//let array_of_guess1 = guess1.children;
//console.log(guess1);

/*
let guess1 = document.getElementById("guessTable");
console.log(guess1.rows[0].cells.item(3).innerHTML);
*/
