from django.urls import path
from . import views

urlpatterns = [
    path("click/", views.index, name="index"),
    path("<int:shop_id>", views.shop, name="shop"),
    path("logout", views.logout_view, name="logout"),
    path("book", views.book, name="book")
]
