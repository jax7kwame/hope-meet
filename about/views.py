from django.shortcuts import render, redirect
from django.contrib import messages
from .models import About
from contact.forms import ContactUsForm


def about_view(request):
    # about object
    about_info = About.objects.all()

    # contact us form
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(request, "Successfully submitted...")

            return redirect('about')
    else:
        form = ContactUsForm()

    form = ContactUsForm()
    context = {
        'about_info': about_info,
        'form': form
    }

    return render(request, 'about.html', context)