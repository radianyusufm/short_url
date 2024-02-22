
document.addEventListener('DOMContentLoaded', function(){

    $("#modal-qrcode").on("hidden.bs.modal", function () {
        document.getElementById("modal-body").innerHTML = ''
    });

})



function generate_qr_code(link){
    new QRCode(document.getElementById("modal-body"), link);
}


function copy_text(text){
    navigator.clipboard.writeText(text);
}