from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view()),
    path("thread/<int:pk>", views.ThreadView.as_view(), name="thread_detail"),
    path("thread/<int:pk>/response/confirm", views.ConfirmResponseView.as_view(), name="response_confirm"),
    path("thread/<int:pk>/response/create", views.CreateResponseView.as_view(), name="response_create"),
]