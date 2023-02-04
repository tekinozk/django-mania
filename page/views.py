from django.shortcuts import render
from django.http import HttpResponse,Http404
from .fake_db.pages import FAKE_DB_PAGES
# FAKE_DB_PROJECTS = [
#     f"https://picsum.photos/id/{id}/100/80" for id in range(21,29)
# ]
FAKE_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1200/400" for id in range(24,28)
]
def home(request):
    page_title = "Home"
   
    context = dict(
        page_title=page_title,
        hero_content = "lorem",
        # images=FAKE_DB_PROJECTS,
        carousel = FAKE_DB_CAROUSEL, 


    )
    return render(request,"page/index.html",context)

def about(request):
   
    page_title = "Hakkimizda"
    context = dict(
        page_title=page_title,
        hero_content = "lorem",
        # images = FAKE_DB_PROJECTS,
    )
    return render(request,"page/about.html",context)

def contact(request):
    
    page_title = "İletisim"
    context = dict(
        page_title=page_title,
        hero_content = "lorem",
        # images=FAKE_DB_PROJECTS,

    )
    return render(request,"page/contact.html",context)

def mission(request):
   
    page_title = "Vizyonumuz"
    context = dict(
        page_title=page_title,
        hero_content = "lorem",
        # images=FAKE_DB_PROJECTS,

    )
    return render(request,"page/mission.html",context)
    
def page_view(request,slug):
    filtered = list(filter(lambda element: element["url"] == slug, FAKE_DB_PAGES ))
    if filtered:
        context = dict(
        #   images=FAKE_DB_PROJECTS,
          page_title = filtered[0]["page_title"],
          detail = filtered[0]["detail"]
    )
        return render(request,"page/page_detail.html",context)
    return Http404  
