from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from gamesplay_app2.accounts.models import Profile
from gamesplay_app2.games.models import Game


# def show_home(request):
#     profile = Profile.objects.first()
#     if not profile:
#         return redirect('create profile')
#
#     context = {
#         'profile': profile,
#     }
#
#     return render(request, 'home-page.html', context)


class HomeView(TemplateView):
    template_name = 'common/home-page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = Profile.objects.first()
        return context

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return super().dispatch(request, *args, **kwargs)


class DashboardView(ListView):
    model = Game
    template_name = 'common/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        hide_additional_fields = False
        context['games'] = Game.objects.all()
        return context


# def show_dashboard(request):
#     profile = Profile.objects.first()
#     games = Game.objects.all()
#
#     context = {
#         'profile': profile,
#         'games': games,
#     }
#
#     return render(request, 'dashboard.html', context)


#     model = PetPhoto
#     template_name = 'main/photo_edit.html'
#     fields = ('description',)
#
#     def get_success_url(self):
#         return reverse_lazy('edit pet photo', kwargs= {'pk': self.object.id})
