from asgiref.sync import async_to_sync
from django.shortcuts import render
from core.agent import main


def text_view(request):
    output = ""
    if request.method == "POST":
        user_input = request.POST.get("user_text")
        
        if user_input:

            output = async_to_sync(main)(user_input)

    return render(request, "core/home.html", {"output": output})
