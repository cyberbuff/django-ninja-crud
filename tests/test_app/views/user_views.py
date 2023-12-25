from django.contrib.auth.models import User
from ninja import Router

from ninja_crud import views
from ninja_crud.viewsets import ModelViewSet
from tests.test_app.schemas import UserIn, UserOut

router = Router()


class UserViewSet(ModelViewSet):
    model = User

    list_users = views.ListModelView(output_schema=UserOut, pagination_class=None)
    create_user = views.CreateModelView(input_schema=UserIn, output_schema=UserOut)
    retrieve_user = views.RetrieveModelView(output_schema=UserOut)
    update_user = views.UpdateModelView(input_schema=UserIn, output_schema=UserOut)
    delete_user = views.DeleteModelView()


UserViewSet.register_routes(router)
