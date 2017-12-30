from django.shortcuts import render, get_object_or_404

# Create your views here.

def home(request):
	return render(request, 'home.html') 

def servicos(request):
	return render(request, 'servicos.html')	

def speaker_detail(request, slug):

    speaker = get_object_or_404(Speaker, slug=slug)
    return render(request, 'base.html', {'speaker':speaker})