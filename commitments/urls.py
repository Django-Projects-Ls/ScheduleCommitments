from django.urls import path
from . import views

urlpatterns = [
    path('', views.commitments_request_handler, name='commitment'),
    path('details/<int:id>', views.details_request_handler, name='commitment details'),
    path('create-forms', views.create_commitment, name='create commitment')   
]
