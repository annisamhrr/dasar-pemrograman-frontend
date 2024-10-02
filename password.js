var password = prompt("Apa Password Kamu ?");

if(password=="Momentum"){
    document.write("<p>Password yang anda masukkan benar yaitu : "+ password +"</p>");
} else {
    alert("Maaf password anda salah..silahkan coba lagi ");
    window.location = "dialog_prompt.html";
}