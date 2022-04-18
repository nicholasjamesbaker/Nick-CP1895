"use strict";

// Query Selectors
const recipeForm = document.querySelector('#recipe-form');
const recipeContainer = document.querySelector('#recipe-container');
let listItems = [];
let file = document.getElementById("recipe_image");

// FUNCTIONS
function handleFormSubmit(e){
  e.preventDefault();
  const name = DOMPurify.sanitize(recipeForm.querySelector('#name').value);
  const ingredients = DOMPurify.sanitize(recipeForm.querySelector('#ingredients').value);
  const serving = DOMPurify.sanitize(recipeForm.querySelector('#serving').value);
  const prep = DOMPurify.sanitize(recipeForm.querySelector('#prep').value);
  const recipe_image = recipeForm.querySelector('#recipe_image').value;

  const newRecipe = {
    name,
    ingredients,
    serving,
    prep,
    recipe_image,
    id: Date.now()
  }
  listItems.push(newRecipe);
  e.target.reset();
  recipeContainer.dispatchEvent(new CustomEvent('refreshRecipes'));
}

function validateFileType(){
  var fileName = file.value,
  idxDot = fileName.lastIndexOf(".") + 1,
  extFile = fileName.substr(idxDot, fileName.length).toLowerCase();
  if (extFile=="jpg" || extFile=="jpeg" || extFile=="png"){
    alert("File is good to upload");
  }else{
    alert("Only jpg/jpeg and png files are allowed!");
    file.value = "";
  }
}

function displayRecipes(){
  const tempString = listItems.map(item => `
    <div class="col">
      <div class="card mb-4 rounded-3 shadow-sm border-primary">
        <div class="card-header py-3 text-white bg-primary border-primary">
          <h4 class="my-0">${item.name}</h4>
        </div>
        <div class="card-body">
          <ul class="text-start">
            <img src=${item.recipe_image}></img>
            <li><strong>Ingredients: </strong>${item.ingredients}</li>
            <li><strong>Serving Instructions: </strong>${item.serving}</li>
            <li><strong>Preparation Instructions: </strong>${item.prep}</li>
          </ul>
          <button class="btn btn-lg btn-outline-danger" aria-label="Delete ${item.name}" value="${item.id}">Delete Recipe</button>
        </div>
      </div>
    </div>
    `).join('');
  recipeContainer.innerHTML = tempString;
}

function mirrorStateToLocalStorage(){
  localStorage.setItem('recipeContainer.list', JSON.stringify(listItems));
}

function downloadCSV (arr) {

    var keys = [];
    var values = [];
    function getKeys(data, k = '') {
      for (var i in data) {
        var rest = k.length ? '_' + i : i
        if (typeof data[i] == 'object') {
          if (!Array.isArray(data[i])) {
            getKeys(data[i], k + rest)
          }
        } else keys.push( k+ rest)
      }
    }
    function getValues(data, k = '') {
      for (var i in data) {
        var rest = k.length ? '' + i : i
        if (typeof data[i] == 'object') {
          if (!Array.isArray(data[i])) {
            getValues(data[i], k + rest)
          }
        }
        else values.push(data[rest])
      }
    }

    getKeys(arr[0])
    var value="";
    arr.forEach(x=>{
       values=[];
       getValues(x);
       value+=values.join(";")+"\r\n";
    })

    let result = keys.join(";")+"\r\n"+value;
    let fileToSave = new Blob([result], {
       type: "csv",
       name: 'data.csv'
     });

    saveAs(fileToSave, 'recipes.csv');
  }

function loadinitialUI(){
  const tempLocalStorage = localStorage.getItem('recipeContainer.list');
  if(tempLocalStorage === null || tempLocalStorage === []) return;
  const tempRecipes = JSON.parse(tempLocalStorage);
  listItems.push(...tempRecipes);
  recipeContainer.dispatchEvent(new CustomEvent('refreshRecipes'));
}

function deleteRecipeFromList(id){
  listItems = listItems.filter(item => item.id !== id);
  recipeContainer.dispatchEvent(new CustomEvent('refreshRecipes'));
}

// EVENT LISTENERS
recipeForm.addEventListener("submit", handleFormSubmit);
recipeContainer.addEventListener('refreshRecipes', displayRecipes);
recipeContainer.addEventListener('refreshRecipes', mirrorStateToLocalStorage);
window.addEventListener('DOMContentLoaded', loadinitialUI);
recipeContainer.addEventListener('click', (e) => {
  if(e.target.matches('.btn-outline-danger')){
    deleteRecipeFromList(Number(e.target.value));
  };
})
