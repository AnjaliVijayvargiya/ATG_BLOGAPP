


console.log("ss")
var a = Math.floor(Math.random() * 10);
var b = Math.floor(Math.random() * 10);
function login(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == ''){
        alert('You must enter both')
    }

    var data = {
        'username' : username,
        'password' : password
    }

    fetch('/api/login/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        
        if(response.status == 200){
            window.location.href = 'http://127.0.0.1:8000/'
        }
        else{
            alert(response.message)
        }

    })

}

function A(){
    document.getElementById('demo').innerHTML = a
}
function B(){
    document.getElementById('demo1').innerHTML = b
}

function register(){
    var username = document.getElementById('loginUsername').value
    var password = document.getElementById('loginPassword').value
    var cpassword = document.getElementById('loginCPassword').value
    var captcha = document.getElementById('captchaid').value
    
    var csrf = document.getElementById('csrf').value

    if(username == '' && password == '' && cpassword == '' && captcha == ''){
        alert('You must enter all')
    }

    var data = {
        'username' : username,
        'password' : password,
        'cpassword' : cpassword,
        'captcha' : captcha,
        'a':a,
        'b':b
    }

    fetch('/api/register/' , {
        method : 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken' : csrf,
        },
       
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => {
        console.log(response)
        if(response.status == 200){
          
        }
        else{
            alert(response.message)
        }

    })

}