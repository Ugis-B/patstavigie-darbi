from django.shortcuts import render
from django.views.generic import View, ListView
from user.models import User
from django.http import HttpRequest, HttpResponse

# def index(request):
#
#     users = User.objects.all()
#
#     context = {
#         'users': users,
#     }
#
#     return render(
#         template_name='index.html',
#         request=request,
#         context=context,
#     )

class AddUserView(View):
    def get(self,request):
        return render(
            template_name='user.html',
            request=request,
            # context=context,
        )
    def post(self,request):
            user = User(
                username=request.POST['name'],
                email=request.POST['email'],
            )

            user.save()

            context = {
                'user': user,
            }

            return render(
                template_name='form.html',
                request=request,
                context=context,

            )

class UserListView(ListView):
    model = User
    template_name = 'index.html'

# def add_user(request):
# #
#     if request.method == 'POST':
#
#         user = User(
#             username=request.POST['name'],
#             email=request.POST['email'],
#         )
#
#         user.save()
#
#         context = {
#             'user': user,
#         }
#
#         return render(
#             template_name='user.html',
#             request=request,
#             context=context,
#
#         )
#
#     return render(
#         template_name='form.html',
#         request=request
#     )
#
#
def get_user(request, user_id):

    user = User.objects.get(pk=user_id)

    context = {
        'user': user,
    }

    return render(
        template_name='user.html',
        request=request,
        context=context,

    )


def delete_user(request, user_id):

    user = User.objects.get(pk=user_id)
    user.delete()

    return HttpResponse(f'Deleted {user.username}')


def edit_user(request, user_id):

    user = User.objects.get(id=user_id)

    if request.method == 'POST':

        username = request.POST['name']
        email = request.POST['email']

        if len(username) != 0:
            user.username = username

        if len(email) != 0:
            user.email = email

        user.save()

        context = {
            'user': user,
        }

        return render(
            template_name='user.html',
            request=request,
            context=context,

        )

    return render(
        template_name='form.html',
        request=request
    )