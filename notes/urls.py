from django.urls import path
from . import views
urlpatterns = [
    path('notes/',views.note,name='notes'),
    path('new_note',views.new_note,name='new note'),
    path('notes/<slug:slug>',views.detail_note,name='detail_note')
]