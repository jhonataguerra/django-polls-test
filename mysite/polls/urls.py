from django.urls import path
from . import views


# Home page
urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
]

# Details, results and votes
urlpatterns += [
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
