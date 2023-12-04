from django.shortcuts import render, get_object_or_404
from .forms import FormClass

# Create your views here.

def home_view(request):
    return render(request, 'home_view.html', context={})

def generate_view(request):
    form = FormClass(request.POST or None)
    if form.is_valid():
        new_name = form.cleaned_data.get('name')
        context = {
            'form': form,
            'word_from_view': new_name,
            'created': True,
        }
    else:
        context = {
            'form': form,
            'created': False,
        }
    return render(request, 'generate.html', context=context)

def about_view(request):
    return render(request, 'about_view.html', context={})