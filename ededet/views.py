from django.shortcuts import render
from .forms import StatusForm
from .models import Status

# Create your views here
def landing(request):
    form = StatusForm()
    var = {
        'status_data':Status.objects.all(),
        'form':form
    }
    return render(request, 'landing.html', var)
