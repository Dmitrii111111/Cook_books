from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название продукта")
    times_cooked = models.IntegerField(default=0, verbose_name="Использование продукта")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Recipe(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название рецепта")
    products = models.ManyToManyField(Product, through='RecipeProduct', verbose_name="Продукты в рецепте") #  связываем несколько продуктов с одним рецептом

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'


class RecipeProduct(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, verbose_name="Название рецепта") # внешний ключ
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Название продукта") # внешний ключ
    weight = models.IntegerField(verbose_name="Вес продукта в рецепте")  # вес

    def __str__(self):
        return f"{self.recipe.name} - {self.product.name}"

    class Meta:
        verbose_name = 'Рецепт Продукт'
        verbose_name_plural = 'Рецепты Продукты'