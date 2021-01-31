from django.urls import path
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index, name='index'),

    path('Capi', views.CategoryList.as_view(), name='categorylist'),
    path('Categories', views.ListCategory.as_view(), name='category'),
    path('Categories/<int:pk>/', views.DetailsCategory.as_view(), name='singlecategory'),

    path('Bapi', views.BookList.as_view(), name='booklist'),
    path('Book', views.ListBook.as_view(), name='book'),
    path('Book/<int:pk>/', views.DetailsBook.as_view(), name='singlebook'),

    path('Papi', views.ProductList.as_view(), name='productlist'),
    path('Product', views.ListProduct.as_view(), name='product'),
    path('Product/<int:pk>/', views.DetailsProduct.as_view(), name='singleProduct'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
