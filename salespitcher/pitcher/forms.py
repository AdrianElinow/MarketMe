from django import forms

class NewPlayerForm(forms.Form):
	player_name = forms.CharField(label="player_name",max_length=32)

	def is_valid(self):
		data = self.cleaned_data['player_name']

		if len(data) > 1 and len(data) < 32:
			return data

class TaglineForm(forms.Form):
	text = forms.CharField(max_length=256)

class Vote(forms.Form):
	selection = forms.IntegerField()