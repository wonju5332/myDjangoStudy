# 뷰를 호출하려면, 이와 연결된 URL이 있어야 한다.
# 이를 위해 URLconf가 필요함.
# urls.py를 생성하여, URLconf를 생성해보자.

from django.urls import path
from . import views


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


