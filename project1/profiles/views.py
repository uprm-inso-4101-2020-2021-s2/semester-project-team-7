from django.shortcuts import render

from .models import profiles


# Create your views here.
def profile_detail_view(request):
    obj = profiles.objects.get(id=1)
    context = {
        'email': obj.email,
        'name': obj.name
    }
    return render(request, "profiles/detail.html", context)
