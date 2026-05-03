from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('sneakers/', views.sneaker_index, name='sneaker-index'),
    path('sneakers/<int:sneaker_id>/', views.sneaker_detail, name='sneaker-detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneaker-create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneaker-update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneaker-delete'),
    
    path('sneakers/<int:sneaker_id>/add_collecting/', views.add_collecting, name='add-collecting'),
    path('sneakers/<int:sneaker_id>/assoc_condition/<int:condition_id>/', views.associate_condition, name='associate-condition'),
    path('sneakers/<int:sneaker_id>/unassoc_condition/<int:condition_id>/', views.remove_condition, name='unassociate-condition'),
]
