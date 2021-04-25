from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            if request.user.username != "":
                for i in request.user.practitionerRoles.all():
                    if str(i.role_name) in allowed_roles:
                        return view_func(request, *args, **kwargs)
                return HttpResponseRedirect("/Application/login")
            else:
                return HttpResponseRedirect("/Application/login")

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator


def allowed_read_users():
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            if request.user.username != "":
                for i in request.user.practitionerRoles.all():
                    if i.role_name.isUsers:
                        return view_func(request, *args, **kwargs)
                    return HttpResponseRedirect("login")
            else:
                return HttpResponseRedirect("login")

            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator
