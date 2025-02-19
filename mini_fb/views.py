# mini_fb/views.py

from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Profile

# Create your views here.
class ShowAllProfilesView(ListView):
    '''Define a view class to show all Profiles'''

    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

class ShowProfilePageView(DetailView):
    '''Display a single profile.'''

    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'