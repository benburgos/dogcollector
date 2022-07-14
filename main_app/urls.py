from django.urls import path
from . import views

# YOU LEFT OFF ON THIS PAGE/STEP!
# https://seir-222-sasquatch.netlify.app/second-language/week-20/day-1/lecture-materials/django-urls-views-and-templates/#:~:text=Define%20main_app%27s%20Home%20Page%20URL%20%26%20View
# Other sites to complete homework:
# https://seir-222-sasquatch.netlify.app/second-language/week-20/day-3/lecture-materials/intro-to-django-models/
# https://seir-222-sasquatch.netlify.app/second-language/week-20/day-3/lecture-materials/intro-to-class-based-views/
urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about')
]
