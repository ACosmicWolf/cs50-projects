from django.shortcuts import render, redirect
from django.http import HttpResponse

from . import util

import markdown2

from fuzzywuzzy import process

entries = util.list_entries()

import random

def index(request):
    if request.method == "GET":
        random_page = random.choice(entries)
        print(random_page)
    return render(request, "encyclopedia/index.html", {
        "entries": entries,
        "random_page": random_page
    })

def title(request, title):
    if title in entries:
        html = markdown2.markdown(util.get_entry(title))
        return  render(request, "encyclopedia/titlepage.html", { "title": title, "html": html })
    else:
        return render(request, "encyclopedia/404_titlepage.html", {"title": title})

def createpage(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        util.save_entry(title, content)
    return  render(request, "encyclopedia/createpage.html")
   
def edit(request, title):
    if request.method == "POST":
        content = request.POST.get("content")
        util.save_entry(title, content)
        return redirect("/wiki/"+title)

    content = util.get_entry(title)
    return  render(request, "encyclopedia/editpage.html", {"title": title, "content": content})

def search(request):
    if request.method == "GET":
        query = request.GET.getlist("q")[0]
        if query in entries:
            return redirect("/wiki/"+query)
        else:
            results = process.extract(query, entries)
            results_list = []
            for result in results:
                if result[1] >= 60:
                    results_list.append(result[0])
            return render(request, "encyclopedia/search.html", {"results":results_list})
    else:
        return render(request, "encyclopedia/index.html")
