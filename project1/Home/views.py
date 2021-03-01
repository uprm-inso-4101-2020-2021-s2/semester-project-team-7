from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def about(request):
    my_context = {
        "my_text": "about us",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "about.html", my_context)


def contact(request):
    return render(request, "contact.html", {})
