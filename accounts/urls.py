from django.urls import path
from . import views
from django.conf.urls import include


urlpatterns = [


    path('signup_patient', views.signup_patient, name="signup_patient"),
    path('sign_in_patient', views.sign_in_patient , name='sign_in_patient'),
    path('savepdata/<str:patientusername>', views.savepdata , name='savepdata'),
    

    path('logout', views.logout , name='logout'),


    # path('home', views.home, name='home'),
    # path('profile/', views.profile, name='profile'),
    # path('accounts/', include('allauth.urls')),
    # path('oauth/', include('social_django.urls', namespace='social')),
]