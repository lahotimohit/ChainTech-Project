from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    current_time = datetime.now()
    return render(request, 'myapp/index.html', context={'time': current_time})