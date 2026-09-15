from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    services = Service.objects.filter(is_active=True).order_by('order', 'name')
    return render(request, 'services/service_list.html', {'services': services})

def service_detail(request, slug):
    service = get_object_or_404(Service, slug=slug, is_active=True)
    # Если SEO-заголовок не заполнен, используем название услуги
    seo_title = service.seo_title or f"{service.name} — дезинсекция в [ваш город]"
    seo_description = service.seo_description or f"Профессиональная дезинсекция от {service.name}. Гарантия, безопасность, срочный выезд."
    return render(request, 'services/service_detail.html', {
        'service': service,
        'seo_title': seo_title,
        'seo_description': seo_description,
    })


def home(request):
    # Берём первые 6 активных услуг для главной (можно изменить количество)
    services = Service.objects.filter(is_active=True).order_by('order', 'name')[:6]
    return render(request, 'index.html', {'services': services})
