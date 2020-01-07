from django.shortcuts import render
from django.views.generic import ListView
from .models import Profile
# Create your views here.


class ProfileListView(ListView):
    ListView.model  = Profile
    ListView.template_name = 'profile/profile_list.html'
    ListView.context_object_name = 'profile_list'