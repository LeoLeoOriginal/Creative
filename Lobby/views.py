from django.shortcuts import render

links = {'leo':'https://www.youtube.com/channel/UCLV6eXozEinVXqaTjcVRmvQ',
'learn':'mailto:leoleo.learn@gmail.com?Subject=Interes',
'art':'mailto:leoleo.art21@gmail.com?Subject=Interes',
'music':'https://www.youtube.com/channel/UCNCAIsVIkMNgz8_jUpXJOSg',
'nw':'mailto:leoleo.nw00@gmail.com?Subject=Interes'}


# Create your views here.
def lob(request):
    return render(request, 'lob_son.html', {'leo':links['leo'],'learn':links['learn'],'art':links['art'],'music':links['music'],'nw':links['nw']})