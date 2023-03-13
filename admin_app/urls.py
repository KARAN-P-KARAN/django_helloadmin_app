from django.urls import path
from .import views 

urlpatterns = [
     
  path('',views.index,name='index'),
  path('components-alerts/',views.alerts,name='alerts'),
  path('components-accordion/',views.accordion,name='accordion'),
  path('components-badges/',views.badges,name='badges'),
  path('components-breadcrumbs/',views.breadcrumbs,name='breadcrumbs'),
  path('components-buttons/',views.buttons,name='buttons'),
  path('components-cards',views.cards,name='cards'),
  path('components-carousel/',views.carousel,name='carousel'),
  path('components-list-group/',views.list_group,name='list_group'),
  path('components-modal/',views.modal,name='modal'),
  path('components-tabs/',views.tabs,name='tabs'),
  path('components-pagination/',views.pagination,name='pagination'),
  path('components-progress/',views.progress,name='progress'),
  path('components-spinners/',views.spinners,name='spinners'),
  path('components-tooltips',views.tooltips,name='tooltips',),
  path('forms-elements/',views.elements,name='elements'),
  path('forms-layouts/',views.layouts,name='layouts'),
  path('forms-editors/',views.editors,name='editors'),
  path('forms-validation/',views.validation,name='validation'),
  path('tables-general/',views.general,name='general'),
  path('tables-data/',views.data,name='data'),
  path('charts-chartjs/',views.chartjs,name='chartjs'),
  path('charts-apexcharts/',views.apexcharts,name='apexcharts'),
  path('charts-echarts/',views.echarts,name='echarts'),
  path('icons-bootstrap/',views.bootstrap,name='bootstrap'),
  path('icons-remix/',views.remix,name='remix'),
  path('icons-boxicons/',views.boxicons,name='boxicons'),
  path('users-profile/',views.profile,name='profile'),
  path('pages-faq/',views.faq,name='faq'),
  path('pages-contact/',views.contact,name='contact'),
  path('pages-register/',views.register,name='register'),
  path('pages-login/',views.login,name='login'),
  path('pages-error-404/',views.error,name='error'),
  path('pages-blank/',views.blank,name='blank'),


]