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


def english(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "English.html", my_context)


def spanish(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "spanish.html", my_context)


def japanese(request):
    my_context = {
        "my_text": "english",
        "my_number": 123,
        "my_list": [1, 2, 3]

    }
    return render(request, "japanese.html", my_context)


def contact(request):
    return render(request, "contact.html", {})
