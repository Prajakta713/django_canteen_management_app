from django.shortcuts import render
from mycanteen.models import Section


def user(request):
    # Retrieve all sections and their associated items
    sections = Section.objects.prefetch_related('item_set').all()

    # Debug: Print sections and associated items to console to verify data
    for section in sections:
        print(section.name)
        for item in section.item_set.all():
            print(item.name)

    # Pass sections and items to the template
    return render(request, 'mycanteen/user.html', {'sections': sections})