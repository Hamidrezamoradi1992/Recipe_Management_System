from django.urls.conf import path
from recipes.views import recipe_list,recipe_create,recipe_update,recipe_delete,recipe_view
urlpatterns = [
    path('', recipe_list, name='recipe_list'),
    path('create/', recipe_create, name='recipe_create'),
    path('delete/<int:pk>',recipe_delete,name='recipe_delete'),
    path('view/<int:pk>',recipe_view,name='recipe_view'),
    path('update/<int:pk>',recipe_update,name='recipe_update'),
]