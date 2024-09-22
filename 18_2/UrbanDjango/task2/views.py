from django.shortcuts import render

# Create your views here.
def classT(request):
    return render(request, 'second_task/class_template.html')

def funcT(request):
    return render(request, 'second_task/func_template.html')