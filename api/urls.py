from django.urls import path
from api import views

urlpatterns = [
    path('data/datalist/<str:id>',views.databyid),
    path('data/datalist/',views.dataList),
    path('data/create/',views.create),
    path('data/get/',views.get_data),
    path('data/update/',views.update),
    path('data/delete/',views.delete),
]