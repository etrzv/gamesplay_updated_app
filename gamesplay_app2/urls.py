from django.contrib import admin
from django.urls import path, include

urlpatterns = (
    path('admin/', admin.site.urls),
    path('', include('gamesplay_app2.common.urls')),
    path('accounts/', include('gamesplay_app2.accounts.urls')),
    path('common/', include('gamesplay_app2.common.urls')),
    path('games/', include('gamesplay_app2.games.urls')),
)


''' 
from django.contrib import admin
from django.urls import path

from gamesplay_app2.games.views import details_game, CreateGameView, EditGameView, DeleteGameView
from gamesplay_app2.common.views import HomeView, DashboardView
from gamesplay_app2.accounts.views import CreateProfileView, details_profile, edit_profile, delete_profile

urlpatterns = (
    path('', HomeView.as_view(), name='index'),

    path('dashboard/', DashboardView.as_view(), name='show dashboard'),

    path('game/create/', CreateGameView.as_view(), name='create game'),
    path('game/details/<int:pk>', details_game, name='details game'),
    path('game/edit/<int:pk>', EditGameView.as_view(), name='edit game'),
    path('game/delete/<int:pk>', DeleteGameView.as_view(), name='delete game'),

    path('profile/create/', CreateProfileView.as_view(), name='create profile'),
    path('profile/details/', details_profile, name='details profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
)

http://localhost:8000/ - home page

http://localhost:8000/dashboard/ - dashboard page

http://localhost:8000/game/create/ - create game page
http://localhost:8000/game/details/<id>/ - details game page
http://localhost:8000/game/edit/<id>/ - edit game page
http://localhost:8000/game/delete/<id>/ - delete game page

http://localhost:8000/profile/create - create profile page
http://localhost:8000/profile/details/ - details profile page
http://localhost:8000/profile/edit/ - edit profile page
http://localhost:8000/profile/delete/ - delete profile page
'''

