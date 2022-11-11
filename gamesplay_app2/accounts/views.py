from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import views as auth_views, get_user_model
from django.views import generic as views
from gamesplay_app2.accounts.forms import CreateProfileForm, EditProfileForm, DeleteProfileForm
from gamesplay_app2.accounts.models import Profile
from gamesplay_app2.games.models import Game


# def create_profile(request):
#
#     if request.method == 'POST':
#         form = CreateProfileForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('show home')
#     else:
#         form = CreateProfileForm()
#
#     context = {
#         'form': form,
#     }
#
#     return render(request, 'create-profile.html', context)
# def details_profile(request):
#     profile = Profile.objects.first()
#     games = Game.objects.all()
#     q_games = len(games)
#     if q_games > 0:
#         avg_rating = sum([g.rating for g in games]) / q_games
#     else:
#         avg_rating = 0.0
#
#     context = {
#         'profile': profile,
#         'q_games': q_games,
#         'avg_rating': avg_rating,
#     }
#     return render(request, 'accounts/details-profile.html', context)
#
#
# def edit_profile(request):
#     profile = Profile.objects.first()
#
#     if request.method == 'POST':
#         form = EditProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             return redirect('details profile')
#     else:
#         form = EditProfileForm(instance=profile)
#
#     context = {
#         'profile': profile,
#         'form': form,
#     }
#     return render(request, 'accounts/edit-profile.html', context)
#
#
# def delete_profile(request):
#     profile = Profile.objects.first()
#     games = Game.objects.all()
#
#     if request.method == 'POST':
#         form = DeleteProfileForm(request.POST, instance=profile)
#         if form.is_valid():
#             form.save()
#             games.delete()
#             return redirect('show home')
#
#     form = DeleteProfileForm(instance=profile)
#
#     context = {
#         'form': form,
#         'profile': profile,
#         'games': games,
#     }
#
#     return render(request, 'accounts/delete-profile.html', context)

UserModel = get_user_model()


class CreateProfileView(CreateView):
    template_name = 'accounts/create-profile.html'
    form_class = CreateProfileForm
    success_url = reverse_lazy('index')


class SignInView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'


class SignOutView(auth_views.LogoutView):
    next_page = reverse_lazy('index')

# def details_profile(request):
#     profile = Profile.objects.first()
#     games = Game.objects.all()
#     q_games = len(games)
#     if q_games > 0:
#         avg_rating = sum([g.rating for g in games]) / q_games
#     else:
#         avg_rating = 0.0
#
#     context = {
#         'profile': profile,
#         'q_games': q_games,
#         'avg_rating': avg_rating,
#     }
#     return render(request, 'accounts/details-profile.html', context)


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/details-profile.html'
    model = Profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['games_count'] = self.object.games_set.count()
        context['games'] = self.object.games_set.all()

        if context['games_count'] > 0:
            context['avg_rating'] = sum([g.rating for g in context['games']]) / len(context['games'])
        else:
            context['avg_rating'] = 0.0

        # TODO:
        # games = self.object.games_set.prefetch_related('games')

        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/edit-profile.html'
    model = Profile

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={
            'pk': self.request.user.pk,
        })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/delete-profile.html'
    model = Profile
    success_url = reverse_lazy('index')
