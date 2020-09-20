from django.shortcuts import render,redirect

from django.http import HttpResponse, Http404
from django.views import View


from .forms import UrlForm
from .models import UrlData

class UrlView(View):
    form_class = UrlForm
    template_name = 'shortner/home.html'
    # Handle GET HTTP requests
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # Handle POST GTTP requests
    def post(self, request, *args, **kwargs):
        url=None
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            url = form.instance
            print(url.shortened_url)

        return render(request, self.template_name, {'form': form,'url': url})

class WebsiteUrl(View):
    def get(self, request, *args, **kwargs):
        print(args)
        print(kwargs['slug'])
        full_url = UrlData.objects.filter(shortened_url=kwargs['slug']).first()
        if not full_url:
            raise Http404
        return redirect(full_url.long_url)

