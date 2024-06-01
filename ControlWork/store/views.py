from . import models
from django.views import generic
from django.http import HttpResponse
from .models import VideoContent
from django.shortcuts import get_object_or_404
from . import forms


class MainPageView(generic.ListView):
    template_name = "main.html"
    model = models.VideoContent
    context_object_name = "devises"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["video_content"] = VideoContent.objects.order_by("-id")
        context["items"] = models.Items.objects.order_by("-id")[:5]
        return context


class InformationView(generic.TemplateView):
    template_name = "information.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["image_url"] = "/media/storePic/image.jfif"
        context["message"] = "В нашем магазине есть все что связано с электро техникой"
        return context


class ItemDetailsView(generic.DetailView):
    template_name = "items_details.html"
    context_object_name = "item_id"

    def get_object(self, **kwargs):
        item_id = self.kwargs.get("id")
        return get_object_or_404(models.Items, id=item_id)


class AllItemsView(generic.ListView):
    template_name = "all_items.html"
    context_object_name = "items"
    model = models.Items

    def get_queryset(self):
        return self.model.objects.filter().order_by("-id")


class CreateReviewView(generic.CreateView):
    template_name = "create_review.html"
    form_class = forms.ReviewForm
    success_url = "/"

    def from_valid(self, form):
        print(form.cleaned_data)
        return super(CreateReviewView, self).form_valid(form=form)


