# Python imports
import datetime
import time

# Django imports
from django.shortcuts import render
from django.http import StreamingHttpResponse


def stream(request):
    def event_stream():
        # Bucle para simular actualizaciones por parte del servidor
        while True:
            # Se programan actualizaciones cada 3 segundos
            time.sleep(3)
            # Yield es un return que conserva la iteracion
            yield 'data: The server time is: %s\n\n' % datetime.datetime.now()
    return StreamingHttpResponse(event_stream(), content_type='text/event-stream')


def index(request):
    return render(request, 'index.html')
