import os
import sys
from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '7yx9vwoi@wz3hp&8_eiai&cqoa2h^h*!%nkj88-mt*lw79z9mt')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

from django import forms
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest
from django.core.wsgi import get_wsgi_application


class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""

    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)


def placeholder(request, width, height):
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        height = form.cleaned_data['height']
        width = form.cleaned_data['width']
        # TODO: Generate image of requested size
        return HttpResponse('OK, width: {}, height: {}'.format(width, height))
    else:
        return HttpResponseBadRequest('Invalid Image Request')


def index(request):
    return HttpResponse("<h3>Hello World!<h3>")


urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
    url(r'^$', index, name='homepage'),
)

application = get_wsgi_application()

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
