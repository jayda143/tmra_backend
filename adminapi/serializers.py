from rest_framework import serializers
from .models import Employee,User,Training,Budget,Trainees,IndividualPoints,EmployeeEvaluation,Department,RolesResponsibilities,Schedule,EmploymentDetails

class EmployeeSerializers(serializers.ModelSerializer):
    employeeID = serializers.IntegerField(required=False)
    
    class Meta:
         model = Employee
         fields = ('url',
         'id',
         'employeeID',
         'firstname',
         'middlename',
         'lastname',
         'address',
         'contact_number',
         'gender',
         'birthday',
         'age',
         'citizenship',
         'height',
         'weight',
         'blood_type',
         'status'
         )

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','url','employee_id','username','password','user_type')
        depth = 1

class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ('id','url','training','date','time','timeDisplay','speaker','venue','address')

class BudgetSerializers(serializers.ModelSerializer):
    training = TrainingSerializers(read_only=True)
    training_id = serializers.PrimaryKeyRelatedField(queryset=Training.objects.all(), source='training', write_only=False)
    class Meta:
        model = Budget
        fields = ('id','url','training_id','training','reference_number','description','date','amount')
       

class TraineesSerializers(serializers.ModelSerializer):
    training = TrainingSerializers(read_only=True)
    training_id = serializers.PrimaryKeyRelatedField(queryset=Training.objects.all(), source='training', write_only=False)
    employee = EmployeeSerializers(read_only=True)
    employee_id = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee', write_only=False)

    class Meta:
        model = Trainees
        fields = ('id', 'url','training_id','training','employee_id', 'employee')
  
class IndividualPointsSerializers(serializers.ModelSerializer):
    employee_id = EmployeeSerializers(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee_id', write_only=False)
    class Meta: 
        model = IndividualPoints
        fields = ('id',
        'url',
        'employee_id',
        'employee',
        'date',
        'paid',
        'notpaid_billable',
        'extra_workload',
        'management',
        'training',
        'admin',
        'investment',
        'non_billable',
        'sales',
        'points',)
        
        
class EmployeeEvaluationSerializers(serializers.ModelSerializer):
    class Meta:
        model = EmployeeEvaluation
        fields = ('id','url','employee_id','date','description','certified_by','performance_rating')

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id','url','department_name','classification')

class RolesResponsibilitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = RolesResponsibilities
        fields = ('id','url','position','responsibilities')

class ScheduleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ('id','url','login','breakout','breakin','logout')

class EmploymentDetailsSerializers(serializers.ModelSerializer):
    employee_id = EmployeeSerializers(read_only=True)
    employee = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), source='employee_id', write_only=False)
    department_id = DepartmentSerializers(read_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), source='department_id', write_only=False)
    roles_responsibilities_id = RolesResponsibilitiesSerializers(read_only=True)
    roles_responsibilities = serializers.PrimaryKeyRelatedField(queryset=RolesResponsibilities.objects.all(), source='roles_responsibilities_id', write_only=False)

    schedule_id = ScheduleSerializers(read_only=True)
    schedule = serializers.PrimaryKeyRelatedField(queryset=Schedule.objects.all(), source='schedule_id', write_only=False)
    class Meta:
        model = EmploymentDetails
        fields = ('id',
        'url',
        'employee_id',
        'employee',
        'department_id',
        'department',
        'date_employed',
        'date_effective',
        'roles_responsibilities_id',
        'roles_responsibilities',
        'quota',
        'salary_base',
        'basic_rate',
        'incentive',
        'challenge_quota',
        'designation',
        'assignment',
        'employee_type',
        'employment_status',
        'resignation_date',
        'end_of_contract',
        'remarks_for_resignation_termination',
        'flexi',
        'schedule_id',
        'schedule')
        