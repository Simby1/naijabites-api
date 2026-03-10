from django.contrib import admin
from django.urls import path
from recipes.views import RecipeList, RecipeDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/recipes/', RecipeList.as_view(), name='recipe-list'),
    path('api/recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),
]