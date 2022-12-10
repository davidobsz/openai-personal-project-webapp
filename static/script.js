    var button = document.getElementById("submit-prompt")
    var prompt = document.getElementById("prompt-input")

    function checkInput(){
        if (prompt.value == ""){
            alert("Prompt cannot be empty")
            return false
        }
    }