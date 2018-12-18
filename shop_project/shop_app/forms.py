from django import forms 
from shop_app.models import Comment, Question, Response

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['username', 'text']
		widgets = {
		'username': forms.TextInput(attrs={
			'id':'comment-username',
			'placeholder':'username',
			'required': True
			}),
		'text': forms.Textarea(attrs={
			'id':'comment-text',
			'placeholder':'Ecrivez un commentaire...',
			'required': True
			})
		}

class QuestionForm(forms.ModelForm):
	class Meta:
		model = Question
		fields = ['title', 'username', 'text']
		widgets = {
		'username': forms.TextInput(attrs={
			'id':'comment-username',
			'placeholder':'username',
			'required': True
			}),
		'title': forms.TextInput(attrs={
			'id':'comment-title',
			'placeholder':'title',
			'required': True
			}),
		'text': forms.Textarea(attrs={
			'id':'comment-text',
			'placeholder':'text',
			'required': True
			})
		}

class ResponseForm(forms.ModelForm):
	class Meta:
		model = Response
		fields = ['username', 'text']
		widgets = {
		'username': forms.TextInput(attrs={
			'id':'comment-username',
			'placeholder':'username',
			'required': True
			}),
		'text': forms.Textarea(attrs={
			'id':'comment-text',
			'placeholder':'text',
			'required': True
			})
		}