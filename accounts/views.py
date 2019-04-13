from django.shortcuts import render, redirect, resolve_url
from django.urls import reverse
from django.contrib import messages
from django.http import JsonResponse, HttpResponseRedirect

from accounts.forms import (
    RegistrationForm,
    EditProfileForm,
    ChangePassword,
    PasswordResetConfirmForm
)

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash, login, get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError



from django.utils.translation import ugettext as _
from django.utils.http import is_safe_url, urlsafe_base64_decode
from django.utils.encoding import force_text

from home.models import BlogPost
from django.forms.models import model_to_dict

from django.contrib.auth.tokens import default_token_generator

from django.template.response import TemplateResponse

def register(request):

    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
          user=form.save()
          username = request.POST.get('username')
          password = request.POST.get('password1')

          login(request, user)
          return redirect(reverse('home:home'))
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'accounts/reg_form.html', args)


def validate_username(request):
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)


def view_profile(request, pk=None):
    storage = messages.get_messages(request)
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    args = {'user': user, 'message': storage}
    return render(request, 'accounts/profile.html', args)

def view_profile_entries(request, pk):

    user=User.objects.get(pk=pk)
    user_articles = BlogPost.objects.filter(author=user)
    user_articles_list = list(BlogPost.objects.filter(author = user).values_list('title', flat=True))
    args = {'user':user, 'user_articles':user_articles}

    return render(request, 'accounts/profile_entries.html', args)




def edit_profile(request):
    user=User.objects.get(id=request.user.id)
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('accounts:view_profile'))
    else:
        form = EditProfileForm(initial=model_to_dict(user))
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)

def change_password(request):
    if request.method == 'POST':
        form = ChangePassword(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your new password has been saved.')
            update_session_auth_hash(request,form.user)
            return redirect(reverse('accounts:view_profile'))

    else:
        form = ChangePassword(user=request.user)
    args = {'form': form}
    return render(request,'accounts/change_password.html', args)

def password_reset_confirm_view(request, uidb64=None, token=None,
                           template_name='accounts/reset_password_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=PasswordResetConfirmForm,
                           post_reset_redirect="{% url' accounts:password_reset_complete' %}",
                           current_app=None, extra_context=None):


    UserModel = get_user_model()
    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = _('Enter new password')
        if request.method =='POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(post_reset_redirect)

        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = _('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)
