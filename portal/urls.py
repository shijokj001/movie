from django.urls import path


from portal.views import HomeView, MovieAddView, MovieUpdateView, MovieDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie/add/', MovieAddView.as_view(), name='add'),
    path('movie/<int:pk>/', MovieUpdateView.as_view(), name='update'),
    path('movie/<int:pk>/delete/', MovieDeleteView.as_view(), name='delete'),
]
