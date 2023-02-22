from . import index, detail, vote, results
from django.urls import path

urlpatterns = [
    path('', index, name="index"),
    path('<int:question_id>/', detail, name="question detail"),
    path('<int:question_id>/results', results, name="question vote page"),
    path('<int:question_id>/vote', vote, name="question results"),
]