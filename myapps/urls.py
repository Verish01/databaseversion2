from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.inventory_list, name='inventory_list'),
    path('edit/<int:id>/', views.edit_item, name='edit_item'),
    path('delete/<int:id>/', views.delete_item, name='delete_item'),
    path('visualization/', views.inventory_visualization, name='inventory_visualization'),
    path('add/', views.add_item, name='add_item'),
    path('export_csv/', views.export_inventory_csv, name='export_inventory_csv'),
    path('query/', views.query_view, name='query_view'),
    path('clear_history/', views.clear_history, name='clear_history'),
    path('weather/', views.weather_list, name='weather_list'),
    path('weather/<int:pk>/', views.weather_detail, name='weather_detail'),
    path('export_weather_csv/', views.export_weather_csv, name='export_weather_csv'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
