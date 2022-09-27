from django.shortcuts import render


def landing_page(request):
    return render(
        request=request,
        template_name='playground/landing-page.html'
    )
