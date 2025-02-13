# formdata/views.py

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show_form(request):
    '''Show the form to the user'''

    template_name = 'formdata/form.html'
    return render(request, template_name)

def submit(request):
    '''Process the form submition and generate a result.'''

    template_name = 'formdata/confirmation.html'

    if request.POST:
        name = request.POST['name']
        favorite_color = request.POST['favorite_color']

        context = {
            'name' : name,
            'favorite_color' : favorite_color,
        }

    return render(request, template_name, context)