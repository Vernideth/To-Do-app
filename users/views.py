from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def register(request):
    if request.method=='post':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    form = UserCreationForm()
    return render (request, 'register.html',{'form':form})
