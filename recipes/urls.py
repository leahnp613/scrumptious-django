from django.urls import path
from recipes.views import recipe_list, show_recipe, create_recipe, edit_recipe

app_name = "recipes"
urlpatterns = [
    path("recipes/<int:id>/", show_recipe, name="show_recipe"),
    path("recipes/", recipe_list, name="list_recipe"),
    path("recipes/create/", create_recipe, name = "create_recipe"),
    path("recipes/<int:pk>/edit", edit_recipe, name = "edit_recipe"),
]