from rest_framework import viewsets
from .models import Employee, User, Training, Budget, Trainees, IndividualPoints, EmployeeEvaluation, Department, RolesResponsibilities, Schedule,EmploymentDetails
from .serializers import EmployeeSerializers, UserSerializers, TrainingSerializers, BudgetSerializers, TraineesSerializers, IndividualPointsSerializers, EmployeeEvaluationSerializers, DepartmentSerializers, RolesResponsibilitiesSerializers, ScheduleSerializers, EmploymentDetailsSerializers

class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers

class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class TrainingView(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializers

class BudgetView(viewsets.ModelViewSet):
    serializer_class = BudgetSerializers

    def get_queryset(self):
        queryset = Budget.objects.all()
        trainingid = self.request.query_params.get('id', None)
        if trainingid:
            queryset = queryset.filter(training_name=trainingid)
        return queryset

class TraineesView(viewsets.ModelViewSet):
    serializer_class = TraineesSerializers

    def get_queryset(self):
        queryset = Trainees.objects.all()
        trainingid = self.request.query_params.get('id', None)
        if trainingid:
            queryset = queryset.filter(training_name=trainingid)
        return queryset
    
class IndividualPointsView(viewsets.ModelViewSet):
    queryset = IndividualPoints.objects.all()
    serializer_class = IndividualPointsSerializers

class EmployeeEvaluationView(viewsets.ModelViewSet):
    queryset = EmployeeEvaluation.objects.all()
    serializer_class = EmployeeEvaluationSerializers

class DepartmentView(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers

class RolesResponsibilitiesView(viewsets.ModelViewSet):
    queryset = RolesResponsibilities.objects.all()
    serializer_class = RolesResponsibilitiesSerializers

class ScheduleView(viewsets.ModelViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializers

class EmploymentDetailsView(viewsets.ModelViewSet):
    queryset = EmploymentDetails.objects.all()
    serializer_class = EmploymentDetailsSerializers