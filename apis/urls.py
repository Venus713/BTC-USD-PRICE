from django.urls import path

from .views import QuoteView

urlpatterns = [
    path("v1/quotes/", QuoteView.as_view(), name="quotes"),
]
