from django.shortcuts import render, redirect
from . models import tweet
from . forms import TweetForm, CustomRegistrationForm
from django.shortcuts import get_object_or_404 ,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

#create your views here

def index(request):
    return render (request,'index.html')

def tweet_list(request):
    tweets=tweet.objects.all().order_by('-created_at')
    return render(request,'tweet_list.html',{'tweets':tweets})

def tweet_detail(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, pk=tweet_id)
    return render(request, 'tweet_detail.html', {'tweet': tweet_obj})

@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm()
    return render(request, 'tweet_from.html', {'form': form})

@login_required
def tweet_edit(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        form = TweetForm(request.POST, request.FILES, instance=tweet_obj)
        if form.is_valid():
            tweet_obj = form.save(commit=False)
            tweet_obj.user = request.user
            tweet_obj.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet_obj)
    return render(request, 'tweet_form.html', {'form': form})


@login_required
def tweet_delete(request, tweet_id):
    tweet_obj = get_object_or_404(tweet, pk=tweet_id, user=request.user)
    if request.method == 'POST':
        tweet_obj.delete()
        return redirect('tweet_list')
    return render(request, 'tweet_confirm_delete.html', {'tweet': tweet_obj})




def register(request):
    if request.method == 'POST':
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = CustomRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})
    