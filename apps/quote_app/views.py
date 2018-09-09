from django.shortcuts import render, redirect
from . import views
from .models import User, UserManager, Like, Quote
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def home(request):
    quotes = Quote.objects.all()
    this_quote = Quote.objects.filter()
    this_user = User.objects.get(id=request.session['user_id'])
    likes = Like.objects.count()
    # like = Like.objects.create(
    #     user = this_user,
    # )
    return render(request,'home.html',{
        'quotes': quotes,
        'likes':likes
    })

def user(request, id):
    this_user = User.objects.get(id=id)
    user_qs = Quote.objects.filter(user=this_user.id)
    return render(request,'user.html',{
        'quotes':user_qs
    })

def edit(request, id):
    return render(request,'edit.html')

def editUser(request, id):
    # result = User.objects.editValidator(request.POST)
    # if type(result) == dict:
    #     for key, value in result.items():
    #             messages.error(request, value)
    #     return redirect('/edit/{}'.format(id))
    # else:
    this_user = User.objects.get(id=request.session['user_id'])
    this_user.first_name = request.POST['first']
    this_user.last_name = request.POST['last']
    this_user.email = request.POST['email']
    this_user.save()
    request.session['user_first']=this_user.first_name
    request.session['user_last']=this_user.last_name
    request.session['user_email']=this_user.email
    return redirect('/home')


def process(request):
    if request.POST['reg'] == 'new':
        result = User.objects.userValidator(request.POST)
        # print("LOOOOOOK",type(errors))
        # print("LOOK AT ALL OF THESE ERRORS",errors)
        if type(result) == dict:
            for key, value in result.items():
                messages.error(request, value)
            return redirect('/')
        else:
            # print(result.id)
            request.session['user_id'] = result.id
            request.session['user_first'] = result.first_name
            request.session['user_last'] = result.last_name
            request.session['email'] = result.email
            # print(request.session['user_name'])
            return redirect('/home')

    if request.POST['reg'] == 'login':
        result = User.objects.userValidator(request.POST)
        if type(result) == str:
            messages.error(request,result)
            return redirect('/')
        else:
            request.session['user_id'] = result.id 
            request.session['user_first'] = result.first_name
            request.session['user_last'] = result.last_name
            request.session['email'] = result.email
            print(request.session['user_id'])
            return redirect('/home')

def addQuote(request):
    result = User.objects.quoteValidator(request.POST)
    if type(result) == dict:
        for key, value in result.items():
                messages.error(request, value)
        return redirect('/home')
    if type(result) != dict:
        quoted = Quote.objects.create(
            author = request.POST['author'],
            quote = request.POST['quote'],
            user = User.objects.get(id=request.session['user_id'])
        )
        return redirect('/home')

def delete(request, id):
    this_quote = Quote.objects.get(id=id)
    this_quote.delete()
    return redirect('/home')

def like(request, id):
    this_user = User.objects.get(id=id)
    this_quote = Quote.objects.get(id=request.POST['like'])
    likey = Like.objects.create(
        user=this_user,
        quote=this_quote
    )
    return redirect('/home')


def logout(request):
    request.session.clear()
    return redirect('/')