from django import forms 
from contact_app.models import Contact

class ContactForm(forms.ModelForm):
	class Meta:
		model = Contact
		fields = ['subject', 'email', 'text']
		widgets = {
		'subject': forms.TextInput(attrs={
			'id':'comment-subject',
			'placeholder':'Subject',
			'required': True
			}),
		'email': forms.EmailInput(attrs={
			'id':'comment-email',
			'placeholder':'Email',
			'required': True
			}),		
		'text': forms.Textarea(attrs={
			'id':'comment-text',
			'placeholder':'Text',
			'required': True
			})
		}
		