// HANDLES THE NAVBAR background COLOR
document.addEventListener("scroll",function(){
  var a = document.querySelector(".navbar").classList;
  if (window.scrollY > 50){
    a.add("bg-light")

  }
  else{
    if("bg-light" in a == true){
    }
    else {
      a.remove("bg-light")
    }
  }
})


// NAVBAR WIDTH AND FREE ConsultationBUTTON STYLE CHANGER-------------------------
window.addEventListener("scroll",function(){
  var a = document.querySelector(".navbar-brand>img");
  var b = document.querySelector(".free_btn1").classList;
  if (window.scrollY > 60){
      a.style.width = "120px";
      if(window.scrollY > 140){
        b.remove("btn-outline-warning");
        b.add("btn-warning");
      }else {
        b.remove("btn-warning");
        b.add("btn-outline-warning");
      }
  }
  else {
    // console.log("else");
    a.style.width = "150px";
    if("btn-outline-warning" in b == true){
      // console.log("already in classList");
    }
    else {
      // console.log("not in classList");
      b.remove("btn-warning");
      b.add("btn-outline-warning");
    }
  }
})
