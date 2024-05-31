from django.shortcuts import render
from . import models
from django.views import generic





class AllClothView(generic.ListView):
    template_name = 'cloth/all_cloth.html'
    context_object_name = 'cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')
# def all_cloth(request):
#     if request.method == 'GET':
#         cloth = models.Cloth.objects.filter().order_by('-id')
#         return render (request, 'cloth/all_cloth.html', {'cloth': cloth})


class MaleClothView(generic.ListView):
    template_name = 'cloth/male_cloth.html'
    context_object_name = 'male_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='мужская одежда').order_by('-id')

# def male_cloth(request):
#     if request.method == 'GET':
#         male_cloth = models.Cloth.objects.filter(tags__name='мужская одежда').order_by('-id')
#         return render(request, 'cloth/male_cloth.html', {'male_cloth': male_cloth})

class FemaleClothView(generic.ListView):
    template_name = 'cloth/female_cloth.html'
    context_object_name = 'female_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='женская одежда').order_by('-id')
# def female_cloth(request):
#     if request.method == 'GET':
#         female_cloth = models.Cloth.objects.filter(tags__name='женская одежда').order_by('-id')
#         return render(request, 'cloth/female_cloth.html', {'female_cloth': female_cloth})

class ChildClothView(generic.ListView):
    template_name = 'cloth/child_cloth.html'
    context_object_name = 'child_cloth'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детская одежда').order_by('-id')

# def child_cloth(request):
#     if request.method == 'GET':
#         child_cloth = models.Cloth.objects.filter(tags__name='детская одежда').order_by('-id')
#         return render(request, 'cloth/child_cloth.html', {'child_cloth': child_cloth})