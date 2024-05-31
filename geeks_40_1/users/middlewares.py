from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class AgeAllowedGanres(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            age = int(request.POST.get("age"))
            if age < 5:
                return HttpResponseBadRequest(
                    "Ваш возраст слишком мал для прочтения книг :("
                )
            elif age >= 5 and age <= 10:
                request.allowed_ganres = "Сказки"
            elif age >= 11 and age <= 18:
                request.allowed_ganres = "Фантастика"
            elif age >= 18 and age <= 45:
                request.allowed_ganres = "Художественная Литература"
            else:
                return HttpResponseBadRequest(
                    "Извините вы уже слишком стары для наших книг"
                )
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "allowed_ganres", "Ваш жанр не определен ")
