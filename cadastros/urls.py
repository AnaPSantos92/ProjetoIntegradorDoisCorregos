from django.urls import path
from cadastros.views import index, login, logincadastrar,indexcompleta,cadastrar,consultar, usuarioscadastrados,logout,listausuarios,buscar
# from cadastros.views import UsuariosList

urlpatterns = [
    path('', index, name='inicio'),
    path('login/', login, name='login'),
    path('logincadastrar/', logincadastrar, name='logincadastrar'),
    path('indexcompleta/', indexcompleta, name='indexcompleta'),
    path('cadastrar/', cadastrar, name='cadastrar'),
    path('consultar/', consultar, name='consultar'),
    path('usuarioscadastrados', usuarioscadastrados, name='usuarioscadastrados'),
    path('logout/', logout, name='logout'),
    path('listausuarios/', listausuarios, name='listausuarios'),
    # path('listausuarios/', UsuariosList.as_view(), name="listausuarios"),
    path('buscar/', buscar, name="buscar"),

]