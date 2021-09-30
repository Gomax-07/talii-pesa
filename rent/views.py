from django.http import Http404, HttpResponse
from django.shortcuts import render

# Create your views here.

from .models import *
from django.views import generic


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_houses = House.objects.all().count()
    num_rent = Rent.objects.all().count()

    # Available payments (status = 'p')
    num_rent_paid = Rent.objects.filter(status__exact='G').count()

    # The 'all()' is implied by default.
    num_tenants = Tenant.objects.count()

    context = {
        'num_houses': num_houses,
        'num_rent': num_rent,
        'num_rent_paid': num_rent_paid,
        'num_tenants': num_tenants,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


def house_detail_view(request, primary_key):
    try:
        house = House.objects.get(pk=primary_key)
    except House.DoesNotExist:
        raise Http404('House does not exist')

    return render(request, 'rent/house_detail.html', context={'house': house})


class HouseListView(generic.ListView):
    model = House
    paginate_by = 10

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(HouseListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context


class HouseDetailView(generic.DetailView):
    model = House
