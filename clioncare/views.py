from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse
from django.contrib import messages
from .models import usermessage, patient
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    return render(request, "clioncare/index.html")

def costpage(request):
    return render(request, "clioncare/costpage.html")

def chatform(request):
    if request.method == "POST":
        fname = request.POST["fullname"]
        email = request.POST["email"]
        message = request.POST["message"]
        mob_no = request.POST["mob_no"]
        newchatdata = usermessage.objects.create(fname=fname,email=email,message=message,mob_no=mob_no)
        try:
            newchatdata.save()
            messages.success(request, "Your form was submited sucessfully!, Mr Vikas will contact you within 2-3 hrs Thank You.")
            return render(request, "clioncare/index.html")
        except Exception as e:
            messages.error(request, "You entered invalid data,please retry!")
            return render(request, "clioncare/index.html")

    else:
        messages.info(request, "enter some data in the form below first,then submit")
        return render(request, "clioncare/index.html")
@csrf_exempt
def hairform(request):
    # if post method
    # if request.is_ajax():---------->>what is this???
    if request.method == "POST":
        raw_data = json.loads(request.body)
        print(raw_data)
        raw_json_data = json.dumps(raw_data)
        gender = raw_data["gender"]
        hair_color = raw_data["hair_color"]
        baldness_pattern = raw_data["baldness_pattern"]
        had_transplant = raw_data["had_transplant"]
        problem_since = raw_data["problem_since"]
        how_bad = raw_data["how_bad"]
        urgency = raw_data["urgency"]
        fullname = raw_data["fname"]
        age = int(raw_data["age"])
        email = str(raw_data["email"])
        mob_no = raw_data["mob_no"]
        print(type(request.body))
        new_patient = patient.objects.create(
                                                # raw_json_data = raw_json_data,
                                                gender=gender,
                                                hair_color = hair_color,
                                                baldness_pattern = baldness_pattern,
                                                had_transplant = had_transplant,
                                                problem_since = problem_since,
                                                how_bad = how_bad,
                                                urgency = urgency,
                                                fullname = fullname,
                                                age = age,
                                                email = email,
                                                mob_no = mob_no)
        new_patient.save()
        messages.success(request, "Your data was send to our Expert doctors, after analysing it,we will contact you, Have a nice day!")
        return redirect(reverse("clioncare:index"))
        print("in success")
        # except Exception as e:
        #     print("in failed")
        #     messages.error(request, "Your data was not send,some error occured please inform us by clicking on Q&A button on bottom right of screen!")
        #     return render(request, "clioncare/index.html")


        # # if get method
        # return redirect(request, "clioncare/hairform.html")

    # if get method
    else:
        return render(request,"clioncare/hairform.html")

@csrf_exempt
def createuser(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST.get("pass")
        re_pass = request.POST.get("re-pass")
        if User.objects.filter(username = username).exists():
            messages.error(request, 'This username = ' + f"{username}" + ' already exists please choose another one!')
            return render(request,"clioncare/createuser.html")
        else:
            new_user = User.objects.create_user(username,email,password)
            new_user.first_name = fname;
            new_user.last_name = lname;
            new_user.save()
            messages.success(request, 'your account was created sucessfully with'+ f" username : {username}")
            return render(request,"clioncare/login.html")
        # else:
        #     messages.error(request, "Passwords did not matach, please re-enter password carefully!")
        #     return render(request,"clioncare/createuser.html")
    else:
        return render(request, "clioncare/createuser.html")



def userlogin(request):
    if request.method == "POST":
        loginusername = request.POST["username"]
        loginpassword = request.POST["your_pass"]
        user = authenticate(username = loginusername,password = loginpassword)
        if user is not None:
            login(request, user)
            messages.info(request,"You are now LoggedIn.")
            return redirect("clioncare:costpage")
        else:
            messages.error(request,"Error: Invalid username or password, please retry")
            return render(request,"clioncare/login.html")
    else:
        return render(request, "clioncare/login.html")

def userlogout(request):
    if request.method =="GET":
        logout(request)
        messages.info(request, "Successfully logged out.")
        return redirect("clioncare:costpage")
