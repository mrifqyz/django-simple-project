from django.shortcuts import render, redirect, render, reverse
from .forms import StatusForm
from .models import Status

# Create your views here
def landing(request):
    form = StatusForm()
    i = Status.objects.all().count()
    if(i==0):
        obj = "No status yet."
    else:
        obj = Status.objects.filter(id=i)[0]
    var = {
        'status_data':Status.objects.all(),
        'status_obj':i,
        'latest':obj,
        'form':form
    }
    return render(request, 'landing.html', var)

def create_status(request):
    form = StatusForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            if len(request.POST['status']) < 300:
                Status.objects.create(status=request.POST['status'])
    return redirect(reverse('landing'))
