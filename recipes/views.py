from django.shortcuts import render

# Create your views here.
def show_recipe(request):
    return render(render, "recipes/detail.html")