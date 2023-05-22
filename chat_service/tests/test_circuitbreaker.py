from requests import JsonResponse, args
from random import randint
import time

def test_errors():

    n = randint(0, 100)
    time = randint(4, 10)

    if n < 20:
        return JsonResponse({'error': 'Error with the chat service.'}, status=500)
    elif 20 >= n <= 50:
        return JsonResponse({'error': 'Not Found'}, status=400)
    elif 50 >= n <= 80:
        return JsonResponse({'success': 'OK'}, status=200)
    elif 80 >= n <= 100:
        time.sleep(time)
        return JsonResponse({'success': 'OK con Latencia'}, status=200)
