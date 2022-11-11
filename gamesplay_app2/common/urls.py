from django.urls import path
from gamesplay_app2.common.views import HomeView, DashboardView

urlpatterns = (
    path('', HomeView.as_view(), name='index'),

    path('dashboard/', DashboardView.as_view(), name='show dashboard'),

)