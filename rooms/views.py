from django.shortcuts import render

def home_view(request):
    return render(request, 'home.html')
def room_view(request, room):
    return render(request, 'room.html')
