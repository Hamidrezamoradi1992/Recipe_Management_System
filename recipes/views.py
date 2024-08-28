import json

from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponse
import json
from recipes.models import Recipe


# Import Recipe model and RecipeForm here

def recipe_list(request):
    # Retrieve and display all recipes
    if request.method == "POST":
        recipes = Recipe.objects.all()
        jason = [dict(title=recipe.title, description=recipe.description, id=recipe.pk) for recipe in recipes]
        print(jason)
        return JsonResponse(jason, safe=False,status=200)
    return render(request, 'home.html')


def recipe_create(request):
    # Handle recipe creation with AJAX
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        print('title', title)
        print('description', description)
        Recipe.objects.create(title=title, description=description)
        return JsonResponse(data={'title': title, 'description': description}, status=200)
    return JsonResponse(data={}, status=200)


def recipe_update(request, pk):  # OPTIONAL
    # Handle recipe update with AJAX
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')
        if len(title) != 0:
            recipe.title = title
        recipe.description = description
        recipe.save()
        return JsonResponse({}, status=200)
    jason = [dict(title=recipe.title, description=recipe.description, id=recipe.pk)]
    print(jason)
    return JsonResponse(jason,safe=False, status=200)


def recipe_delete(request, pk):  # OPTIONAL
    # Handle recipe deletion with AJAX
    recipe = get_object_or_404(Recipe, pk=pk)
    print('pk', pk)
    print(recipe)
    recipe.delete()
    return JsonResponse(data={}, status=200)


def recipe_view(request, pk):  # OPTIONAL
    # Handle recipe deletion with AJAX

    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'view.html', {'recipe': recipe})
