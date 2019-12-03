from django.urls import path
from . import views

urlpatterns = [
    path(r'',views.index, name='index'),
    # path(r'details/(?P<id>\w{1,50})/$',views.details),
      path(r'details/<int:id>/',views.details),
      path(r'add', views.add)

]
