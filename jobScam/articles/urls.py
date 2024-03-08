from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('what-is-a-job-scam/', views.article1, name='article1'),
    path('why-victims-fall-into-job-scam/', views.article2, name='article2'),
    path('how-to-prevent-from-job-scam/', views.article3, name='article3'),
    path('red-flags-of-job-scam/', views.article4, name='article4'),
]