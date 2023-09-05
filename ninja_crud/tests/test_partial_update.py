import logging

from django.http import HttpResponse

from ninja_crud.tests.request_components import AuthHeaders, PathParameters, Payloads
from ninja_crud.tests.request_composer import ArgOrCallable, TestCaseType
from ninja_crud.tests.test_update import TestUpdateModelView
from ninja_crud.views import PartialUpdateModelView

logger = logging.getLogger(__name__)


class TestPartialUpdateModelView(TestUpdateModelView):
    model_view_class = PartialUpdateModelView
    model_view: PartialUpdateModelView

    def __init__(
        self,
        path_parameters: ArgOrCallable[PathParameters, TestCaseType],
        payloads: ArgOrCallable[Payloads, TestCaseType],
        auth_headers: ArgOrCallable[AuthHeaders, TestCaseType] = None,
    ) -> None:
        super().__init__(path_parameters, payloads, auth_headers)
        self.request_composer.request_method = self.request_partial_update_model

    def request_partial_update_model(
        self,
        path_parameters: dict,
        query_parameters: dict,
        auth_headers: dict,
        payload: dict,
    ) -> HttpResponse:
        path = "/" + self.test_model_view_set.base_path + self.model_view.get_path()
        return self.test_model_view_set.client_class().patch(
            path=path.format(**path_parameters),
            data=payload,
            content_type="application/json",
            **auth_headers,
        )


class PartialUpdateModelViewTest(TestPartialUpdateModelView):
    def __init__(self, *args, **kwargs):  # pragma: no cover
        logger.warning(
            f"{PartialUpdateModelViewTest.__name__} is deprecated, use {TestPartialUpdateModelView.__name__} instead",
            DeprecationWarning,
        )
        super().__init__(*args, **kwargs)
