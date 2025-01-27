from ninja_crud.testing.core.components import PathParameters, Payloads
from ninja_crud.testing.views import (
    CreateModelViewTest,
    DeleteModelViewTest,
    ListModelViewTest,
    RetrieveModelViewTest,
    UpdateModelViewTest,
)
from ninja_crud.testing.viewsets import ModelViewSetTestCase
from tests.test_app.tests.base_test_case import BaseTestCase
from tests.test_app.views.user_views import UserViewSet


class TestUserViewSet(ModelViewSetTestCase, BaseTestCase):
    model_viewset_class = UserViewSet
    base_path = "api/users"

    def get_path_parameters(self):
        return PathParameters(ok={"id": self.user_1.id})

    def get_user_payloads(self):
        return Payloads(
            ok={
                "username": "new-user",
                "email": "user@email.com",
                "password": "new-password",
                "groups": [self.group_1.id, self.group_2.id],
            },
            bad_request={"username": "new-user", "password": "new-password"},
            conflict={
                "username": self.user_2.username,
                "email": "user@email.com",
                "password": "new-password",
            },
        )

    test_list_users = ListModelViewTest()
    test_create_user = CreateModelViewTest(payloads=get_user_payloads)
    test_retrieve_user = RetrieveModelViewTest(path_parameters=get_path_parameters)
    test_update_user = UpdateModelViewTest(
        path_parameters=get_path_parameters, payloads=get_user_payloads
    )
    test_delete_user = DeleteModelViewTest(path_parameters=get_path_parameters)
