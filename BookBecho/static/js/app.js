function showPassword(){
  console.log("Working");
  var x = document.getElementById('pass-content');
  console.log(x);
  if(x.type === "password"){
    x.type = "text";
  }else{
    x.type = "password";
  }
}

function showPasswordMob(){
  console.log("Working");
  var x = document.getElementById('pass-content-mob');
  console.log(x);
  if(x.type === "password"){
    x.type = "text";
  }else{
    x.type = "password";
  }
}
