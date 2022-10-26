from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("thread/<int:pk>", views.ThreadView.as_view(), name="thread_detail"),
    path("thread/confirm", views.ConfirmThreadView.as_view(), name="thread_confirm"),
    path("thread/create", views.CreateThreadView.as_view(), name="thread_create"),
    path("thread/<int:pk>/response/confirm", views.ConfirmResponseView.as_view(), name="response_confirm"),
    path("thread/<int:pk>/response/create", views.CreateResponseView.as_view(), name="response_create"),
]