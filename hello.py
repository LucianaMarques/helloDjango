#helloDjango
import sys
from django.conf.urls import url
from django.conf import settings
from django.http import HttpResponse

def index(Request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index)
)

settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

if __name__ == "main":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)