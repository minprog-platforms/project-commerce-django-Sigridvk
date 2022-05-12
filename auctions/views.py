from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse
from django import forms
from .models import User, Listing, Bid


def index(request):
    return render(request, "auctions/index.html", {
        "listings" : Listing.objects.all()
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def new_listing(request):
    return render(request, "auctions/new.html")

def listing_view(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    biddings = Bid.objects.filter(listing = listing)
    min_price = listing.starting_bid + 1
    return render(request, "auctions/listing.html", {
        "listing":listing,
        "biddings":biddings,
        "min_price":min_price
    })

class NewBidForm(forms.Form):
    bid = forms.IntegerField(label="New Bid")

class NewListingForm(forms.Form):
    title = forms.CharField(label="Title", max_length=64, required=True)
    description = forms.CharField(widget=forms.Textarea())
    starting_bid = forms.IntegerField(min_value=0)
    category = forms.CharField(max_length=64)
    image_url = forms.URLField(max_length=1000)

def new(request):
    # Check if method is POST
    if request.method == "POST":
        form = NewListingForm(request.POST)

        # Check if form data is valid (server-side)
        if form.is_valid():

            # Isolate the task from the 'cleaned' version of form data
            title = form.cleaned_data['title']
            description = form.cleaned_data['description']
            starting_bid = form.cleaned_data['starting_bid']
            category = form.cleaned_data['category']
            image_url = form.cleaned_data['image_url']

            l = Listing(title=title, description=description, starting_bid=starting_bid, category=category, image_url=image_url, owner = request.user)
            l.save()
            
            
            # Redirect user to list of tasks
            return render(request, "auctions/listing.html", {
                "listing": l})

        else:
            # If the form is invalid, re-render the page with existing information.
            return render(request, "auctions/new.html", {
                "form": form
            })
    return render(request, "auctions/new.html", {
        "form":NewListingForm()
    })

# def bid(request):
#     # Check if method is POST
#     if request.method == "POST":
#         form = NewBidForm(request.POST)

#         # Check if form data is valid (server-side)
#         if form.is_valid():

#             # Isolate the task from the 'cleaned' version of form data
#             title = form.cleaned_data['title']
      


#             l = Listing(title=title, description=description, starting_bid=starting_bid, category=category, image_url=image_url, owner = request.user)
#             l.save()
            
            
#             # Redirect user to list of tasks
#             return render(request, "auctions/listing.html", {
#                 "listing": l})

#         else:
#             # If the form is invalid, re-render the page with existing information.
#             return render(request, "auctions/new.html", {
#                 "form": form
#             })
#     return render(request, "auctions/new.html", {
#         "form":NewListingForm()
#     })