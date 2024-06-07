# создал отдельным файлом, в случае, если при расширении визуализация API станет сложнее

from django.urls import path
from . import views

urlpatterns = [
    path('api/farpost-ads/<int:ad_id>/', views.FarpostAdAPIView.as_view()),
    path('api/register/', views.FarpostAdAPIView.as_view()),
    path('api/login/', views.FarpostAdAPIView.as_view()),
]

