from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def recipes(request):
    if request.method == 'POST':
        try:
            recipe_name = request.POST.get("recipe_name")
            recipe_desc = request.POST.get("recipe_desc")
            recipe_image = request.FILES.get("recipe_image")
            Recipe.objects.create(recipe_name=recipe_name, recipe_desc=recipe_desc, recipe_image=recipe_image)
            return redirect('/')
        except (ValueError, TypeError) as e:
            # Handle specific exceptions if needed
            print(e)  # Log the error or handle it appropriately

    queryset = Recipe.objects.all()

    search_query = request.GET.get("search")
    if search_query:
        queryset = queryset.filter(recipe_name__icontains=search_query).distinct()

    context = {
        'title': "Recipe",
        'data': queryset
    }

    return render(request, "core/index.html", context)
def delete_recipe(request,id):
    data = Recipe.objects.get(id=id)
    data.delete()
    return redirect('/')


def update_recipe(request, id):
    data = Recipe.objects.get(id=id)
    context = {
        'title': "Recipe",
        'data': data
    }
    
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        recipe_desc = request.POST.get("recipe_desc")
        recipe_image = request.FILES.get("recipe_image")  # Use request.FILES for file uploads
        
        data.recipe_name = recipe_name
        data.recipe_desc = recipe_desc
        
        if recipe_image:
            data.recipe_image = recipe_image
        
        data.save()
        return redirect('/')
    
    return render(request, "core/update_recipe.html", context)