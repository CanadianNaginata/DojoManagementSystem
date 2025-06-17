from django.db import models
from django.contrib.auth.models import User


class LoggableModel(models.Model):
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                   related_name="+")
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey(User, on_delete=models.PROTECT,
                                  related_name="+")

    class Meta:
        abstract = True

# Create your models here.
class Role(models.IntegerChoices): #Creating Enum for User (role)
    GUEST = 0, 'Guest'
    MEMBER = 1, 'Member'
    LEADER = 2, 'Leader'
    OFFICER = 3, 'Officer'
    ADMIN = 4, 'Admin'

class Gender(models.IntegerChoices): #Creating Enum for Member (gender)
    UNKNOWN = 0, 'Unknown'
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'
    OTHER = 3, 'Other'

class GenderCert(models.IntegerChoices): #Creating Enum for Member (gender_cert)
    UNKNOWN = 0, 'Unknown'
    MALE = 1, 'Male'
    FEMALE = 2, 'Female'

class Officer(models.IntegerChoices): #Creating Enum For Member (officer)
    REGULAR_MEMBER = 0, 'Regular Member'
    PRESIDENT = 1, 'President'
    VICE_PRESEIDENT = 2, 'Vice President'
    EXECUTIVE_SECRETARY = 3, 'Executive Secretary'
    MEMBERSHIP_SECRETARY = 4, 'Membership Secretary'
    TREASURER = 5, 'Treasurer'
    COMMUNITY = 6, 'Community'
    OTHERS = 10, 'Others'

class Probation(models.IntegerChoices): #Creating Enum for Dojo (probation)
    NO = 0, 'No'
    YES = 1, 'Yes'
    DID_NOT_APPLY_OFFICIALLY = 2, 'Did not apply officially'
    DENIED = 3, 'Denied'

class RankType(models.IntegerChoices): #Creating Enum for Rank (rank)
    KYU = 1, 'Kyu'
    DAN = 2, 'Dan'
    SHOGO = 3, 'Shogo'

class EnglishName(models.IntegerChoices): #Creating Enum for Rank (name_in_english)
    NO_RANK = 0, 'No Rank'
    SIX_KYU = 1, '6 Kyu'
    FIVE_KYU = 2, '5 Kyu'
    FOUR_KYU = 3, '4 Kyu'
    THREE_KYU = 4, '3 Kyu'
    TWO_KYU = 5, '2 Kyu'
    ONE_KYU = 6, '1 Kyu'
    ONE_DAN =7, '1 Dan'
    TWO_DAN = 8, '2 Dan'
    THREE_DAN = 9, '3 Dan'
    FOUR_DAN = 10, '4 Dan'
    FIVE_DAN = 11, '5 Dan'
    RENSHI = 12, 'Renshi'
    KYOSHI = 13, 'Kyoshi'
    HANSHI = 14, 'Hanshi'

class JapaneseName(models.IntegerChoices): #Creating Enum for Rank (name_in_japanese)
    NO_RANK = 0, '無級'
    SIX_KYU = 1, '六級'
    FIVE_KYU = 2, '五級'
    FOUR_KYU = 3, '四級'
    THREE_KYU = 4, '三級'
    TWO_KYU = 5, '二級'
    ONE_KYU = 6, '一級'
    ONE_DAN =7, '初段'
    TWO_DAN = 8, '二段'
    THREE_DAN = 9, '三段'
    FOUR_DAN = 10, '四段'
    FIVE_DAN = 11, '五段'
    RENSHI = 12, '錬士'
    KYOSHI = 13, '教士'
    HANSHI = 14, '範士'

class RegistraType(models.IntegerChoices): #Creating Enum for Registration (registration_type)
    INVALID = 0, 'Invalid'
    NEW = 1, 'New'
    RENEW = 2, 'Renew'

class Printed(models.IntegerChoices): #Creating Enum for Printed (printed)
    NOT_APPLICABLE = 0, 'Not Applicable'
    NOT_READY = 1, 'Not ready'
    READY_TO_PRINT = 2, 'Ready to print'
    PRINTED = 3, 'printed'
    GIVEN_TO_DOJO_LEADER = 4, "Given to dojo leader or regional leader"

class PrinedLanguage(models.IntegerChoices): #Creating Enum for Printed (printed_languages)
    UNKNOWN = 0, 'Unknown'
    ENGLISH = 1, 'English'
    FRENCH = 2, 'French'
    JAPANESE = 3, 'Japanese'
    OTHER = 4, 'Other'

class Dojo(LoggableModel):
    abbr = models.CharField(max_length=10)
    active = models.BooleanField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20)   # TODO: Make it a selection
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    probation = models.IntegerField()  # TODO: make selection
    approval_date = models.DateField(blank=True, null=True)
    contact_email = models.CharField(max_length=254)
    website = models.CharField(max_length=2048)
    notes = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')
    
    
class User(models.Model):
    sso_id= models.IntegerField()
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    role = models.IntegerField(
        choices=Role,
        default=Role.GUEST
    )

class Member(models.Model):
    member_code = models.CharField(max_length=12)
    active = models.BooleanField()
    active_status_change_history = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    known_name = models.CharField(max_length=100) # INSERT Firstname Lastname in the application
    name_in_japanese = models.CharField(max_length=100, blank=True)
    name_change_history = models.TextField(blank=True, null=True)
    gender = models.IntegerField(
        choices=Gender,
        default=Gender.UNKNOWN
    )
    gender_for_inf_cert = models.IntegerField(
        choices=GenderCert,
        default=GenderCert.UNKNOWN
    )
    gender_change_history = models.TextField(blank=True, null=True)
    sso_email = models.EmailField(max_length=254)
    contact_email = models.EmailField(max_length=254)
    dojo = models.ForeignKey('Dojo', on_delete=models.SET_NULL, null=True) #Does not make sense to do CASCADE
    current_rank = models.ForeignKey('Rank', on_delete=models.SET_NULL, null=True)
    last_cnf_cert_number = models.IntegerField()
    last_other_cert_number = models.IntegerField()
    last_inf_cert_number = models.IntegerField()
    date_of_birth = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20)  
    postal_code = models.CharField(max_length=20)
    phone_1 = models.CharField(max_length=20, blank=True, null=True)
    phone_2 = models.CharField(max_length=20, blank=True, null=True)
    phone_3 = models.CharField(max_length=20, blank=True, null=True)
    date_of_first_registration = models.DateField(blank=True, null=True)
    date_of_last_registration = models.DateField(blank=True, null=True)
    date_of_first_grading = models.DateField(blank=True, null=True)
    officers = models.IntegerField(
        choices=Officer,
        default=Officer.REGULAR_MEMBER
    )
    board_of_directors = models.BooleanField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')

class DojoLeader(models.Model):
    dojo = models.ForeignKey('Dojo', on_delete=models.CASCADE)
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')
   
class Rank(models.Model):
    rank = models.IntegerField(
        choices=RankType,
        default=RankType.KYU
    )
    name_in_english = models.IntegerField(
        choices=EnglishName,
        default=EnglishName.NO_RANK
    )
    name_in_japanese = models.IntegerField(
        choices=JapaneseName,
        default=JapaneseName.NO_RANK
    )
   
class Registration(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE)
    registration_date = models.DateField()
    dojo = models.ForeignKey('Dojo', on_delete=models.CASCADE)
    dojo_leader = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    registration_type = models.IntegerField(
        choices=RegistraType,
        default=RegistraType.INVALID
    )
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    reciept_number = models.CharField(max_length=20)
    notes_for_member = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')

class Grading(models.Model):
    event_name = models.CharField(max_length=50)
    grading_data = models.DateTimeField()
    location = models.TextField(max_length=255)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20)
    head_examiner_name = models.CharField(max_length=50)
    head_examiner_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    head_examiner_rank = models.ForeignKey("Rank", on_delete=models.CASCADE, related_name='+')
    second_examiner_name = models.CharField(max_length=50)
    second_examiner_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    second_examiner_rank = models.ForeignKey("Rank", on_delete=models.CASCADE, related_name='+')
    third_examiner_name = models.CharField(max_length=50)
    third_examiner_member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    third_examiner_rank = models.ForeignKey("Rank", on_delete=models.CASCADE, related_name='+')
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    reciept_number = models.CharField(max_length=20)
    notes_for_member = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')

class GradingResult(models.Model):
    member = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    dojo = models.ForeignKey('Dojo', on_delete=models.CASCADE, related_name='+')
    dojo_leader = models.ForeignKey('Member', on_delete=models.CASCADE)
    rank_requested = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='+')
    rank_granted = models.ForeignKey('Rank', on_delete=models.CASCADE, related_name='+')
    grading = models.ForeignKey('Grading', on_delete=models.CASCADE)
    cnf_cert_number = models.IntegerField()
    other_cert_number = models.IntegerField()
    other_cert_region = models.CharField(max_length=20)
    inf_cert_number = models.IntegerField()
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    receipt_number = models.CharField(max_length=20)
    printed = models.IntegerField(
        choices=Printed,
        default=Printed.NOT_APPLICABLE
    )
    given_to = models.ForeignKey('Member', on_delete=models.CASCADE, related_name='+')
    printed_language = models.IntegerField(
        choices=PrinedLanguage,
        default=PrinedLanguage.UNKNOWN
    )
    notes_user = models.TextField()
    notes = models.TextField()
    created_at = models.DateTimeField()
    created_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='created_by', related_name='+')
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey('User', on_delete=models.CASCADE, db_column='edited_by', related_name='+')
