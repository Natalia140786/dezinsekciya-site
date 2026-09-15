from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import OrderForm
from .models import Order
from services.models import Service   # для получения услуги по slug

def order_view(request):
    # Если передан параметр service, заполняем поле услуги
    initial_data = {}
    service_slug = request.GET.get('service')
    if service_slug:
        try:
            service = Service.objects.get(slug=service_slug)
            initial_data['service'] = service.name
        except Service.DoesNotExist:
            pass

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()
            
            # Отправка письма менеджеру
            subject = f"Новая заявка от {order.name}"
            message = f"""
            Имя: {order.name}
            Телефон: {order.phone}
            Услуга: {order.service}
            Площадь: {order.area}
            Удобное время: {order.preferred_time}
            Сообщение: {order.message}
            """
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.DEFAULT_FROM_EMAIL],   # отправляем на тот же ящик
                fail_silently=False,
            )
            
            messages.success(request, 'Ваша заявка отправлена! Мы свяжемся с вами в ближайшее время.')
            return redirect('home')
    else:
        form = OrderForm(initial=initial_data)

    return render(request, 'orders/order_form.html', {'form': form})