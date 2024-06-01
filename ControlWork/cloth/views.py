from . import models
from django.views import generic


class AllClothView(generic.ListView):
    template_name = "cloth/all_cloth.html"
    context_object_name = "cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class ElderClothView(generic.ListView):
    template_name = "cloth/elder_cloth.html"
    context_object_name = "elder_cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="Пенсионерская одежда").order_by("-id")


class ChildishClothView(generic.ListView):
    template_name = "cloth/childish_cloth.html"
    context_object_name = "childish_cloth"
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter(tags__name="Детская одежда").order_by("-id")


