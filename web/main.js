async function commit(){ 
    var commandText = document.querySelector('#SQLcommand').value
    result = await eel.SqlExec(commandText)()
    document.querySelector('#output').textContent = result
}