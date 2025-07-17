from django.http import JsonResponse
from django.shortcuts import redirect, render
from gamehubapp.models import users

# Create your views here.
def homepage(request):
    return render(request,"login.html")
def dashboard(request):
    return render(request,'dashboard.html')
def registerpage(request):
    return render(request,'register.html')
def registerpagepost(request):
    username = request.POST['username']
    print("username",username)
    
        
    if users.objects.filter(username = username ).exists():
        return render(request,'register.html',{'message':'Username already exist'})
    else:
        password = request.POST['password1']
        
        obj = users()
        obj.username = username
        obj.password = password
        obj.snakescore= 0
        obj.stonescore = 0
        obj.quizscore = 0
        obj.tictactoescore = 0
        obj.save()
        request.session['login_user'] = username
        return redirect('/dashboard')
def loginpost(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        usr = users.objects.get(username = username)
        if usr.password == password:
            request.session['login_user'] = username
            return redirect('/dashboard')
        else:
            return render(request,'login.html',{'message':'Incorrect Password'})
    except Exception:
        return render(request,'login.html',{'message':'Invalid User'})

def quizapp(request):
    return render(request,'quizapp.html')

def displayquestions(request):
    data = {
        'question': 'What is the capital of France?',
        'a':'Paris',
        'b':'Berlin',
        'c':'Delhi',
        'd':'London'
    }
    return JsonResponse(data)
    