
// document.querySelector("#re_pass").addEventListener("input", function(){
//   if (pass1 != pass2)
//   {
//     alert("Passwords did not matach,please fill again")
//     pass2 = "";
//   }
// })

document.querySelector("#re_pass").oninput = function(){
  pass1 = document.querySelector("#pass1").value;
  pass2 = document.querySelector("#re_pass").value;
  if (pass1 === pass2)
  {
    document.querySelector("#pass_btn").innerHTML = "Password Matched"
    document.querySelector("#pass_btn").classList.remove("btn-danger")
    document.querySelector("#pass_btn").classList.add("btn-success")
  }
  else{
    console.log("no-match");
    
    document.querySelector("#pass_btn").innerHTML = "Password did Matched"
    document.querySelector("#pass_btn").classList.add("btn-danger")
    document.querySelector("#pass_btn").classList.remove("btn-success");
  }
}
