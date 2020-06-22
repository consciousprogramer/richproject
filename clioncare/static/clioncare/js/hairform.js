str_step0 = "Welcome, To Clion Care Free Hair Consultation";

document.querySelector(".question_header").innerHTML = str_step0;

// displayonly the welcome BANNER------------------------------>
console.log("Started");
var a = document.querySelectorAll(".all_container>div");
var l = a.length;
for(var i = 0;i < l;i++){
  a[i].style.display = "none";
}
document.querySelector(".container0").style.display = "flex";

// Userinput object creation------------------------------------>
function userInput(gender,hair_color,baldness_pattern,had_transplant,problem_since,how_bad,urgency,fname,age,email,mob_no){
  this.gender = gender;
  this.hair_color = hair_color;
  this.baldness_pattern = baldness_pattern;
  this.had_transplant = had_transplant;
  this.problem_since = problem_since;
  this.how_bad = how_bad;
  this.urgency = urgency;
  this.fname = fname;
  this.age = age;
  this.email = email;
  this.mob_no = mob_no;
}

// h1 values for different steps---------------------------------->
str_step0 = "Welcome, To Clion Care Free Hair Consultation";
str_step1 = "Please Choose Your Gender";
str_step2 = "Choose Your Hair color";
str_step3 = "What Is Your Hair Loss Pattern?";
str_step4 = "From How Many Years You Suffer, Hair Loss?";
str_step5 = "Do You Ever Had Hair Transplant?";
str_step6 = "How Bad Do You Feel About Your Current Hair condition?";
str_step7 = "When Do You Want Your Treatment To Begin?";
str_step8 = "Enter Your Details";

var str_list = [str_step0,str_step1,str_step2,str_step3,str_step4,str_step5,str_step6,str_step7,str_step8];

var paddingtop_list = [];
var paddingbottom_list = [];

// selecting  all the div----------->
var all_images = document.querySelectorAll(".all_container>div>div");
var len = all_images.length;
var step = 0;
var click_state = false;
var inputRecord = [];
var newinput = new userInput();
var clicked_btn;


// ---------adding EventListners to the divs------------------>
for(var i = 0;i < len; i++){
  all_images[i].addEventListener('click',divclick);
}

//removing the unecessary EventListners------------------>
// document.querySelector(".container4>div").removeEventListener("click", divclick);
// document.querySelector(".container8>div").removeEventListener("click", divclick);
// ------------------------------------------------------>
document.querySelector("#mob_no").oninput = function(){
  if(document.querySelector("#mob_no").value == "" && step > 7){
    document.querySelector("#next-btn").disabled = true;
  }
  else{
    document.querySelector("#next-btn").disabled = false;
  }
}

function do_reset(){
  console.log("doing reset....");
  click_state = false;
  step = 0;
  inputRecord.push(newinput);
  newinput = new userInput();
  console.log("done reset!");

}

// divClick handler function
function divclick(){
  clicked_btn = this.className;
  for(var k = 0;k < len;k++){
    all_images[k].style.border = "2px solid orange";
    all_images[k].addEventListener("mouseover",function(){
      this.style.border = "2px solid black";
    })
    all_images[k].addEventListener("mouseout",function(){
      if(this.className != clicked_btn){
        this.style.border = "2px solid orange";
      }
      else {
        this.style.border = "2px solid black";
      }
    })
  }
  click_state = true;
  this.style.border = "2px solid rgb(0,0,0)";

  switch (step) {
    case 0:
      // console.log("User clicked on banner, case = 0");
      click_state = false;
      break;
    case 1:
      newinput.gender = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 2:
      newinput.hair_color = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 3:
      newinput.baldness_pattern = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 4:
      newinput.problem_since = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 5:
      newinput.had_transplant = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 6:
      newinput.how_bad = this.className;
      // console.log("clicked: " + this.className);
      break;
    case 7:
      newinput.urgency = this.className;
      // console.log("clicked: " + this.className);
      break;

    }
}


//back btn handler-------------------------------------------------------->
document.querySelector(".back-btn").addEventListener("click",function(){
  if(step > 0){
    step--;
    // click_state = true;
    nextscreen();
  }

})


//next btn handler------------------------------------------------------------>
document.querySelector(".next-btn").addEventListener("click",function(){
  if(click_state == true){
    if(step > 0){
      step++;
      // if(step == 8){
      //   document.querySelector(".next-btn").innerHTML = "SUBMIT FORM";
      // }
      console.log("nextscreen called with step=" + step);
      nextscreen();
    }
    else{
      // when step == 8;
      // post the data to the server;
    }
  }
  else if (step == 0) {
    step++;
    console.log("nextscreen called with step=" + step);
    nextscreen();
  }
  // else if(step == 4){
  //   var value = document.querySelector("#scince_years").value;
  //     if(value > 0){
  //       step++;
  //       nextscreen();
  //     }
  //     else {
  //       alert("Please Valid Number of years!");
  //     }
  // }
})


function nextscreen(){
  var current_percentage = Math.round((step/9)*100).toFixed(0);
  // console.log(current_percentage);
  document.querySelector(".top_progress_bar>div").style.width = current_percentage + "%";
  document.querySelector(".top_progress_bar>div").innerHTML = current_percentage + "% Complete";
  // console.log("in nextscreen()");
  container_str = "container" + step;
  if(step == 9){
    newinput.fname = document.querySelector("#fname").value;
    newinput.age = document.querySelector("#age").value;
    newinput.email = document.querySelector("#email").value;
    newinput.mob_no = document.querySelector("#mob_no").value;
    document.querySelector(".container8").style.display = "none";
    document.querySelector(".status_div").style.display = "flex";
    var cpy = newinput;
    var myjson = JSON.stringify(cpy);
    console.log(myjson);
    // xhttp.open("POST", "ajax_test.asp", true);
    // xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
    // xhttp.send("fname=Henry&lname=Ford");
    xhr = new XMLHttpRequest();

    xhr.onload = function(){
      disp = document.querySelector("#display_status");
      disp.innerHTML = "Your form is submitted successfully,Thank you for filling the form";
      // document.querySelector("#anchor").style.display = "inline-block";
      // var bton = document.createElement("A");   // Create a <button> element
      // bton.innerHTML = "Now Click Here";
      // bton.href = "/clioncare/index"                  // Insert text
      // document.disp.appendChild(bton);
    }
    xhr.open("POST","/clioncare/hairform" , true);
    xhr.setRequestHeader("Content-type", "application/json");

    xhr.send(myjson);
    // do_reset();
    // python manage.py collectstatic --noinput --clear
  }
  else if(step <= 8){
    document.querySelector(".question_header").innerHTML = str_list[step];
    var all_slidables = document.querySelectorAll(".slidables");
    var len_slidables = all_slidables.length;
    for(var i = 0;i < len_slidables;i++){
      // all_slidables[i].classList.add("hide_slidables")
      all_slidables[i].style.display = "none";
    }
    // console.log("Container str = " + container_str);
    // document.querySelector("." + container_str).classList.add("show_slidables");
    if(step != 8){
      document.querySelector("." + container_str).style.display = "grid";
        document.querySelector("." + container_str).style.paddingTop = paddingtop_list[step];
        document.querySelector("." + container_str).style.paddingBottom = paddingbottom_list[step];
    }
    else if(step === 8) {
      document.querySelector("." + container_str).style.display = "flex";


    }
    click_state = false;
    // console.log("done nextscreen()");
  }

}
