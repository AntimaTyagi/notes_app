from django.urls import path
from .views import NotesListView, welcomenote_view, NotesFormView, product_details_view,NotesUpdateView,NotesDeleteView
from Notes import views

app_name="notes"

urlpatterns = [
    # path('',views.welcomenote_view,name="welcomenote"),
    path('',NotesListView.as_view(),name="welcomenote"),
    path("<int:pk>/",product_details_view,name="sample"),
    path('createnote/',NotesFormView.as_view(),name="createnote"),
    path('updatenote/<slug:pk>/',NotesUpdateView.as_view(),name="updatenote"),
    path('deletenote/<slug:pk>/',NotesDeleteView.as_view(),name="deletenote")
]