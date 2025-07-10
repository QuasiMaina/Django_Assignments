from .models import FoodItem
from django.shortcuts import render, redirect
from django.utils import timezone

def index(request):
    today = timezone.now().date()
    food_items = FoodItem.objects.filter(date_added=today)
    total_calories = sum(item.calories for item in food_items)

    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        if name and calories.isdigit():
            FoodItem.objects.create(name=name, calories=int(calories), date_added=today)
        return redirect('home')

    return render(request, 'calorie_tracker/index.html', {
        'food_items': food_items,
        'total_calories': total_calories,
    })

# Function to delete a food item

def delete_food(request, item_id):
    FoodItem.objects.filter(id=item_id).delete()
    return redirect('home')

# Function to reset the day's food items
def reset_day(request):
    today = timezone.now().date()
    FoodItem.objects.filter(date_added=today).delete()
    return redirect('home')
