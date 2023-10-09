"""
URL configuration for hack project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mental import views as app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',app.default),
    path('login',app.login),
    path('login_validation',app.check_cred),
    path('books',app.books),
    path('dashboard',app.dashboard),
    path('music',app.music),
    path('pop',app.pop),
    path('christmas',app.christmas),
    path('disney',app.disney),
    path('sour',app.sour),
    path('bollywood',app.bollywood),
    path('worship',app.worship),
    path('radio',app.radio),
    path('meditation',app.meditation),
    path('exercise',app.exercise),
    path('mydiary',app.mydiary),
    path('activity',app.activity),
    path('home',app.home),
    path('logout',app.logout),
    path('feedback',app.feedback),
    path('daily_report',app.report)
]
