from myapp import models
from django import forms
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from myapp.models import Site_Data
import datetime
import json

class SiteDataModelForm(forms.ModelForm):
    class Meta:
        model = models.Site_Data
        fields = ["total_views", "total_datas", "total_used"]

def show_site_data(request):
    # form = SiteDataModelForm()
    # 如果是ajax请求就返回画图的数据
    current_date = datetime.date.today()
    last_data = Site_Data.objects.exclude(create_time=current_date).order_by('-create_time').first()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        #数据库获取画图数据
        views_data_list = []
        datas_data_list = []
        used_data_list = []
        for i in range(7):
            start_date = current_date + datetime.timedelta(days=i - 6)
            # print(start_date)
            if Site_Data.objects.filter(create_time=start_date).exists():
                views = Site_Data.objects.filter(create_time=start_date).first().total_views
                datas = Site_Data.objects.filter(create_time=start_date).first().total_datas
                used = Site_Data.objects.filter(create_time=start_date).first().total_used

                views_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': views})
                datas_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': datas})
                used_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': used})
            else:
                views_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': 0})
                datas_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': 0})
                used_data_list.append({'time': start_date.strftime("%Y-%m-%d"), 'value': 0})
        data = {
            'views_data_list' : views_data_list,
            'datas_data_list' : datas_data_list,
            'used_data_list' : used_data_list,
            'today_views' : views - last_data.total_views,
            'not_today_views' :  last_data.total_views ,
            'today_datas' : datas - last_data.total_datas,
            'not_today_datas' : last_data.total_datas,
        }
        return JsonResponse(data)
    # 否则就返回首页
    else:
        #获取当前日期，如果不存在今天的数据就创建
        # formatted_date = current_date.strftime("%Y-%m-%d")
        Today_date_not_exists = (not Site_Data.objects.filter(create_time=current_date).exists())
        last_views = Site_Data.objects.exclude(create_time=current_date).order_by('-create_time').first().total_views
        if Today_date_not_exists:
            site_data = Site_Data.objects.create(total_views=last_views + 1, total_datas=200, total_used=150, create_time=current_date)
            site_data.save() 
        # 否则就更新
        else:
            site_data = Site_Data.objects.filter(create_time=current_date).first()
            site_data.total_views += 1
            site_data.save()

            context = {
                'total_views': site_data.total_views,
                'total_data': site_data.total_datas,
                'total_used': site_data.total_used,
                'today_views': site_data.total_views - last_views,
                'today_data': site_data.total_datas - last_data.total_datas,
                'today_used': site_data.total_used - last_data.total_used,
            }
            return render(request, 'index.html',context)