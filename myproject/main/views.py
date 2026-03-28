from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def project_detail(request, project_id):
    return HttpResponse(f"<h1>Жоба №{project_id}</h1><p>Бұл - динамикалық параметрлерді қолдану мысалы.</p>")

def info(request):
    ip = request.META.get('REMOTE_ADDR')
    user_agent = request.META.get('HTTP_USER_AGENT')
    return HttpResponse(f"<h3>Пайдаланушы мәліметтері:</h3><p>IP-мекенжай: {ip}</p><p>Браузер мен ОЖ: {user_agent}</p>")