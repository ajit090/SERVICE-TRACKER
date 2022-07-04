from django.contrib import admin
from django.urls import path,include
from fir_model import views
from .views import Fir,FirAPIView,FirDetail,index,Techtracker,TechtrackerAPIView,TechtrackerDetail,CustomerList

urlpatterns = [
    path('',views.index,name='index'),
    path('FIR/',FirAPIView.as_view()),
    path('detail2/<int:pk>/',FirDetail.as_view()),
    path('TECH/',TechtrackerAPIView.as_view()),
    path('detail1/<int:pk>/',TechtrackerDetail.as_view()),
    path('customerissues/',CustomerList.as_view()),

]
