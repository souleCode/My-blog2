

from django.urls import path
from .import views

urlpatterns = [
    path('',views.post_list,name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug>/',views.post_detail,name='post_detail'), #<int:year>/<int:month>/<int:day> cest pour passer en agrumant les parmetres defini dans la vue pour get_absolute_url().
    # path('',views.PostList.as_view(),name='post_list'), #le lien de la vue generic
    path('category/<slug:category>/',views.post_list,name='category_post_list'),
    path('search/',views.post_search,name='post_search'),
    
]
