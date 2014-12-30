from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


def persona_login(request):
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        import pdb; pdb.set_trace()  # XXX BREAKPOINT
        login(request, user)

    return HttpResponse('OK')
