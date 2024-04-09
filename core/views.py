from django.shortcuts import render,redirect
from .models import *
# Create your views here.

def recipes(request):
    try:
        if request.method == 'POST':
            recipe_name = request.POST.get("recipe_name")
            recipe_desc = request.POST.get("recipe_desc")
            recipe_image = request.FILES.get("recipe_image")
            data = Recipe.objects.create(recipe_name=recipe_name,recipe_desc=recipe_desc,recipe_image=recipe_image)
            data.save()
            return redirect('/')
    except:
        pass
    quesryset= Recipe.objects.all()
    context = {
        'title':"Recipe",
        'data':quesryset
    }

    return render(request,"core/index.html",context)

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