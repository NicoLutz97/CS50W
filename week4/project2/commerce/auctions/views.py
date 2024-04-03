from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import User, Listing
from .all_forms import Form_New_Listing, Form_Whishlist


def index(request):
    return render(request, "auctions/index.html", {
        "listings": Listing.objects.all(),
    })


def add(request):
    if request.method == "POST":
        form = Form_New_Listing(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            starting_bid = form.cleaned_data["starting_bid"]
            image = form.cleaned_data["image"]
            category = form.cleaned_data["category"]
            current_price = starting_bid

            new_listing = Listing(title=title, description=description, starting_bid=starting_bid, image=image, category=category, current_price=current_price)
            new_listing.save()

            return HttpResponseRedirect(reverse("index"))
                    
    form = Form_New_Listing()
    return render(request, "auctions/add.html", {
        "form": form
    })


@login_required
def listing(request, id):
    try:
        l = Listing.objects.get(id=id)
    except Listing.DoesNotExist:
        l = None

    if request.method == "POST":
        form = Form_Whishlist(request.POST)
        if form.is_valid():
            l_id = form.cleaned_data["listing_id"]
            user = request.user

            is_marked= l in user.whishlist.all()

            if not is_marked:
                listing = Listing.objects.get(id=l_id)
                user.whishlist.add(listing)
            else:
                listing = Listing.objects.get(id=l_id)
                user.whishlist.remove(listing)
            
            return redirect("listing", id=l_id)
    
    form = Form_Whishlist(initial={"listing_id": id})

    return render(request, "auctions/listing.html", {
        "listing": l,
        "form": form
    })
    

@login_required
def whishlist(request):
    return render(request, "auctions/whishlist.html", {
        "whishlist": request.user.whishlist.all() 
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
