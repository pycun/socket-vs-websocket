# views.py
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect


def chat(request, room_name):
    avatar = request.session['avatar']
    username = request.session['username']

    return render(request, 'chat.html', {
        'room_name': room_name,
        'avatar': avatar,
        'username': username
    })


def login(request):
    if request.method == 'POST':
        room = request.POST.get('room')
        request.session['avatar'] = request.POST.get('avatar')
        request.session['username'] = request.POST.get('username')
        request.session['room'] = room
        return HttpResponseRedirect(reverse("chat", args=[room]))
    return render(request, 'login.html', {})
