from django.views.generic import View
from django.views.generic import TemplateView
from django.shortcuts import render
from movies import api
from movies import forms


class IndexView(TemplateView):
    template_name = 'index.html'


class NameSearchView(View):
    template_name = 'query.html'
    form_class = forms.NameForm

    def get(self, request):
        ctx = {'form': self.form_class()}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        ctx = {'form': form,
               'movie': None}
        if form.is_valid():
            data = form.cleaned_data
            kwargs = {'title': data['name']}
            if data['year']:
                kwargs['year'] = data['year']
            movie = api.get_movie_by_title(**kwargs)
            ctx['movie'] = movie
        return render(request, self.template_name, ctx)


class IDSearchView(View):
    template_name = 'query.html'
    form_class = forms.IDForm

    def get(self, request):
        ctx = {'form': self.form_class()}
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        ctx = {'form': form,
               'movie': None}
        if form.is_valid():
            data = form.cleaned_data
            movie = api.get_movie_by_id(imdb_id=data['imdb_id'])
            ctx['movie'] = movie
        return render(request, self.template_name, ctx)
