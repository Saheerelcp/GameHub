function passwordchecking(){
    password1 = document.getElementById('password1').value
    password2 = document.getElementById("password2").value
    if (password1 !== password2){
        console.log('unmatched')
        document.querySelector(".password-mismatch").style.display = 'block'
        return false
    }
    else{
        document.querySelector('.password-mismatch').style.display = 'none'
    }
}
const pass = document.getElementById('password1')
pass.addEventListener('input',() => {
    if (pass.value.length === 8 || pass.value.length >= 8){
        document.querySelector('.password-count').classList.add("d-none")
    }
    else if (pass.value.length < 8 ){
        document.querySelector('.password-count').classList.remove('d-none')
    }
})
console.log('hello world')
