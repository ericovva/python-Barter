from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader, Context
from service.models import Category,CategorySubcategory
import json

def index(request):
    latest_question_list = [["first","second","333"],["third","fourth","4444"],["third","fourth","4444"]];
    #t = loader.get_template('service/modal_window.html') Blog.objects.filter(entry__authors__name__isnull=True)
    #objects = Category.objects.filter(categorysubcategory_requests_category=True);
    #print objects
    relations = CategorySubcategory.objects.select_related('category');
    H = {}
    for rel in relations:
        if rel.category in H:
            H[rel.category].append(rel.subcategory);
        else:
            H[rel.category] = [rel.subcategory]
    #context2 = {'modal_window': t.render(context)}
    return render(request, 'service/index.html',{'H' : H})

def get_subcategories(request,category_id):
    print "Category_id " + category_id; 
    t = loader.get_template('service/subcategory_items.html')
    relations = CategorySubcategory.objects.select_related('subcategory').filter(category__id = category_id);
    context = {"relations": relations}
    response = {
            'category_name' : relations[0].category.name,
            'widget'        : t.render(context),
            'status'        : 'OK'
    }
    return HttpResponse(json.dumps(response), content_type="application/json")
