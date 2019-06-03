from django.urls import path, includefrom rest_framework import routersfrom .views import *p_router = routers.DefaultRouter()p_router.register('', ProductViewSet)c_router = routers.DefaultRouter()c_router.register('', CategoryViewSet)ps_router = routers.DefaultRouter()ps_router.register('', ProductStatusViewSet)t_router = routers.DefaultRouter()t_router.register('', TagsViewSet)pp_router = routers.DefaultRouter()pp_router.register('', ProductPhotoViewSet)urlpatterns = [    path('tags/', include(t_router.urls)),    path('products/', include(p_router.urls)),    path('product_photos/', include(pp_router.urls)),    path('categories/', include(c_router.urls)),    path('product_statuses/', include(ps_router.urls)),]# for url in pp_router.urls:#     print(url)