# views.py
import random
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.db.models import Count, Q

from .models import Problem, SeenProblems
from .forms import TagForm, RatingRangeForm

def home(request):
    form = RatingRangeForm(request.GET or None)
    return render(request, "home.html", {"form": form})

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Account created! Please log in.")
            return redirect("login")
    else:
        form = UserCreationForm()
    
    return render(request, "register.html", {"form": form})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect("home")

def random_problem(request):
    rating_form = RatingRangeForm(request.GET or None)
    tag_form = TagForm(request.GET or None)
    
    problems = Problem.objects.all()
    
    if rating_form.is_valid():
        min_rating = rating_form.cleaned_data.get("min_rating")
        max_rating = rating_form.cleaned_data.get("max_rating")
        
        if min_rating:
            problems = problems.filter(rating__gte=min_rating)
        if max_rating:
            problems = problems.filter(rating__lte=max_rating)
    
    if tag_form.is_valid():
        selected_tag = tag_form.cleaned_data.get("tag")
        if selected_tag:
            problems = problems.filter(tag=selected_tag)
    
    if problems.exists():
        count = problems.count()
        random_index = random.randint(0, count - 1)
        problem = problems[random_index]
        
        if request.user.is_authenticated:
            SeenProblems.objects.get_or_create(user=request.user, problem=problem)
    else:
        problem = None
        messages.warning(request, "No problems found with the selected criteria.")

    return render(request, "random_problem.html", {
        "problem": problem,
        "tag_form": tag_form,
        "rating_form": rating_form,
    })

@login_required
def seen_problems(request):
    seen = SeenProblems.objects.filter(user=request.user).select_related("problem")
    return render(request, "seen_problems.html", {"seen_problems": seen})