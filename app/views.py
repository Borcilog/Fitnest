from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Video, Contact
from .forms import VideoForm, ContactForm, CreateUserForm
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def RegisterPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, ' Account Has Been Created for ' + user)

            return redirect('login')

    context = {'form': form }
    return render(request, 'app/register.html', context)

def LoginPage(request):
    
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            messages.info(request, 'Username or Password is Incorrect')
            
        context = {}
        return render(request, 'app/login.html', context)

def LogoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')

class HomePageView(TemplateView):
    template_name = 'app/home.html'

class AboutPageView(TemplateView):
    template_name = 'app/about.html'


class BlogListView(ListView):
    model = Post
    context_object_name = 'posts'
    template_name = 'app/blog_list.html'

class BlogDetailView(DetailView):
    model = Post
    context_object_name = 'post'
    template_name = 'app/blog_detail.html'

class BlogCreateView(CreateView):
    model = Post
    fields = ['title', 'author', 'body', 'header_image']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body', 'header_image']
    template_name = 'app/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('body')

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'app/Video_list.html', {'videos': videos})

def upload_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')  # Adjust to the URL name of your video list page
    else:
        form = VideoForm()
    return render(request, 'app/Video.html', {'form': form})

class ContactPageView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'app/contact.html'
    success_url = reverse_lazy('home')
