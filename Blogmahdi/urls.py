from django.urls import path

from.views import HomeView,EntryView,CreateEntryView

urlpatterns = [
    path('',HomeView.as_view(),name ="blog-home"),
    path("entry/<int:pk>/",EntryView.as_view(),name ="entry-detail"),
    path("create_entry/",CreateEntryView.as_view(success_url='/'),name ="create_entry"),        
]
