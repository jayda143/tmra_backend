from rest_framework import viewsets
from .models import Employee, User, Training, Budget, Trainees, IndividualPoints, EmployeeEvaluation, Department, RolesResponsibilities, Schedule,EmploymentDetails, EmploymentHistory, UserLogs, AccountSettings
from .serializers import EmployeeSerializers, UserSerializers, TrainingSerializers, BudgetSerializers, TraineesSerializers, IndividualPointsSerializers, EmployeeEvaluationSerializers, DepartmentSerializers, RolesResponsibilitiesSerializers, ScheduleSerializers, EmploymentDetailsSerializers, EmploymentHistorySerializers, UserLogsSerializers, AccountSettingsSerializers

class EmployeeView(viewsets.ModelViewSet):
    serializer_class = EmployeeSerializers

    def get_queryset(self):
        queryset = Employee.objects.all()
        firstname = self.request.query_params.get('firstname', None)
        if firstname:
            queryset = queryset.filter(firstname=firstname)
        return queryset

class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializers
    
    def get_queryset(self):
        queryset = User.objects.all()
        token = self.request.query_params.get('id', None)
        if token:
            queryset = queryset.filter(token=token)
        return queryset

class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all().order_by('-date')
    serializer_class = TrainingSerializers

class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializers

    def get_queryset(self):
        queryset = Budget.objects.all().order_by('-date')
        trainingid = self.request.query_params.get('id', None)
        if trainingid:
            queryset = queryset.filter(training=trainingid)
        return queryset

class TraineesView(viewsets.ModelViewSet):
    serializer_class = TraineesSerializers

    def get_queryset(self):
        queryset = Trainees.objects.all()
        trainingid = self.request.query_params.get('id', None)
        if trainingid:
            queryset = queryset.filter(training=trainingid)
        return queryset

class IndividualPointsView(viewsets.ModelViewSet):
    serializer_class = IndividualPointsSerializers

    def get_queryset(self):
        queryset = IndividualPoints.objects.all()
        employeeid = self.request.query_params.get('id', None)
        if employeeid:
            queryset = queryset.filter(employee_id=employeeid)
        return queryset
       
class EmployeeEvaluationView(viewsets.ModelViewSet):
    serializer_class = EmployeeEvaluationSerializers

    def get_queryset(self):
        queryset = EmployeeEvaluation.objects.all()
        employeeid = self.request.query_params.get('id', None)
        if employeeid:
            queryset = queryset.filter(employee_id=employeeid)
        return queryset

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

class RolesResponsibilitiesView(viewsets.ModelViewSet):
    serializer_class = RolesResponsibilitiesSerializers

    def get_queryset(self):
        queryset = RolesResponsibilities.objects.all()
        position_id = self.request.query_params.get('id', None)
        if position_id:
            queryset = queryset.filter(id=position_id)
        return queryset


class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers

class EmploymentDetailsView(viewsets.ModelViewSet):
    serializer_class = EmploymentDetailsSerializers

    def get_queryset(self):
        queryset = EmploymentDetails.objects.all()
        employee_id = self.request.query_params.get('id', None)
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        return queryset

class EmploymentHistoryView(viewsets.ModelViewSet):
    serializer_class = EmploymentHistorySerializers

    def get_queryset(self):
        queryset = EmploymentHistory.objects.all().order_by('-id')
        employee_id = self.request.query_params.get('id', None)
        if employee_id:
            queryset = queryset.filter(employee_id=employee_id)
        return queryset

class UserLogsView(viewsets.ModelViewSet):
    serializer_class = UserLogsSerializers

    def get_queryset(self):
        queryset = UserLogs.objects.all()
        user_id = self.request.query_params.get('id', None)
        if user_id:
            queryset = queryset.filter(user_id=user_id)
        return queryset

class AccountSettingsView(viewsets.ModelViewSet):
    serializer_class = AccountSettingsSerializers

    def get_queryset(self):
        queryset = AccountSettings.objects.all()
        user_type = self.request.query_params.get('id', None)
        if user_type:
            queryset = queryset.filter(user_type=user_type)
        return queryset