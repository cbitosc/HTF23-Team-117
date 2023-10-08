from django.shortcuts import render,redirect
from mental.forms import cred_form
from mental.models import cred_model,emotion
# Create your views here.
def default(request):
    return render(request,'home.html')

def login(request):
    if request.method=="POST":
        form=cred_form(request.POST)
        if form.is_valid:
            try:
                form.save()
                return render(request,'reg_success.html')
            except:
                pass

    return render(request,'login.html')

def check_cred(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        try:
            user = cred_model.objects.get(email=email, password=password)    
            # Successful login, you can redirect the user to a dashboard or any other page
            return render(request,'dashboard.html',{'name':user.name})  # Replace 'dashboard' with your actual URL name
            
        except cred_model.DoesNotExist:
            # Handle unsuccessful login (credentials don't match)
            error_message = "Invalid email or password. Please try again."
            return render(request, 'login_fail.html')
    
    return render(request, 'login.html')

def books(request):
    return render(request,'books.html')

def dashboard(request):
    return render(request,'dashboard.html')

def music(request):
    return render(request,'music.html')

def pop(request):
    return render(request,'pop.html')

def christmas(request):
    return render(request,'christmas.html')
##
def disney(request):
    return render(request,'disney.html')

def sour(request):
    return render(request,'sour.html')

def bollywood(request):
    return render(request,'bollywood.html')

def radio(request):
    return render(request,'radio.html')

def worship(request):
    return render(request,'worship.html')

def meditation(request):
    return render(request,'meditation.html')

def exercise(request):
    return render(request,'exercise.html')

def mydiary(request):
    return render(request,'mydiary.html')

def activity(request):
    return render(request,'quiz1.html')

def home(request):
    return render(request,'dashboard.html')

def logout(request):
    return render(request,'login.html')

def feedback(request):
    return render(request,'feedback.html')

def report(request):
    data=emotion.objects.all()
    return render(request,'daily_report.html',{'data':data})