from django.urls import path
from page.views import (
    home,
    about,
    contact,
    mission,
    page_view,
)
    


urlpatterns = [
    path('', home,name="home"),
    # path("about/",about,name="about_us"),
    # path("contact/",contact,name="contact"),
    # path("mission/",mission,name="mission" ),
    path("<slug:slug>/",page_view,)
]