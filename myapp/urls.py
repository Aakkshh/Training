from django.urls import path
from .views import (
    EmployeeListSet, EmployeeRetrieveSet, DepartmentViewSet, ProjectViewSet, DepartmentonEmployee,DepartmentRetrieveViewset,AddMemberToProjectView, StatusOfProject,StatusOngoingProjects,StatusEndedProjects,ProjectBudgetView,HighestSalaryView, SecondHighestSalaryByDepartmentView,TotalSalaryByDepartmentView
)

urlpatterns = [
    path('employees/', EmployeeListSet.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveSet.as_view(), name='employee-detail'),
    path('departments/', DepartmentViewSet.as_view(), name='department-list-create'),
    path('departments/<int:pk>/', DepartmentRetrieveViewset.as_view(), name='department-detail'),
    path('projects/', ProjectViewSet.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectViewSet.as_view(), name='project-detail'),
    path('projects/<int:pk>/add-member/', AddMemberToProjectView.as_view(), name='project-add-member'),
    path('projects/<int:pk>/update-status/', ProjectViewSet.as_view(), name='project-update-status'),
    path('employees/<int:pk>/Department',DepartmentonEmployee.as_view(), name='employee-on-department'),
    path('statusofproject/', StatusOfProject.as_view()),
    path('statusofproject/ongoing/', StatusOngoingProjects.as_view()),
    path('statusofproject/ended/', StatusEndedProjects.as_view()),
    path('projects/<int:pk>/budget/', ProjectBudgetView.as_view(), name='project-budget'),
    path('employees/highest-salary/', HighestSalaryView.as_view(), name='highest-salary'),
    path('employees/second-highest-salary/', SecondHighestSalaryByDepartmentView.as_view(), name='second-highest-salary'),
    path('projects/<int:pk>/budget/', ProjectBudgetView.as_view(), name='project-budget'),
    path('employees/total-salary/',TotalSalaryByDepartmentView.as_view(), name='highest-salary')
]
