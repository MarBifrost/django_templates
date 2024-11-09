from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

@login_required(login_url='store:login')
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form=ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})


def send_mail_page(request):
    context={}
    if request.method == 'POST':
        address = request.POST.get('address')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if address and subject and message:
            try:
                send_mail(subject, message, settings.EMAIL_HOST_USER, [address])
                context['result'] = 'Email sent successfully'
            except Exception as e:
                context['result'] = str(e)
        else:
            context['result'] = 'All fields are required'
    return render(request, 'accounts/send_mail.html', context)