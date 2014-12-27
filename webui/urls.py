from django.conf.urls import url
from django.views.generic import TemplateView
from django.conf import settings

urlpatterns = (
    url(r'^$', TemplateView.as_view(template_name='webui/index.html'), {
        'api_root': settings.API_ROOT,
        'api_token': settings.API_TOKEN,
    }),
)
