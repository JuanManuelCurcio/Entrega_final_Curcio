from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


# Create your views here.

def BehLabTools_view(req):
    if req.user.is_authenticated:
        return render(req, "BehLabTools_view.html", {})
    else:
        return redirect('no_access_view')