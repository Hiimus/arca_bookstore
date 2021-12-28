from django.shortcuts import render

# Create your views here.


def view_faq(request):
    """ A view that renders the FAQ page """
    return render(request, 'help/faq.html')


def view_policies(request):
    """ A view that renders the Policies page """
    return render(request, 'help/policies.html')


def view_contact(request):
    """ A view that renders the Contact page """
    return render(request, 'help/contact.html')



