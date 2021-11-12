from django.core import mail
from django.shortcuts import render
from django.views.generic import TemplateView
from django.core.files.storage import FileSystemStorage
from lxml import etree
from django.core.mail import message, send_mail
from .models import FileXML
import threading


def index(request):
    return render(request, 'index.html')

def upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        if uploaded_file.name[-3:] == 'xml':
            parser = etree.XMLParser(dtd_validation=True)
            xml_file = etree.parse(uploaded_file)
            xml_validator = etree.XMLSchema(file="media/xml_validator.xsd")
            is_valid = xml_validator.validate(xml_file)

            if is_valid:
                name = fs.save(uploaded_file.name, uploaded_file)
                context['url'] = fs.url(name)
                post = FileXML()
                post.title = name
                post.content = etree.tostring(xml_file, pretty_print=True)
                post.author_id = "1" #TODO
                post.save()

            else:
                err_msg = 'Invalid file content!'
                error_mail(request.user.email, err_msg)
                context['url'] = err_msg

        else:
            err_msg = 'Invalid file extension!'
            error_mail(request.user.email, err_msg)
            context['url'] = err_msg
    return render(request, 'xml_project/upload.html', context)



def error_mail(email, message):
    send_mail('XML Project Title', message, 'avci.of@gmail.com', [email,], fail_silently=False)