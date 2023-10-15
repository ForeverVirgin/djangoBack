from django.db import models

# Create your models here.
from django.shortcuts import redirect
from django.urls import reverse, path


class Menu(models.Model):
    title = models.CharField(max_length=255)
    url = ""

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
        ordering = ['pk']

class Item(models.Model):
    title = models.CharField(max_length=255)
    motherItem = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    level = 0
    url = ""

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'
        ordering = ['pk']