from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic as views
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.detail import SingleObjectMixin

from gamesplay_app2.games.forms import CreateGameForm, EditGameForm, DeleteGameForm
from gamesplay_app2.accounts.models import Profile
from gamesplay_app2.games.models import Game


class CreateGameView(views.CreateView):
    template_name = 'games/create-game.html'
    form_class = CreateGameForm
    hide_additional_fields = False
    success_url = reverse_lazy('show dashboard')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    # def form_valid(self, form):
    #     form.instance.user = self.request.user
    #     return super().form_valid(form)


# class DetailsGameView(DetailView, SingleObjectMixin):
#     model = Game
#     template_name = 'details-game.html'
#     hide_additional_fields = False
#     context_object_name = 'game'
#
#     def get_queryset(self):
#         return super().get_queryset().prefetch_related()
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['user'] = self.object.user == self.request.user
#         return context

    # def get_object(self, queryset=None):
    #     if queryset is None:
    #         queryset = self.get_queryset()
    #     else:
    #         pk = self.kwargs.get(self.pk_url_kwarg)
    #         if pk is not None:
    #             queryset = queryset.filter(pk=pk)
    #         game = queryset.get()
    #
    #         return game


def details_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    context = {
        'profile': profile,
        'game': game,
    }
    return render(request, 'games/details-game.html', context)


class EditGameView(UpdateView):
    model = Game
    template_name = 'games/edit-game.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('show dashboard')


class DeleteGameView(DeleteView):
    model = Game
    template_name = 'games/delete-game.html'

    def get_success_url(self):
        return reverse_lazy('show dashboard')


'''
def create_game(request):
    profile = Profile.objects.first()
    if request.method == 'POST':
        form = CreateGameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show home')

    else:
        form = CreateGameForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-game.html', context)


def edit_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = EditGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = EditGameForm(instance=game)

    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'edit-game.html', context)


def delete_game(request, pk):
    profile = Profile.objects.first()
    game = Game.objects.get(pk=pk)
    if request.method == 'POST':
        form = DeleteGameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('show dashboard')
    else:
        form = DeleteGameForm(instance=game)

    context = {
        'profile': profile,
        'form': form,
        'game': game,
    }
    return render(request, 'delete-game.html', context)

'''

