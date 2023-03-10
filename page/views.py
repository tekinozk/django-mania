from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404
from .fake_db.pages import FAKE_DB_PAGES
from page.models import Page

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


    
def page_view(request,page_slug):
    page = get_object_or_404(Page,slug=page_slug)
    context = dict(
        page=page,
        page_title=page.title,
    )
    return render(request,"page/page_detail.html",context)
   
