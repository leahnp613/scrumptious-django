from django.urls import path
from recipes.views import recipe_list, show_recipe


urlpatterns = [
    path("recipes/<int:id>/", show_recipe),\
    path("recipes/<int:id>", recipe_list)
]