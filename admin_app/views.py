from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    
    return render(request,'index.html')

def alerts(request):
    return render(request,'components-alerts.html')    

def accordion(request):
    return render(request,'components-accordion.html')

def badges(request):
    return render(request,'components-badges.html')

def breadcrumbs(request):
    return render(request,'components-breadcrumbs.html')

def buttons(request):
    return render(request,'components-buttons.html')

def cards(request):
    return render(request,'components-cards.html')

def carousel(request):
    return render(request,'components-carousel.html')

def list_group(request):
    return render(request,'components-list-group.html')

def modal(request):
    return render(request,'components-modal.html')

def tabs(request):
    return render(request,'components-tabs.html')

def pagination(request):
    return render(request,'components-pagination.html')

def progress(request):
    return render(request,'components-progress.html')

def spinners(request):
    return render(request,'components-spinners.html')

def tooltips(request):
    return render(request,'components-tooltips.html')

def elements(request):
    return render(request,'forms-elements.html')

def layouts(request):
    return render(request,'forms-layouts.html')

def editors(request):
    return render(request,'forms-editors.html')

def validation(request):
    return render(request,'forms-validation.html')

def general(request):
    return render(request,'tables-general.html')

def data(request):
    return render(request,'tables-data.html')

def chartjs(request):
    return render(request,'charts-chartjs.html')

def apexcharts(request):
    return render(request,'charts-apexcharts.html')

def echarts(request):
    return render(request,'charts-echarts.html')

def bootstrap(request):
    return render(request,'icons-bootstrap.html')

def remix(request):
    return render(request,'icons-remix.html')

def boxicons(request):
    return render(request,'icons-boxicons.html')

def profile(request):
    return render(request,'users-profile.html')

def faq(request):
    return render(request,'pages-faq.html')

def contact(request):
    return render(request,'pages-contact.html')

def register(request):
    return render(request,'pages-register.html')

def login(request):
    return render(request,'pages-login.html')

def error(request):
    return render(request,'pages-error-404.html')

def blank(request):
    return render(request,'pages-blank.html')




