
from django.urls import path

from . import views


urlpatterns = [
    path("", views.EntityView.as_view(), name = "index"),
    path("ru/", views.IndexView.as_view()),
    path("create/", views.CreateView.as_view(), name = 'create'),
    path("filter/", views.FilterEntitysView.as_view(), name='filter'),
    path("search/", views.Search.as_view(), name='search'),
    path("<slug:slug>/", views.EntityDetailView.as_view(), name="entity_detail"),
    path("review/<int:pk>/", views.AddReview.as_view(), name = "add_review")


]