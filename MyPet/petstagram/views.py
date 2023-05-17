from django.shortcuts import render, redirect
from .models import Profile, Feed
from .forms import FeedForm

# Create your views here.

def dashboard(request):
    form = FeedForm(request.POST or None)
    profiles = Profile.objects.exclude(user=request.user)

    if request.method == "POST":
        
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("petstagram:dashboard")
        

    followed_feeds = Feed.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by("-created_at")

    return render(request, "petstagram/mainpage.html", {"form": form, "feeds": followed_feeds, "profiles": profiles})


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    return render(request, "petstagram/profile_list.html", {"profiles": profiles})

def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()


    profile = Profile.objects.get(pk=pk)
    if request.method == "POST":
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == "follow":
            current_user_profile.follows.add(profile)
        elif action == "unfollow":
            current_user_profile.follows.remove(profile)
        current_user_profile.save()

    return render(request, "petstagram/feedprofile.html", {"profile": profile})


def uploadPage(request):
    profiles = Profile.objects.exclude(user=request.user)
    form = FeedForm(request.POST or None)
    if request.method == "POST":
        
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("petstagram:dashboard")
    return render(request, "petstagram/uploadPage.html", {"form": form,"profiles": profiles})