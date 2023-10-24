from example.models import Department, Employee
from example.schemas import DepartmentIn, DepartmentOut, EmployeeIn, EmployeeOut
from ninja import Router

from ninja_crud.views import CreateModelView, ListModelView
from ninja_crud.viewsets import BaseModelViewSet


class DepartmentViewSet(BaseModelViewSet):
    model_class = Department
    default_input_schema = DepartmentIn
    default_output_schema = DepartmentOut

    list_employees = ListModelView(
        detail=True,
        queryset_getter=lambda id: Employee.objects.filter(department_id=id),
        output_schema=EmployeeOut,
    )
    create_employee = CreateModelView(
        detail=True,
        model_factory=lambda id: Employee(department_id=id),
        input_schema=EmployeeIn,
        output_schema=EmployeeOut,
    )


router = Router()
DepartmentViewSet.register_routes(router)
