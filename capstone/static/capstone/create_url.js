
document.addEventListener('DOMContentLoaded', function(){
    
    document.getElementById("form_Password").style.display = 'none';

    document.querySelector('#password_true').addEventListener('change', function(event){
        event.preventDefault()
        const cb = event.target;
        if (cb.checked){
            document.getElementById("form_Password").style.display = 'block';
        } else {
            document.getElementById("form_Password").style.display = 'none';
        }
    })


})
