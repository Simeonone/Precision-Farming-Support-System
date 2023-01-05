from django.urls import path
from .views import render_pdf_view, CustomerpdfListView, customerpdf_render_pdf_view

app_name = 'customerpdf'

urlpatterns = [
    path('', CustomerpdfListView.as_view(), name='customer-list-view'),
    path('test/', render_pdf_view, name = 'test-view'),
    path('pdf/<pk>/', customerpdf_render_pdf_view, name = 'customer-pdf-view'),
]