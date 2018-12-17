from django.shortcuts import render , redirect
from contact_app.models import Contact
from contact_app.forms import ContactForm

# Create your views here.
def contact(request):
	if request.method=='POST':
		Contact.objects.get_or_create(subject=request.POST.get('subject'),email = request.POST.get('email'),text = request.POST.get('text'))
		return redirect('contact_succes/')
	
	return render(request,'contact.html', context= { 'contact_form': ContactForm() })

    

def contact_succes(request):
    return render(request,'contact_succes.html')