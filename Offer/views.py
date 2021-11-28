from django.shortcuts import render
from django.core.mail import send_mail

links = {'leo':'https://www.youtube.com/channel/UCLV6eXozEinVXqaTjcVRmvQ',
'learn':'mailto:leoleo.learn@gmail.com?Subject=Interes',
'art':'mailto:leoleo.art21@gmail.com?Subject=Interes',
'music':'https://www.youtube.com/channel/UCNCAIsVIkMNgz8_jUpXJOSg',
'nw':'mailto:leoleo.nw00@gmail.com?Subject=Interes'}


# Create your views here.
def of(request):
    done = False
    if request.method == 'POST':
        done = True
        for i in request.POST:
            print(i)

        if int(request.POST['style']) == 0:
            st = 'Estilo libre'
        elif int(request.POST['style']) == 1:
            st = 'Estilo 1'
        elif int(request.POST['style']) == 2:
            st = 'Estilo 2'
        elif int(request.POST['style']) == 3:
            st = 'Estilo 3'
        elif int(request.POST['style']) == 4:
            st = 'Estilo 4'

        sub = '''Orden a Creative'''
        message = f'''Orden hecha por {request.POST['name']}

Estilo                  :       {st}
Detalles del producto   :       {request.POST['name']}
Correo electrónico      :       {request.POST['details']}
Teléfono                :       {request.POST['tel']}
Dirección               :       {request.POST['address']}'''
        send_mail(
            sub,#subject
            message,#message
            request.POST['email'],#from
            [request.POST['email'], 'leoleo.art.creative@gmail.com'],#to
        )

    return render(request, 'of_son.html', {'submitted':done,'leo':links['leo'],'learn':links['learn'],'art':links['art'],'music':links['music'],'nw':links['nw']})