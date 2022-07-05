from django.shortcuts import render, redirect
from .models import Garden, Flower, FlowerCategory, Video, Reminder, Question, Answer
from .forms import GardenForm, FlowerForm


# Create your views here.
def garden(request):
    context = {"garden": Garden.objects.filter(user=request.user)}
    return render(request, "garden.html", context=context)


def gardenForm(request):
    if request.method == "POST":
        form = GardenForm(request.POST)
        if form.is_valid():
            garden = form.save(commit=False)
            garden.user = request.user
            garden.save()
            return redirect("garden")
    context = {"form": GardenForm}
    return render(request, "gardenForm.html", context=context)


def flowerForm(request):
    if request.method == "POST":
        form = FlowerForm(request.POST)
        if form.is_valid():
            flower = form.save(commit=False)
            flower.save()
            return redirect("home")

    context = {"form": FlowerForm}
    return render(request, "addFlower.html", context=context)


def home(request):
    context = {"category": FlowerCategory.objects.all(), "flower": Flower.objects.all()}
    return render(request, "home.html", context=context)


def gardenInfo(request):
    context = {"garden": Garden.objects.filter(user=request.user).all(),
               "flowers": Flower.objects.filter(garden__user=request.user)}
    return render(request, "garden-info.html", context=context)


def video(request):
    context = {"videos": Video.objects.all()}
    return render(request, "video.html", context=context)


def reminder(request):
    context = {"reminder": Reminder.objects.filter(garden__user=request.user).all()}
    return render(request, "reminder.html", context=context)


def forum(request):
    context = {"questions": Question.objects.all(), "answer": Answer.objects.all()}
    return render(request, "forum.html", context=context)

