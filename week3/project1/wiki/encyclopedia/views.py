from django.shortcuts import render, redirect
from random import choice
from markdown2 import markdown


from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def wiki(request, title):
    entries = util.list_entries()
    for entry in entries:
        if title.capitalize() == entry.capitalize():
            content = util.get_entry(entry)
            title = entry
            content = markdown(content)
            break
        else:
            content = None

    return render(request, "encyclopedia/wiki.html", {
        "wiki": content,
        "title": title,
    })
    


def search(request):
    if request.method == "GET":
        q = request.GET.get('q', '')
        if q:
            # Suchlogik: Wenn der Suchbegriff einem Eintrag entspricht, leite zur Wiki-Seite weiter
            entries = util.list_entries()
            for entry in entries:
                if q.lower() == entry.lower():
                    return redirect('wiki', title=entry)
            matches = []
            for entry in entries:
                if q.lower() in entry.lower():
                    matches.append(entry)
            if matches:
                return render(request, "encyclopedia/search.html", {
                    "q": q,
                    "matches": matches
                    })
            
            # Wenn der Suchbegriff keinem Eintrag entspricht, zeige die Suchseite mit dem Suchbegriff an
            return render(request, "encyclopedia/search.html", {
                "q": q
            })
    # Falls kein Suchbegriff vorhanden ist oder ein POST-Request gesendet wird, zeige die Indexseite an
    return redirect('index')

def new(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        content = request.POST.get("content", "")
        if title and content:
            entries = util.list_entries()
            alert = False
            for entry in entries:
                if title.lower() == entry.lower():
                    alert = True
                    return render(request, "encyclopedia/new.html", {
                        "alert": alert,
                        "title": title
                    })
            if not alert:
                util.save_entry(title, content)
                return render(request, "encyclopedia/wiki.html", {
                    "title": title,
                    "wiki": content,
                })
    return render(request, "encyclopedia/new.html", {
        "alert": False
    })

def edit(request, title):
    content = util.get_entry(title)
    if request.method == "POST":
        content = request.POST.get("content", "")
        if content:
            util.save_entry(title, content)
        return redirect("wiki", title=title)
    else:
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "wiki": content
        })

def random(request):
    title = choice(util.list_entries())
    return redirect(wiki, title=title)