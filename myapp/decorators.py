from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages


def admin_required(view_func):

    @wraps(view_func)

    def wrapper(request, *args, **kwargs):

        if 'adminid' not in request.session:

            messages.error(request, "Please login as Admin.")

            return redirect('adminlogin')

        return view_func(request, *args, **kwargs)

    return wrapper



def student_required(view_func):

    @wraps(view_func)

    def wrapper(request, *args, **kwargs):

        if 'studentid' not in request.session:

            messages.error(request, "Please login first.")

            return redirect('student_login')

        return view_func(request, *args, **kwargs)

    return wrapper