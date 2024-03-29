# Generated by Django 5.0.1 on 2024-01-28 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название продукта'),
        ),
        migrations.AlterField(
            model_name='product',
            name='times_cooked',
            field=models.IntegerField(default=0, verbose_name='Использование продукта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название рецепта'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='products',
            field=models.ManyToManyField(through='recipes.RecipeProduct', to='recipes.product', verbose_name='Продукты в рецепте'),
        ),
        migrations.AlterField(
            model_name='recipeproduct',
            name='weight',
            field=models.IntegerField(verbose_name='Вес продукта в рецепте'),
        ),
    ]
