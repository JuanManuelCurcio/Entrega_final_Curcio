from django.shortcuts import render

def main(req):
    return render(req, "main.html", {})

def index(req):
    return render(req, "index.html", {})

def no_access_view(req):
    return render(req, "no_access_view.html", {})

def about(req):
    return render(req, "about.html", {})