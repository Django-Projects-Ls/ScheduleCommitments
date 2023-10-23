from django.urls import path
from . import views

urlpatterns = [
    path('', views.commitments_request_handler, name='commitment'),
    path('details/<int:id>', views.details_request_handler, name='commitment details'),
    path('create-forms', views.create_commitment, name='create commitment'),
    path('details/edit-forms/<int:pk>', views.edit_commitment, name='edit commitment'),
    path('details/delete-forms/<int:pk>', views.delete_commitment, name='delete commitment') 
]
