from django.views.generic import DetailView, CreateView, UpdateView
from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from app.models import Flower, Action

# Create your views here.


def home(request):
    flowers = Flower.objects.all()
    return render(request, 'home.html', {'flowers': flowers})



class FlowerDetailView(DetailView):
    template_name = 'detail.html'
    model = Flower
    context_object_name = 'flower'



class LikeFlowerView(CreateView, UpdateView):
    http_method_names = ['post']
    model = Action
    fields = ('liked', )

    def get_object(self):
        return Action.objects.get_or_create(
            user=self.request.user,
            flower=Flower.objects.get(
                id=self.kwargs.get('flower_id')
            )
        )[0]

    def _like_or_dislike(self):
        if self.request.POST.get('like'):
            return True

        if self.request.POST.get('dislike'):
            return False

        return None

    def form_valid(self, form):
        interaction = self.get_object()
        interaction.liked = self._like_or_dislike()
        interaction.save()
        return HttpResponseRedirect(reverse('flower-detail', kwargs={'pk': self.kwargs.get('flower_id')}))
