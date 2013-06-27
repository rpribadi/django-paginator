import string
from random import randint, sample

from django.shortcuts import render

from paginator.paginator import Paginator

def _get_random_text():
    random_list = []
    for _ in range(0, 1000):
        random_list.append(
           "".join(sample(string.ascii_letters, randint(20, 40)))
        )

    return random_list


def index(request):
    obj_list = _get_random_text()
    paginator = Paginator(obj_list)

    return render(
        request,
        "index.html",
        {'obj_list': obj_list,
         'paginator': paginator,
         'title': 'This is tite',
        })
