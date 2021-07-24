from django.urls import path
from PizzaApp import views
from django.contrib.auth import views as vs

urlpatterns=[
    path('', views.home, name='hm'),
    path('signup/', views.signup, name='signup'),
    path('login/', vs.LoginView.as_view(template_name='html/login.html'), name='login'),
    path('logout/',vs.LogoutView.as_view(template_name='html/logout.html'),name="logout"),
    path('itemlist/',views.itlist,name="itemlist"),
    path('itemdel/<int:n>/',views.itemdel,name="itemdel"),
    path('itemup/<int:m>/',views.itemup,name="itemup"),
    path('vm/',views.vegmenu,name="vm"),
    path('nvm/',views.nvegmenu,name="nvm"),
    path('ct/',views.cart,name="ct"),
    path('ctdlt/<int:m>/',views.cartdel,name="ctdlt"),
    path('bill/',views.bill,name="bill"),
    path('order/',views.orders,name="order"),
    path('orderdel/<int:m>/',views.orderdel,name="orderdel"),
    path('ordhis/',views.history,name="ordhis"),
    path('pf/',views.pfle,name="pf"),
    path('profupdt/', views.profupdt, name='profupdt'),
    path('chpw/',views.changepwd,name="chpw")
]