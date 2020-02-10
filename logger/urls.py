from django.conf.urls import url
import views

urlpatterns = [
    url(r'getForm', views.LogViewTemplate, name='log_form_template'),
    url(r'save-log-data-from-template', views.SaveLogFromTemplate, name='log_template_save'),
]
