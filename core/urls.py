from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomePageView.as_view(), name='home'),
    path('clubs/', ClubsView.as_view(), name='clubs'),
    path('clubs/<int:pk>/details/', ClubDetailsView.as_view(), name='clubs'),
    path('countries/<int:pk>/clubs/', ClubsByCountry.as_view(), name='clubs-by-country'),
    path('latest-transfers/', LatestTransfersView.as_view(), name='latest-transfers'),
    path('top-150-accurate-predictions/', Top150AccuratePredictions.as_view(), name='top-150-accurate-predictions'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
