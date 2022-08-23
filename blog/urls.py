from django.urls import path
from . import views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('about/', views.about, name='about'),
    path('publication/<int:pk>', views.PublicationDetail.as_view(), name='publication-detail'),
    path('publications/', views.PublicationList.as_view(), name='publications'),
    ]

    