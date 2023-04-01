from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from chat.models import Message, Group
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


# @login_required
def group_chat(request, group_id):
    group = Group.objects.get(id=group_id)
    messages = Message.objects.filter(group=group).order_by('date')

    context = {
        'group': group,
        'messages': messages,
    }

    return render(request, 'group.html', context)

# @login_required
# def send_message(request):
#     if request.method == 'POST':
#         content = request.POST.get('content')
#         group_id = request.POST.get('group_id')
#         sender = request.user
#         group = Group.objects.get(id=group_id)
#         message = Message.objects.create(group=group, sender=sender, content=content)
#         data = {'success': True}
#         return JsonResponse(data)
#     else:
#         data = {'success': False}
#         return JsonResponse(data)