from django.template import loader,Context
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.http import HttpRequest, HttpResponse, Http404
from apps.models import Item, Comment, Cathegorie, Mark, Feature
from django.shortcuts import get_object_or_404
from django.db.models import Q


def review(request, name):
    response = get_object_or_404(Item, name=name)
    return render_to_response("review.html",{"data": response,
                                             'comments': Comment.objects.filter(item=response)},
                              context_instance = RequestContext(request))

def review_all(request, name):
    response = Item.objects.filter(
        Q(name__icontains=name) |
        Q(description__icontains=name)
    )[:5]
    return render_to_response("review_all.html",{"data": response,
                                             'comments': Comment.objects.filter(item=response)},
                              context_instance = RequestContext(request))

def item_filter(request):
    response = ''
    if request.method == 'POST':
        if request.is_ajax():
            input_data = request.POST.get('request')
            if not input_data:
                input_data = request.POST
                cathegorie = Cathegorie.objects.filter(name=input_data['cathegorie'])
                if input_data['availability'] == 'true':
                    availability = True
                else:
                    availability = False
                feature = Feature.objects.filter(Q(diagonal__gte=input_data['diagonal'])).filter(Q(os__icontains=input_data['os'])).filter(hdd__lte=input_data['hdd']).filter(Q(proccesor__icontains=input_data['proccesor']))
                mark = Mark.objects.filter(name=input_data['mark'])
                response = Item.objects.all().filter(mark=mark).filter(cathegorie=cathegorie).filter().filter(availability=availability).filter(price__lte=input_data['high_price']).filter(price__gte=input_data['low_price']).filter(features=feature)[:5]
            else:
                response = Item.objects.filter(
                    Q(name__icontains=input_data) |
                    Q(description__icontains=input_data)
                )[:5]
            return render_to_response('ajax/items.html',
                                      { 'data': response if response else False })
        else:
            input_data = request.POST.get('search')
            if not len(input_data):
                response = Item.objects.all()
            else:
                response = Item.objects.filter(
                    Q(name__icontains=input_data) |
                    Q(description__icontains=input_data)
                )
            return render_to_response('products.html',
                                      { 'data': response if response else False }, context_instance = RequestContext(request))
    return render_to_response('products.html', { 'data': False}, context_instance = RequestContext(request))


