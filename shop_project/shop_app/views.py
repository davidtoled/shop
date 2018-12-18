from django.shortcuts import render, redirect
from shop_app.models import Product, Client, Comment, Question, Response
from shop_app.forms import CommentForm, QuestionForm, ResponseForm
import datetime


def index(request):
	products = Product.objects.all()[:10]
	return render(request, 'index.html', context={ 'products': products })


def product(request, product_id):
  product = Product.objects.get(id=product_id)
  comments = Comment.objects.all().filter(product_id=product_id)
  questions = Question.objects.all().filter(product_id=product_id)

  questions_with_responses = []
  for question in questions:
    question_with_responses = {
      'question': question,
      'responses': Response.objects.all().filter(question_id=question.id)
    }

    questions_with_responses.append(question_with_responses)

  return render(request, 'product.html', context={
      'product': product,
      'comments': comments,
      'questions': questions_with_responses,
    })

def clients(request):
	clients = Client.objects.all()[:10]
	return render(request, 'clients.html', context={ 'clients': clients })


def client(request, client_id):
	client = Client.objects.get(id=client_id)
	return render(request, 'client.html', context={ 'client': client })


def comments(request):
	comments = Comment.objects.all()
	return render(request, 'comments.html', context={ 'comments': comments })


def comment(request, comment_id):
	comment = Comment.objects.get(id=comment_id)
	return render(request, 'comment.html', context={ 'comment': comment })


def comment_form(request, product_id):
	if request.method == 'POST':
		username = request.POST.get('username')
		text = request.POST.get('text')
		product = Product.objects.get(id=product_id)
		date = datetime.datetime.now()	
		Comment.objects.get_or_create(username=username, text=text, product=product, date=date)[0]


	return render(request, 'comment_form.html', context={ 'comment_form': CommentForm() })


def maillots(request):
	maillots = Maillot.objects.all()
	return render(request, 'maillots.html', context={ 'maillots': maillots })


def maillot(request, maillot_id):
	maillot = Maillot.objects.get(id=maillot_id)
	return render(request, 'maillot.html', context={ 'maillot': maillot })


def question_form(request, product_id):
	if request.method=='POST':
		Question.objects.get_or_create(username=request.POST.get('username'),title=request.POST.get('title'),product=Product.objects.get(id=product_id),text=request.POST.get('text'))
		return redirect('/shop_app/products/{}'.format(product_id))
	
	return render(request,'question_form.html', context= { 'question_form': QuestionForm() })

   
def response_form(request, question_id):
	if request.method=='POST':
		question = Question.objects.get(id=question_id)
		Response.objects.get_or_create(username=request.POST.get('username'),text=request.POST.get('text'),question=question)
		return redirect('/shop_app/products/{}'.format(question.product.id))

	return render(request,'response_form.html', context= { 'response_form': ResponseForm() })
