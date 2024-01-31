from django.db.models import F
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from .models import Product, Recipe, RecipeProduct


def add_product_to_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')
        product_id = request.GET.get('product_id')
        weight = request.GET.get('weight')

        # Проверяем существование объектов рецепта и продукта
        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            product = Product.objects.get(pk=product_id)
            # Обновляем или создаем запись о продукте в рецепте
            recipe_product, created = RecipeProduct.objects.update_or_create(
                recipe=recipe,
                product=product,
                defaults={'weight': weight}
            )
        except (Recipe.DoesNotExist, Product.DoesNotExist):
            return HttpResponse("Ошибка: рецепт или продукт не найден")

        if created:
            return HttpResponse("Продукт успешно добавлен в рецепт.")
        else:
            return HttpResponse("Продукт обновлен.")


def cook_recipe(request):
    if request.method == 'GET':
        recipe_id = request.GET.get('recipe_id')

        try:
            recipe = Recipe.objects.get(pk=recipe_id)
            recipe_products = recipe.recipeproduct_set.all()

            for recipe_product in recipe_products:
                Product.objects.filter(pk=recipe_product.product_id).update(times_cooked=F('times_cooked') + 1)  # атомарная операции, устраняя проблему race condition.
        except Recipe.DoesNotExist:
            return HttpResponse("Ошибка: рецепт не найден")

        return HttpResponse("Рецепт приготовлен успешно + 1 к продуктам в нем.")


def show_recipes_without_product(request):
    if request.method == 'GET':
        product_id = request.GET.get('product_id')
        try:
            product = Product.objects.get(pk=product_id)

            # Поиск всех рецептов, где нет указанного продукта
            recipes_without_product = Recipe.objects.exclude(recipeproduct__product=product)

            # Поиск всех рецептов, где для указанного продукта вес меньше 10
            recipes_with_product_lt_10 = Recipe.objects.filter(
                recipeproduct__product=product, recipeproduct__weight__lt=10
            )

            recipes = recipes_without_product.union(recipes_with_product_lt_10)

            # print(recipes.query)
            return render(request, 'recipes/recipes_without_product.html', {'recipes': recipes})
        except Product.DoesNotExist:
            return HttpResponse("Ошибка: продукт не найден")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')