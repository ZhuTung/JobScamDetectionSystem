from django.shortcuts import render, redirect
from .models import UserAccount

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        if UserAccount.objects.filter(username=username).exists() != True or UserAccount.objects.filter(password=password).exists() != True:
            error_msg = "User account did not exist!"
            return render(request, 'accounts/login.html', {"error_msg":error_msg})
        
        if UserAccount.objects.filter(username=username).exists() and UserAccount.objects.filter(password=password).exists():
            username = UserAccount.objects.get(username = username)
            password = UserAccount.objects.get(password = password)
            print(username.id, password.id)
            if username.id == password.id:
                request.session['stud_id'] = username.id
                return redirect('accounts:home')
            else:
                error_msg = "Incorrect username or password!"
                return render(request, 'accounts/login.html', {"error_msg":error_msg})
    
    return render(request, 'accounts/login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = int(request.POST['age'])
        username = request.POST['username']
        password = request.POST['password']

        print(name, age, username, password)
        print(type(age))

        if len(password) < 8:
            error_msg = "Password must be more than 8 characters!"
        elif age == 0 or age > 100:
            error_msg = "Invalid age!"
        elif UserAccount.objects.filter(username=username).exists():
            error_msg = "Username has been taken!"
        elif UserAccount.objects.filter(password=password).exists():
            error_msg = "Password has been taken!"
        else:
            user_acc = UserAccount.objects.create(name=name, age=age, username=username, password=password)
            user_acc.save()
            return redirect('accounts:login')

        return render(request, 'accounts/register.html', {"error_msg":error_msg}) 

    return render(request, 'accounts/register.html')

def home(request):
    user_id = request.session['stud_id']
    user = UserAccount.objects.get(pk=user_id)
    return render(request, 'accounts/home.html',{'user':user})