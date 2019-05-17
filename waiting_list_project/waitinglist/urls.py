from django.urls import path
from . import views

urlpatterns = [
    path('entries/', views.EntryListView.as_view(), name='entries'),
    path('entry/<int:pk>', views.EntryDetailView.as_view(), name='entry-detail'),
]

urlpatterns += [
    path('', views.EntryCreate.as_view(), name='entry_create'),
    path('entry/<int:pk>/update/', views.EntryUpdate.as_view(), name='entry_update'),
    path('entry/<int:pk>/delete/', views.EntryDelete.as_view(), name='entry_delete'),
]
