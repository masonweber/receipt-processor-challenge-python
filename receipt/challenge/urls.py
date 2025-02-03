from django.urls import path

from . import views

urlpatterns = [
    path("receipts", views.index, name="index"),
    path("receipts/process", views.process, name="process"),
    path("receipts/<uuid:id>/points", views.points, name="points"),
]