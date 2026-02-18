from django.urls import path
from .views import landing_view,home_view,list_view,listing_view,edit_view
urlpatterns = [
    path('',landing_view,name="main"),
    path('home/',home_view,name="home"),
    path('list/',list_view,name="list"),
    path('listing/<str:id>/',listing_view,name="listing"),
    path('listing/<str:id>/edit',edit_view,name="edit")
]
