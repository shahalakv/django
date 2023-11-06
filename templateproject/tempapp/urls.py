from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cust_reg',views.cust_reg,name='cust_reg'),
    path('phy_reg',views.phy_reg,name='phy_reg'),
    path('login_view',views.login_view,name='login_view'),
    path('admin_page',views.admin_page,name='admin_page'),
    path('customer_page',views.customer_page,name='customer_page'),
    path('physician_page',views.physician_page,name='physician_page'),
    path('logout_view',views.logout_view,name='logout_view'),
]
