from rest_framework import serializers
from .models import Employee,User,Training,Budget,Trainees,IndividualPoints,EmployeeEvaluation,Department,RolesResponsibilities,Schedule,EmploymentDetails

class EmployeeSerializers(serializers.ModelSerializer):
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
        fields = ('id','url','employee_id','user_type','password')

class TrainingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ('id','url','name','date','time','speaker','venue','training_duration')

class BudgetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Budget
        fields = ('id',
        'url',
        'training_name',
        'reference_number',
        'description',
        'date',
        'amount')

class TraineesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Trainees
        fields = ('id', 'url', 'training_name', 'employee_id')
        

class IndividualPointsSerializers(serializers.ModelSerializer):
    class Meta: 
        model = IndividualPoints
        fields = ('id',
        'url',
        'employee_id',
        'date',
        'points',
        'hours_classification',
        'hours_duration',
        'actual_hours')
        
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
    class Meta:
        model = EmploymentDetails
        fields = ('id',
        'url',
        'employee_id',
        'department_id',
        'date_employed',
        'date_effective',
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
        'schedule_id')