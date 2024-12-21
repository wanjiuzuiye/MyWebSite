from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.conf import settings 
import os
from myapp.models import Remote_Sensing_Image,Segmentation_Image
from django import forms

#定义原始图像的ModelForm
class Remote_Sensing_imagesForm(forms.ModelForm):
    class Meta:
        model = Remote_Sensing_Image
        fields = ['img_path']
        widgets = {
            'img_path':forms.ClearableFileInput(attrs={'class':'form-control-file'})
        }
#定义图像分割结果的ModelForm
class Segmentation_imagesForm(forms.ModelForm):
    class Meta:
        model = Remote_Sensing_Image
        fields = ['img_path']

def segmentation(request):
    if request.method == 'GET':
        form = Remote_Sensing_imagesForm()
        return render(request, 'pages/remote_sensing_image/segmentation.html',{'form':form})
    
    # file_object = request.FILES.get('image')
    # print(file_object.name)#获取文件名
    # #保存文件
    # save_path = os.path.join(settings.MEDIA_ROOT,'remote_sensing_images',file_object.name)
    # f = open(save_path,mode='wb')
    # for chunk in file_object.chunks():
    #     f.write(chunk)
    # f.close()
    form = Remote_Sensing_imagesForm(request.POST, request.FILES)
    if form.is_valid():
        img_path = form.cleaned_data['img_path']
        img_name = img_path.name.split('/')[-1] #获取文件名
        remote_image = form.save(commit=False)
        remote_image.img_name = img_name
        remote_image.save()
        return render(request, 'pages/remote_sensing_image/segmentation.html',{'form':form})
    return redirect('segmentation.html')

def typography(request):
    return render(request, 'pages/ui-features/typography.html')

def basic_elements(request):
    return render(request, 'pages/forms/basic_elements.html')