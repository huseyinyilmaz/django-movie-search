from django import forms


class NameForm(forms.Form):
    name = forms.CharField(initial='The Matrix')
    year = forms.IntegerField(initial='1999')


class IDForm(forms.Form):
    imdb_id = forms.CharField(initial='tt0133093')
