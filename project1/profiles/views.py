from django.shortcuts import render

from .models import profiles

from .forms import ProfileForm


# Create your views here.
def profile_create_view(request):
    form = ProfileForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProfileForm()

    context = {
        'form': form
    }
    return render(request, "profiles/profile_create.html", context)


def profile_detail_view(request):
    obj = profiles.objects.get(id=1)
    # context = {
    #   'email': obj.email,
    #   'name': obj.name
    # }
    context = {
        'object': obj
    }
    return render(request, "profiles/detail.html", context)
