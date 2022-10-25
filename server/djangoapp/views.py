from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page

def about(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/about.html', context)


# Create a `contact` view to return a static contact page

def contact_us(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/contact_us.html', context)

# Create a `login_request` view to handle sign in request
def login_request(request):
    context = {}
    if request.method == "POST":
        # Get username and password
        username = request.POST['username']
        password = request.POST['psw']
        # Try to check if credentials is correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # If user is valid then call methon
            login(request, user)
            return redirect('djangoapp:index')
        else:
            # If not, return to the default page
            return render(request, 'djangoapp/index.html', context)
    else:
        return render(request, 'djangoapp/index.html', context)

# Create a `logout_request` view to handle sign out request
def logout_request(request):
    print("Log out `{}`".format(request.user.username))
    # Current Logout Request
    logout(request)
    # Redirects the User
    return redirect('djangoapp:index')

# Create a `registration_request` view to handle sign up request
def registration_request(request):
    context = {}
    if request.method == 'GET':
        return render(request, 'djangoapp/registration.html', context)
    elif request.method == 'POST':
        # <HINT> Get user information from request.POST
        # <HINT> username, first_name, last_name, password
        username = request.POST['username']
        password = request.POST['psw']
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        user_exist = False
        try:
            # Checks if the user already exists
            User.objects.get(username=username)
            user_exist = True
        except:
            # If not it logs it
            logger.debug("{} is new brand new user".format(username))
        # 
        if not user_exist:
            # Creates the User
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name,
                                            password=password)
            login(request,user)
            # Back to the original page
            return redirect("djangoapp:index")
        else:
            return render(request, 'djangoapp/index.html', context)


# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        url = "URL"
        # Get dealers from the URL
        dealer_list = get_dealers_from_cf(url)
        #dealer_names = ' '.join([dealer.short_name for dealer in context])
        # Return a list of dealer short name
        #print(dealer_list[0].address)
        return render(request, 'djangoapp/index.html', {'dealership_list': dealer_list})
        #return HttpResponse(dealer_names)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

