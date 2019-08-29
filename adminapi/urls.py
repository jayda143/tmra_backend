from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employee', views.EmployeeView,basename='employee')
router.register('users', views.UserView, basename='user')
router.register('employmentdetails', views.EmploymentDetailsView, basename='employmentdetails')
router.register('employmenthistory', views.EmploymentHistoryView, basename='employmenthistory')
router.register('training', views.TrainingView, basename='training')
router.register('budgets', views.BudgetView, basename='budget')
router.register('trainees', views.TraineesView, basename='trainees')
router.register('individualpoints', views.IndividualPointsView, basename='individualpoints')
router.register('employeeevaluation', views.EmployeeEvaluationView, basename='employeeevaluation')
router.register('department', views.DepartmentView)
router.register('positionresponsibilities', views.RolesResponsibilitiesView, basename='rolesresponsibilities')
router.register('schedule', views.ScheduleView)
router.register('userlogs', views.UserLogsView, basename='userlogs')
router.register('accountsettings', views.AccountSettingsView, basename="accountsettings")


urlpatterns = [
path('', include(router.urls)),
]