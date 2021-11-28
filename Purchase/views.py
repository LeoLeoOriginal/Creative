from django.shortcuts import render


links = {'leo':'https://www.youtube.com/channel/UCLV6eXozEinVXqaTjcVRmvQ',
'learn':'mailto:leoleo.learn@gmail.com?Subject=Interes',
'art':'mailto:leoleo.art21@gmail.com?Subject=Interes',
'music':'https://www.youtube.com/channel/UCNCAIsVIkMNgz8_jUpXJOSg',
'nw':'mailto:leoleo.nw00@gmail.com?Subject=Interes'}

# Create your views here.
def pur(request, style):

    if int(style) == 1:
        web = 'pur_son1.html'
    elif int(style) == 2:
        web = 'pur_son2.html'
    elif int(style) == 3:
        web = 'pur_son3.html'
    elif int(style) == 4:
        web = 'pur_son4.html'
    else:
        web = '404.html'
    
    return render(request, web, {'leo':links['leo'],'learn':links['learn'],'art':links['art'],'music':links['music'],'nw':links['nw']})