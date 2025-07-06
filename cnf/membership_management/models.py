from django.db import models
from django.contrib.auth.models import User


class LoggableModel(models.Model):
    created_at = models.DateTimeField()
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")
    edited_at = models.DateTimeField()
    edited_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name="+")

    class Meta:
        abstract = True

class Provinces(models.TextChoices):
    ALBERTA = "AB", "Alberta"
    BRITISH_COLUMBIA = "BC", "British Columbia"
    MANITOBA = "MB", "Manitoba"
    NEW_BRUNSWICK = "NB", "New Brunswick"
    NEWFOUNDLAND_AND_LABRADOR = "NL", "Newfoundland and Labrador"
    NOVA_SCOTIA = "NS", "Nova Scotia"
    ONTARIO = "ON", "Ontario"
    PRINCE_EDWARD_ISLAND = "PE", "Prince Edward Island"
    QUEBEC = "QC", "Quebec"
    SASKATCHEWAN = "SK", "Saskatchewan"
    NORTHWEST_TERRITORIES = "NT", "Northwest Territories"
    NUNAVUT = "NU", "Nunavut"
    YUKON = "YT", "Yukon"


# Create your models here.
class Role(models.IntegerChoices):  # Creating Enum for User (role)
    GUEST = 0, "Guest"
    MEMBER = 1, "Member"
    LEADER = 2, "Leader"
    OFFICER = 3, "Officer"
    ADMIN = 4, "Admin"


class Gender(models.IntegerChoices):  # Creating Enum for Member (gender)
    UNKNOWN = 0, "Unknown"
    MALE = 1, "Male"
    FEMALE = 2, "Female"
    OTHER = 3, "Other"


class GenderCert(models.IntegerChoices):  # Creating Enum for Member (gender_cert)
    UNKNOWN = 0, "Unknown"
    MALE = 1, "Male"
    FEMALE = 2, "Female"


class Officer(models.IntegerChoices):  # Creating Enum For Member (officer)
    REGULAR_MEMBER = 0, "Regular Member"
    PRESIDENT = 1, "President"
    VICE_PRESEIDENT = 2, "Vice President"
    EXECUTIVE_SECRETARY = 3, "Executive Secretary"
    MEMBERSHIP_SECRETARY = 4, "Membership Secretary"
    TREASURER = 5, "Treasurer"
    COMMUNITY = 6, "Community"
    OTHERS = 10, "Others"


class Probation(models.IntegerChoices):  # Creating Enum for Dojo (probation)
    NO = 0, "No"
    YES = 1, "Yes"
    DID_NOT_APPLY_OFFICIALLY = 2, "Did not apply officially"
    DENIED = 3, "Denied"


class Rank(models.IntegerChoices):
    NO_RANK = 0, "No Rank"
    SIX_KYU = 1, "6 Kyu"
    FIVE_KYU = 2, "5 Kyu"
    FOUR_KYU = 3, "4 Kyu"
    THREE_KYU = 4, "3 Kyu"
    TWO_KYU = 5, "2 Kyu"
    ONE_KYU = 6, "1 Kyu"
    ONE_DAN = 7, "1 Dan"
    TWO_DAN = 8, "2 Dan"
    THREE_DAN = 9, "3 Dan"
    FOUR_DAN = 10, "4 Dan"
    FIVE_DAN = 11, "5 Dan"
    RENSHI = 12, "Renshi"
    KYOSHI = 13, "Kyoshi"
    HANSHI = 14, "Hanshi"

    @property
    def japanese_name(self):
        if self == Rank.NO_RANK:
            return "無級"
        if self == Rank.SIX_KYU:
            return "六級"
        if self == Rank.FIVE_KYU:
            return "五級"
        if self == Rank.FOUR_KYU:
            return "四級"
        if self == Rank.THREE_KYU:
            return "三級"
        if self == Rank.TWO_KYU:
            return "二級"
        if self == Rank.ONE_KYU:
            return "一級"
        if self == Rank.ONE_DAN:
            return "初段"
        if self == Rank.TWO_DAN:
            return "二段"
        if self == Rank.THREE_DAN:
            return "三段"
        if self == Rank.FOUR_DAN:
            return "五段"
        if self == Rank.FIVE_DAN:
            return "五段"
        if self == Rank.RENSHI:
            return "錬士"
        if self == Rank.KYOSHI:
            return "教士"
        if self == Rank.HANSHI:
            return "範士"

    @property
    def type(self):
        if self <= Rank.ONE_KYU:
            return "Kyu"
        elif self < Rank.RENSHI:
            return "Dan"
        else:
            return "Shogo"


class RegistrationType(
    models.IntegerChoices
):  # Creating Enum for Registration (registration_type)
    INVALID = 0, "Invalid"
    NEW = 1, "New"
    RENEW = 2, "Renew"


class Printed(models.IntegerChoices):  # Creating Enum for Printed (printed)
    NOT_APPLICABLE = 0, "Not Applicable"
    NOT_READY = 1, "Not ready"
    READY_TO_PRINT = 2, "Ready to print"
    PRINTED = 3, "printed"
    GIVEN_TO_DOJO_LEADER = 4, "Given to dojo leader or regional leader"


class PrintedLanguage(
    models.IntegerChoices
):  # Creating Enum for Printed (printed_languages)
    UNKNOWN = 0, "Unknown"
    ENGLISH = 1, "English"
    FRENCH = 2, "French"
    JAPANESE = 3, "Japanese"
    OTHER = 4, "Other"


class Dojo(LoggableModel):
    abbr = models.CharField(max_length=10)
    active = models.BooleanField()
    address = models.TextField()
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20, choices=Provinces, default=Provinces.ALBERTA)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    probation = models.IntegerField(choices=Probation, default=Probation.YES)
    approval_date = models.DateField(blank=True, null=True)
    contact_email = models.CharField(max_length=254)
    website = models.CharField(max_length=2048)
    notes = models.TextField()


class Member(LoggableModel):
    member_code = models.CharField(max_length=12)
    active = models.BooleanField()
    active_status_change_history = models.TextField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    known_name = models.CharField(
        max_length=100
    )  # INSERT Firstname Lastname in the application
    name_in_japanese = models.CharField(max_length=100, blank=True)
    name_change_history = models.TextField(blank=True, null=True)
    gender = models.IntegerField(choices=Gender, default=Gender.UNKNOWN)
    gender_for_inf_cert = models.IntegerField(
        choices=GenderCert, default=GenderCert.UNKNOWN
    )
    gender_change_history = models.TextField(blank=True, null=True)
    sso_email = models.EmailField(max_length=254)
    contact_email = models.EmailField(max_length=254)
    dojo = models.ForeignKey(
        "Dojo", on_delete=models.SET_NULL, null=True
    )  # Does not make sense to do CASCADE
    current_rank = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
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
    officers = models.IntegerField(choices=Officer, default=Officer.REGULAR_MEMBER)
    board_of_directors = models.BooleanField()
    notes = models.TextField(blank=True, null=True)


class DojoLeader(LoggableModel):
    dojo = models.ForeignKey("Dojo", on_delete=models.CASCADE)
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()



class Registration(LoggableModel):
    member = models.ForeignKey("Member", on_delete=models.CASCADE)
    registration_date = models.DateField()
    dojo = models.ForeignKey("Dojo", on_delete=models.CASCADE)
    dojo_leader = models.ForeignKey(
        "Member", on_delete=models.CASCADE, related_name="+"
    )
    registration_type = models.IntegerField(
        choices=RegistrationType, default=RegistrationType.INVALID
    )
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    reciept_number = models.CharField(max_length=20)
    notes_for_member = models.TextField()
    notes = models.TextField()


class Grading(LoggableModel):
    event_name = models.CharField(max_length=50)
    grading_data = models.DateTimeField()
    location = models.TextField(max_length=255)
    city = models.CharField(max_length=30)
    province = models.CharField(max_length=20)
    head_examiner_name = models.CharField(max_length=50)
    head_examiner_member = models.ForeignKey(
        "Member", on_delete=models.CASCADE, related_name="+"
    )
    head_examiner_rank = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
    second_examiner_name = models.CharField(max_length=50)
    second_examiner_member = models.ForeignKey(
        "Member", on_delete=models.CASCADE, related_name="+"
    )
    second_examiner_rank = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
    third_examiner_name = models.CharField(max_length=50)
    third_examiner_member = models.ForeignKey(
        "Member", on_delete=models.CASCADE, related_name="+"
    )
    third_examiner_rank = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    reciept_number = models.CharField(max_length=20)
    notes_for_member = models.TextField()
    notes = models.TextField()


class GradingResult(LoggableModel):
    member = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="+")
    dojo = models.ForeignKey("Dojo", on_delete=models.CASCADE, related_name="+")
    dojo_leader = models.ForeignKey("Member", on_delete=models.CASCADE)
    rank_requested = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
    rank_granted = models.IntegerField(
        choices=Rank, default=Rank.NO_RANK
    )
    grading = models.ForeignKey("Grading", on_delete=models.CASCADE)
    cnf_cert_number = models.IntegerField()
    other_cert_number = models.IntegerField()
    other_cert_region = models.CharField(max_length=20)
    inf_cert_number = models.IntegerField()
    fees_paid = models.DecimalField(max_digits=3, decimal_places=2)
    receipt_number = models.CharField(max_length=20)
    printed = models.IntegerField(choices=Printed, default=Printed.NOT_APPLICABLE)
    given_to = models.ForeignKey("Member", on_delete=models.CASCADE, related_name="+")
    printed_language = models.IntegerField(
        choices=PrintedLanguage, default=PrintedLanguage.UNKNOWN
    )
    notes_user = models.TextField()
    notes = models.TextField()
