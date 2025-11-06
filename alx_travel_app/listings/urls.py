from django.urls import path
from .views import HelloListingView

urlpatterns = [
    path('hello/', HelloListingView.as_view()),  
]
