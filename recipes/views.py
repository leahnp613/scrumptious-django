from django.shortcuts import render, get_object_or_404, redirect
from recipes.forms import RecipeForm
from recipes.models import Recipe 

# Create your views here.
def show_recipe(request, id):
    recipe = get_object_or_404(Recipe, id =id)
    context = {
        "recipe" :recipe,
    }
    return render(request, "recipes/detail.html", context)


def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {
        "recipe_list":recipes,
    }
    return render(request, "recipes/list.html", context)


def create_recipe(request):
    if request.method == "POST":
        form = RecipeForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_recipe")
    else:
        form = RecipeForm()

    context ={
        "form":form,
    }

    return render(request, "recipes/create.html", context)

def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, id=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            return redirect("show_recipe", id=pk)

    else:
        form = RecipeForm(instance=recipe)

    context ={
        "recipe":recipe,
        "recipe_form": form,
    }
    return render(request, "recipes/edit.html", context)