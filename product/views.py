from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from product.models import Product,Category,Review,ProductImage
from rest_framework import status
from product.serializers import ProductSerializer,CategorySerializer,ReviewSerializer,ProductImageSerializer
from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from product.filters import ProductFilter 
from rest_framework.filters import SearchFilter,OrderingFilter
from product.paginations import DefaultPagination
from api.permissions import IsAdminOrReadOnly,FullDjangoModelPermission
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from product.permissions import IsReviewAuthorOrReadonly
from drf_yasg.utils import swagger_auto_schema


class ProductViewSet(ModelViewSet):
       """
       API endpoint is for managing  in cityshop
       - Allow Authenticated admin to create,update and delete products
       - Allows user to browse and filter products
       - Support searching by name, category
       - Support Odering by price and updated_at
       """
       queryset=Product.objects.all()
       serializer_class=ProductSerializer
       filter_backends=[DjangoFilterBackend,SearchFilter,OrderingFilter]
       filterset_class=ProductFilter
       pagination_class=DefaultPagination
       search_fields=['name','description']
       ordering_fields=['price','updated_at']
 
       permission_classes=[IsAdminOrReadOnly]

       @swagger_auto_schema(
                     operation_summary="Retrive a list of product"
       )
       def list(self, request, *args, **kwargs):
              """
              Retrive all the products
         
              """
              return super().list(request, *args, **kwargs)
       
       @swagger_auto_schema(
                     operation_summary="Create a product by admin",
                     operation_description="This allow an admin to create a product",
                     request_body=ProductSerializer,
                     responses={
                            201:ProductSerializer,
                            400:"Bad Request"
                     }
       )
       def create(self, request, *args, **kwargs):
              """Ony authenticated user can add product"""
              return super().create(request, *args, **kwargs)
       
 
 
 

class ProductImageViewSet(ModelViewSet):
       serializer_class=ProductImageSerializer
       permission_classes=[IsAdminOrReadOnly]


       def get_queryset(self):
              return  ProductImage.objects.filter(product_id=self.kwargs.get('product_pk'))
       

       def perform_create(self, serializer):
              serializer.save(product_id=self.kwargs.get('product_pk'))
 
       

class CategoryViewSet(ModelViewSet):
       permission_classes=[IsAdminOrReadOnly]
       queryset=categories=Category.objects.annotate(product_count=Count('products')).all()
       serializer_class=CategorySerializer

 

class ReviewViewSet(ModelViewSet):
 
       serializer_class=ReviewSerializer
       permission_classes=[IsReviewAuthorOrReadonly]

       def perform_create(self, serializer):
              serializer.save(user=self.request.user)

       def perform_update(self, serializer):
               serializer.save(user=self.request.user)
               

       def get_queryset(self):
              return  Review.objects.filter(product_id=self.kwargs.get('product_pk'))

       def get_serializer_context(self):
              return  {'product_id':self.kwargs.get('product_pk')}
            

 