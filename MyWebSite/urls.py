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
from myapp.views import site_data ,dataset_analysis_page,remote_sensing_images,tools_page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # path("admin/", admin.site.urls),
    #首页
    path("", site_data.show_site_data),

    #遥感分割界面
    path("remote_sensing_image/segmentation/", remote_sensing_images.segmentation),
    path("remote_sensing_image/analysis/", remote_sensing_images.model_analysis),

    #按钮区
    path("forms/basic_elements/", remote_sensing_images.basic_elements),

    #图表区
    path("charts/chartjs/", tools_page.chartjs),

    #表格区
    path("tables/basic-table/", dataset_analysis_page.basic_table),

    #图表区
    path("icons/mdi/", dataset_analysis_page.mdi),

    #用户区
    path("samples/login/l", dataset_analysis_page.l),
    path("samples/login-2/", dataset_analysis_page.login_2),
    path("samples/register/", dataset_analysis_page.register),
    path("samples/register-2/", dataset_analysis_page.register_2),
    path("samples/lock-screen/", dataset_analysis_page.lock_screen),

    #文档
    path("documentation/documentation/",dataset_analysis_page.documentation),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
