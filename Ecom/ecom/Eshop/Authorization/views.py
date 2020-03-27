from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
# for signup
def signup(request):
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'templates/shoper/home.html')
    return render(request,'templates/Authorization/signup.html',{'form':form})
