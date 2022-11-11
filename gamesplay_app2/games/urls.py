from django.urls import path, include

from gamesplay_app2.games.views import details_game, CreateGameView, EditGameView, DeleteGameView

urlpatterns = (
    path('create/', CreateGameView.as_view(), name='create game'),
    path('<str:email>/game/slug:game_slug/', include([
        path('', details_game, name='details game'),
        path('edit/', EditGameView.as_view(), name='edit game'),
        path('delete/', DeleteGameView.as_view(), name='delete game')
    ])),
)
# urlpatterns = (
#     path('add/', add_pet, name='add pet'),
#     path('<str:username>/pet/<slug:pet_slug>/', include([
#         path('', details_pet, name='details pet'),
#         path('edit/', edit_pet, name='edit pet'),
#         path('delete/', delete_pet, name='delete pet'),
#     ]))
# )