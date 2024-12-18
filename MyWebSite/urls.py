"""
URL configuration for MyWebSite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    # path("admin/", admin.site.urls),
    #首页
    path("", views.index),

    #UI界面
    path("ui-features/buttons/", views.buttons),
    path("ui-features/typography/", views.typography),

    #按钮区
    path("forms/basic_elements/", views.basic_elements),

    #图表区
    path("charts/chartjs/", views.chartjs),

    #表格区
    path("tables/basic-table/", views.basic_table),

    #图表区
    path("icons/mdi/", views.mdi),

    #用户区
    path("samples/login/l", views.l),
    path("samples/login-2/", views.login_2),
    path("samples/register/", views.register),
    path("samples/register-2/", views.register_2),
    path("samples/lock-screen/", views.lock_screen),

    #文档
    path("documentation/documentation/", views.documentation),
]
