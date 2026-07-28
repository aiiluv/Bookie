from django.shortcuts import render, redirect
from .forms import FeedbackForm

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FeedbackForm()

        return render(request, 'home/index.html', {
            'form' : form
        })