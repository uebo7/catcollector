from django.urls import path
from . import views

# NOTE: django ONLY uses GET and POST; there is not REST in django; we never do DELETE, PUT
# NOTE: in django updating and deleting will be conducted using POST request
# NOTE: django paths NEVER begin with a "/"; django prepends this automatically
"""
Examples of deleting and updating
path('cats/<int:cat_id>/remove_cat/'),
path('cats/<int:cat_id>/remove_cat/'),
"""

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cats/', views.cats_index, name='cats_index'),
    path('cats/<int:cat_id>/', views.cats_detail, name='cats_detail'),
]