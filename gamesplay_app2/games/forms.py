from django import forms
from gamesplay_app2.games.models import Game


class CreateGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'
        exclude = 'user',


class EditGameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = '__all__'


class DeleteGameForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'

    def save(self, commit=True):
        self.instance.delete()
        return self.instance

    class Meta:
        model = Game
        fields = '__all__'
