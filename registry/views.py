from django.shortcuts import render
from .models import Person


def persons(request):
    persons_list = Person.objects.all()
    answer = ''
    for el in persons_list:
        answer += f'{el.name} | {el.passport.slug} ; '
    data = {'persons_list': answer}
    return render(request, 'registry/persons/persons.html', context=data)
