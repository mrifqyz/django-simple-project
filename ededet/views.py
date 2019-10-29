from django.shortcuts import render, redirect
from .forms import StatusForm
from .models import Status

# Create your views here
def landing(request):

    if request.method == "POST":
        form = StatusForm(request.POST)
        
        if form.is_valid() == True:
            Status.objects.create(status=request.POST['status'])
            redirect("/")

    form = StatusForm()
    var = {
        'status_data':Status.objects.all(),
        'form':form
    }
    return render(request, 'landing.html', var)
