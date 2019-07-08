from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeView)
router.register('users', views.UserView, basename='user')
router.register('training', views.TrainingView)
router.register('budgets', views.BudgetView, basename='budget')
router.register('trainees', views.TraineesView, basename='trainees')
router.register('individualpoints', views.IndividualPointsView, basename='individualpoints')
router.register('employeeevaluation', views.EmployeeEvaluationView, basename='employeeevaluation')
router.register('department', views.DepartmentView)
router.register('rolesresponsibilities', views.RolesResponsibilitiesView)
router.register('schedule', views.ScheduleView)
router.register('employmentdetails', views.EmploymentDetailsView, basename='employmentdetails')

urlpatterns = [
path('', include(router.urls)),
]