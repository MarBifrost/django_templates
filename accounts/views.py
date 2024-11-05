from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm

# Create your views here.

@login_required(login_url='store:login')
def profile_view(request):
    profile = request.user.profile
    if request.method == 'POST':
        form=ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'accounts/profile.html', {'form': form})
