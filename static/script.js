var button = document.getElementById("submit-prompt")
var prompt = document.getElementById("prompt-input")
var loading_element = document.getElementById("load")
loading_element.style.visibility = "hidden"
function checkInput(){
    if (prompt.value == ""){
        alert("Prompt cannot be empty")
        return false
    }
}

function load(){
    setTimeout( null, 2000);
    loading_element.style.visibility = "visible"
    return true
}



