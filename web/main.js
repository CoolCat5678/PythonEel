document.addEventListener("DOMContentLoaded", () => {
    result = eel.load()()
    result.then(
        function(val)
        {
            val.forEach(element => {
                document.querySelector('#IDselect').innerHTML += `<option value="${element[0]}">${element[0]}</option>`
            });
        }
    );
  });

async function commit(){ 
    var commandText = document.querySelector('#SQLcommand').value
    result = await eel.SqlExec(commandText)()
    document.querySelector('#output').textContent = result
}

async function SelectID(SelectID){
    result = await eel.SelectID(SelectID)()
    document.querySelector('#output').textContent = result
}