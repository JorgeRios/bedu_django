from django.urls import include, path
from . import views
from rest_framework import routers
#from django.contrib.auth.decorators import login_required, permission_required
#path('about/', login_required(TemplateView.as_view(template_name="secret.html"))),

app_name = 'clients'
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'clients', views.ClientViewSet)


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('bio', views.bio, name='bio'),
    path('bio/<id>/', views.bio, name='bio2'),
    path('other', views.MorningGreetingView.as_view(greeting="quivoles"), name="greet"),
    path('publishers/', views.PublisherList.as_view()),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
