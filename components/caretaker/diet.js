var add = document.getElementById("add");
var clear = document.getElementById("clear");

var input = document.getElementById("input");
var calories = document.getElementById("calories");
var list = document.getElementById("list");

var medicine = document.getElementById("input_meds");
var medList = document.getElementById("medsList");

add_meds.addEventListener("click",addMeds);
add.addEventListener("click",addTask);
clear.addEventListener("click",clearlist);

function addTask(){
    var task = input.value;
    var cal = calories.value
    //console.log(task);
    var todotask = document.createElement("li");
    var todotext =  document.createTextNode(task+"-"+cal+" calories");
    todotask.appendChild(todotext);
    //console.log(todotask);
    list.appendChild(todotask);
    //console.log(list);
}

function addMeds(){
    var meds = medicine.value;
    var medsList = document.createElement("li");
    var medsText = document.createTextNode(meds);
    medsList.appendChild(medsText);
    medList.appendChild(medsList);

}

function clearlist(){
    var currentList = list.children;
    while(currentList.length > 0){
        currentList.item(0).remove();
    }
}
