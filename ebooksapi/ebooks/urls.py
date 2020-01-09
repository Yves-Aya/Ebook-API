


from django.urls import path
from ebooks.views import EbookListCreateAPIView, EbookDetailAPIview

urlpatterns = [
    
    path('ebooks/', EbookListCreateAPIView.as_view(), name="ebook-list"),
    path('ebooks/<int:pk>', EbookDetailAPIview.as_view(), name="ebook-detail")
]
