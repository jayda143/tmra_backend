from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeView)
router.register('users', views.UserView)
router.register('training', views.TrainingView)
router.register('budgets', views.BudgetView, basename='budget')
router.register(r'trainees', views.TraineesView, basename='trainees')
router.register('individualpoints', views.IndividualPointsView)
router.register('employeeevaluation', views.EmployeeEvaluationView)
router.register('department', views.DepartmentView)
router.register('rolesresponsibilities', views.RolesResponsibilitiesView)
router.register('schedule', views.ScheduleView)
router.register('employmentdetails', views.EmploymentDetailsView)

urlpatterns = [
path('', include(router.urls)),
]