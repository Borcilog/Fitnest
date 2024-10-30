from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Post, Video, Contact
from .forms import VideoForm, ContactForm
from django.urls import reverse_lazy

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
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_create.html'

class BlogUpdateView(UpdateView):
    model = Post
    fields = ['title', 'author', 'body']
    template_name = 'app/blog_update.html'

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'app/blog_delete.html'
    success_url = reverse_lazy('body')
class VideoListView(ListView):
    model = Video
    template_name = 'app/video_list.html'
    context_object_name = 'Videos'

class VideoUploadView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'app/Video.html'
    success_url = reverse_lazy('Video_list')

class ContactPageView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'app/contact.html'
    success_url = reverse_lazy('home')
