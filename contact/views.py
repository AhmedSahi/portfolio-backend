import json
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["POST"])
def contact_view(request):
    try:
        data = json.loads(request.body)
        name    = data.get('name', '').strip()
        email   = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Basic validation
        if not all([name, email, message]):
            return JsonResponse({'success': False, 'error': 'All fields are required.'}, status=400)

        # Email to YOU (notification in your inbox)
        send_mail(
            subject=f'Portfolio Contact: {name}',
            message=f'Name: {name}\nEmail: {email}\n\nMessage:\n{message}',
            from_email='ahmadsahi344@gmail.com',
            recipient_list=['ahmadsahi344@gmail.com'],
            fail_silently=False,
        )

        # Auto-reply to the sender
        send_mail(
            subject='Thanks for reaching out!',
            message=(
                f'Hi {name},\n\n'
                'Thanks for your message! I received it and will get back to you soon.\n\n'
                'Best,\nAhmed Sahi'
            ),
            from_email='ahmadsahi344@gmail.com',
            recipient_list=[email],
            fail_silently=False,
        )

        return JsonResponse({'success': True})

    except json.JSONDecodeError:
        return JsonResponse({'success': False, 'error': 'Invalid JSON.'}, status=400)
    except Exception as e:
        print(f'Email error: {e}')
        return JsonResponse({'success': False, 'error': str(e)}, status=500)