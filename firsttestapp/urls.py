from django.urls import path
from . import views

urlpatterns = [
	path('createpost', views.createpost, name="createpost"),
	path('show', views.show),
	path('destroy',views.destroy, name="deletepost"),
	path('update',views.update, name="updatepost"),
]