from django.shortcuts import render

def text_view(request):
    output = ""
    if request.method == "POST":
        user_input = request.POST.get("user_text")
        # Example processing: reverse the text
        output = user_input[::-1]

    return render(request, "core/home.html", {"output": output})
