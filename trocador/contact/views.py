from django.shortcuts import render

# Create your views here.
from .forms import Contact

def message(request):

	
	template_name = 'contact/contact.html'
	context = {}
	if request.method == 'POST':
		form = Contact(request.POST)
		if form.is_valid():
			context['is_valid'] = True
			form.send_mail()
			form = Contact()

	else:
		form = Contact()


	context['form'] = form
	
	return render(request, template_name, context)
