from django.shortcuts import render


def user(request):
    # Add any necessary logic here
    return render(request, 'user.html')


def menu_view(request):
    # Add logic for your menu view here
    return render(request, 'menu.html')