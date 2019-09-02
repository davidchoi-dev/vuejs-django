from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, DeleteView
from django.views.decorators.csrf import csrf_exempt

from todo.models import Todo


class ApiTodoLV(ListView):
    model = Todo

    def render_to_response(self, context, **response_kwargs):
        todoList = list(context['object_list'].values())
        return JsonResponse(data=todoList, safe=False)


@method_decorator(csrf_exempt, name='dispatch')
class ApiTodoDelV(DeleteView):
    model = Todo

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return JsonResponse(data={}, status=204)


