from django.shortcuts import render
from . import models

def all_cloth(request):
    if request.method == 'GET':
        cloth = models.Cloth.objects.filter().order_by('-id')
        return render (request, 'cloth/all_cloth.html', {'cloth': cloth})

def male_cloth(request):
    if request.method == 'GET':
        male_cloth = models.Cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
        return render(request, 'cloth/male_cloth.html', {'male_cloth': male_cloth})

def female_cloth(request):
    if request.method == 'GET':
        female_cloth = models.Cloth.objects.filter(tags__name='женская одежда').order_by('-id')
        return render(request, 'cloth/female_cloth.html', {'female_cloth': female_cloth})


def child_cloth(request):
    if request.method == 'GET':
        child_cloth = models.Cloth.objects.filter(tags__name='детская одежда').order_by('-id')
        return render(request, 'cloth/child_cloth.html', {'child_cloth': child_cloth})