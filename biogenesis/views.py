from django.shortcuts import render, redirect
from django.views.generic.base import View
from django.views.generic import ListView, DetailView
from .models import Entity, Vid, Family, Book
from .forms import ReviewForm, AddStateForm
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.forms import inlineformset_factory
from django.forms import formset_factory
from django.forms import modelformset_factory
from django.contrib.auth.models import User


class VidFamilyBook:
    def get_familys(self):
        return Family.objects.all()

    def get_vidss(self):
        # if not Vid.objects.all().exists():
        #     return True
        # else:
            return Vid.objects.all()

    def get_books(self):
        return Book.objects.all()


class CreateView(View):
        def get(self, request):
            form = AddStateForm()
            # form = modelformset_factory(EntityShots, fields = ("image",), form = AddStateForm , extra = 1)
            #formset = inlineformset_factory(Entity, EntityShots, fields=("image",), extra=1)
            context = {
                'form': form,
            }
            if request.user.is_authenticated:
                return render(request, 'entitys\create.html', context)
            else :
                return redirect('/accounts/signup')

        def post(self, request,):
            #formset = modelformset_factory(EntityShots, form=StateForm, extra=1)
            #formset = formset_factory(StateForm, extra=1)
            #formset= inlineformset_factory(Entity, EntityShots, fields=("image",), extra=1)
            #entity = Entity.objects.get(id=pk)
            #formset = formset(instance=entity)
            if request.method == 'POST':
                form = AddStateForm(request.POST, request.FILES)
                #formset =  formset(request.POST, request.FILES, instance=entity )
                #formset = formset(request.POST, request.FILES)

                # formset = (forms.save().id)

                if form.is_valid():
                    entity = form.save(commit=False)
                    entity.user = request.user
                    #obj.user = request.user
                    #obj.save()
                    entity.save()
                    #if formset.is_valid():
                         #formset = formset.save(commit=False)
                         #formset = Entity.objects.get(id=pk)
                         #formset.form_id = form.id
                    #     formset.save()
                    return redirect("/")
                else:
                    context = {
                        'form': form,
                        #'formset': formset,
                    }
                    return render(request, 'entitys\create.html', context)



class EntityView(VidFamilyBook, ListView):
    #Список существ
    model = Entity
    queryset = Entity.objects.filter(draft=False)
    template_name = "entitys\entity_list.html"
    paginate_by = 3


class IndexView(View):
    def get(self, request):
        return HttpResponseRedirect("/")


class EntityDetailView(VidFamilyBook, DetailView):
    model = Entity
    slug_field = "url"
    template_name = "entitys\entity_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        entity = Entity.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.entity = entity
            form.save()
        return redirect(entity.get_absolute_url())


class FilterEntitysView(VidFamilyBook, ListView):
    paginate_by = 3
    def get_queryset(self):
        queryset = Entity.objects.filter(
            Q(vid__in=self.request.GET.getlist("vid")) |
            Q(family__in=self.request.GET.getlist("family")) |
            Q(book__in=self.request.GET.getlist("book"))
        ).distinct()
        return queryset
    template_name = "entitys\entity_list.html"
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["vid"] = ''.join([f"vid={x}&" for x in self.request.GET.getlist("vid")])
        context["family"] = ''.join([f"family={x}&" for x in self.request.GET.getlist("family")])
        context["book"] = ''.join([f"book={x}&" for x in self.request.GET.getlist("book")])
        return context


class Search(VidFamilyBook, ListView):
    paginate_by = 3

    def get_queryset(self):
            return Entity.objects.filter(title__iregex=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
    template_name = "entitys\entity_list.html"

def my_view(request):
    if request.user.is_authenticated():
        return render(request, 'accounts/signup.html')
