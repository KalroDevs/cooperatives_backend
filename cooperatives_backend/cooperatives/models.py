from django.db import models
from users.models import County, SubCounty, Ward


class Cooperative(models.Model):
    REG_CHOICES = (
        ('registered', 'Registered'),
        ('not', 'Not Registered'),
    )
    BOND_CHOICES = (
        ('Agricultural Production', 'Agricultural Production'),
        ('Common Employer', 'Common Employer'),
        ('Fisheries', 'Fisheries'),
        ('Interest in Real Estate and Housing', 'Interest in Real Estate and Housing'),
        ('Interest in the Transport Sector', 'Interest in the Transport Sector'),
        ('Livestock Production', 'Livestock Production'),
        ('Marketing', 'Marketing'),
        ('Same Locality', 'Same Locality'),
        ('Shared Economic Interest', 'Shared Economic Interest'),
        ('Shared Faith', 'Shared Faith'),
        ('other', 'Shared Faith'),

    )
    ROLE_CHOICES = (
        ('chairman', 'Chairman'),
        ('secretary', 'Secretary'),
        ('treasurer', 'Treasurer'),
        ('bookkeeper', 'Book Keeper'),
        ('other', 'Other'),

    )

    ORGANIZATION_TYPE_CHOICES = (
        ('sacco', 'SACCO'),
        ('fpo', 'FPO'),
        ('other', 'Other'),

    )
    # Location Information
    secretariate_county = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True,)
    secretariate_sub_county = models.ForeignKey(SubCounty, on_delete=models.CASCADE, blank=True, null=True,)
    secretariate_ward = models.ForeignKey(Ward, on_delete=models.CASCADE, blank=True, null=True,)
    gps_latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='GPS Coordinates Latitude', null=True, blank=True)
    gps_longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='GPS Coordinates Longitude', null=True, blank=True)
    gps_altitude = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='GPS Coordinates Altitude', null=True, blank=True)
    gps_precision = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='GPS Coordinates Precision', null=True, blank=True)

    # General Information
    cooperative_photo = models.ImageField(upload_to='cooperatives/photos/', null=True, blank=True)
    organization_type = models.CharField(max_length=255, choices=ORGANIZATION_TYPE_CHOICES, blank=True, null=True,)
    registration_status = models.CharField(max_length=255, choices=REG_CHOICES, blank=True, null=True,)
    registration_number = models.CharField(max_length=25, unique=True)
    registration_date = models.DateField(null=True, blank=True)
    registered_office_address = models.CharField(max_length=255,  null=True, blank=True)
    organization_name = models.CharField(max_length=255, unique=True)
    asp_organization_code = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_automated = models.BooleanField(default=False, null=True, blank=True)
    common_bond = models.CharField(max_length=255, choices=BOND_CHOICES, blank=True, null=True,)

    # Contact Information
    contact_person_name = models.CharField(max_length=255, verbose_name="Contact Person Name", null=True, blank=True)
    contact_person_role = models.CharField(max_length=255, choices=ROLE_CHOICES, blank=True, null=True,)
    contact_person_mobile = models.CharField(max_length=15, verbose_name="Contact Person Mobile Number", null=True, blank=True)
    contact_person_email = models.EmailField(verbose_name="Contact Person Email Address", null=True, blank=True)

    # Membership Information
    current_total_membership = models.PositiveIntegerField(verbose_name="Membership", null=True, blank=True)
    previous_year_membership = models.PositiveIntegerField(verbose_name="Previous Year Membership", null=True, blank=True)
    institutional_membership = models.PositiveIntegerField(verbose_name="Institutional/Corporate Membership", null=True, blank=True)
    male_membership = models.PositiveIntegerField(verbose_name="Male Membership", null=True, blank=True)
    female_membership = models.PositiveIntegerField(verbose_name="Female Membership", null=True, blank=True)
    male_youth_membership = models.PositiveIntegerField(verbose_name="Male Youth Membership", null=True, blank=True)
    female_youth_membership = models.PositiveIntegerField(verbose_name="Female Youth Membership", null=True, blank=True)
    indigenous_membership = models.PositiveIntegerField(verbose_name="Indigenous Person Membership", null=True, blank=True)

    # Affiliated Groups (CIGs, VMGs)
    cig_federated_count = models.PositiveIntegerField(verbose_name="No. of CIGs Federated", null=True, blank=True)
    cig_membership_count = models.PositiveIntegerField(verbose_name="CIG Members", null=True, blank=True)
    vmg_federated_count = models.PositiveIntegerField(verbose_name="No. of VMGs Federated", null=True, blank=True)
    vmg_membership_count = models.PositiveIntegerField(verbose_name="VMG Members", null=True, blank=True)

    def __str__(self):
        return self.organization_name




class BookKeeperRegister(models.Model):
    EDUCATION_CHOICES = (
        ('PhD', 'PhD'),
        ('Masters', 'Masters'),
        ('Bachelor', 'Bachelor'),
        ('Higher Diploma/Diploma/Certificate', 'Higher Diploma/Diploma/Certificate'), 
        ('Craft Certificate', 'Craft Certificate'),
        ('Secondary Education', 'Secondary Education'), 
        ('Primary Education', 'Primary Education'),  
    )
   
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,)
    book_keeper_name = models.CharField(max_length=100, blank=True, null=True)
    book_keeper_phone_number = models.CharField(max_length=15, blank=True, null=True)
    book_keeper_national_id = models.CharField(max_length=20,blank=True, null=True)
    book_keeper_highest_education_qualification = models.CharField(max_length=255, choices=EDUCATION_CHOICES, blank=True, null=True,)
    course_considered_for_qualification = models.CharField(max_length=255, blank=True, null=True)
    is_contract_issued = models.BooleanField(default=False, blank=True, null=True)
    contracting_term_period_months = models.IntegerField(blank=True, null=True)
    salary_range = models.CharField(
        max_length=20,
        choices=[
            ('Below 5000', 'Below 5,000'),
            ('5000-10000', '5,000 – 10,000'),
            ('10001-15000', '10,001 – 15,000'),
            ('15001-20000', '15,001 – 20,000'),
            ('20001-25000', '20,001 – 25,000'),
            ('25001-50000', '25,001 – 50,000'),
            ('50001-100000', '50,001 – 100,000'),
            ('100001-150000', '100,001 – 150,000'),
            ('150000+', '150,000+'),
        ],
        default='5000-10000',
        blank=True, null=True
    )

    def __str__(self):
        return self.book_keeper_name

class AmountsDisbursedToOrganisations(models.Model):
    FINANCIAL_YEAR_CHOICES = (
        ('2020/2021', '2020/2021'),
        ('2021/2022', '2021/2022'),
        ('2022/2023', '2022/2023'),
        ('2023/2024', '2023/2024'),
        ('2024/2025', '2024/2025'),
        ('2025/2026', '2025/2026'),
        ('2027/2028', '2027/2028'),
        ('2029/2030', '2029/2030'),

    )
    GRANT_TYPE_CHOICES = (
        ('Inclusion Grant', 'Inclusion Grant'),
        ('Matching Grant', 'Matching Grant'),
    )
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,)
    grant_type = models.CharField(max_length=255, choices=GRANT_TYPE_CHOICES, blank=True, null=True,)
    date_disbursed = models.DateField(blank=True, null=True)
    date_recieved = models.DateField(blank=True, null=True)
    amount_received = models.DecimalField(max_digits=10, decimal_places=2)
    financial_year = models.CharField(max_length=255, choices=FINANCIAL_YEAR_CHOICES, blank=True, null=True,)
 
    def __str__(self):
        return self.organization.organization_name

class MemberRegister(models.Model):
    GEN_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('pnts', 'Prefer Not to Say'), 
    )
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,)
    date_of_registration = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=100, choices=GEN_CHOICES, blank=True, null=True,)
    full_name = models.CharField(max_length=100, blank=True, null=True)
    id_number = models.BigIntegerField(blank=True, null=True, unique=True)
    year_of_birth = models.IntegerField(blank=True, null=True)
    member_shares_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    member_registration_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_committee_member = models.BooleanField(default=False, blank=True, null=True)
    is_active = models.BooleanField(default=False, blank=True, null=True)

    def __str__(self):
        return self.full_name

class MemberSavings(models.Model):
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,) 
    member=models.ForeignKey(MemberRegister, on_delete=models.CASCADE, blank=True, null=True,)    
    member_savings = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    def __str__(self):
        return f"Member: {self.member}, Savings: {self.member_savings}"

class LoanType(models.Model):
    org_loan_type_code = models.CharField(max_length=100)
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,) 
    loan_type_code = models.CharField(max_length=100, blank=True, null=True)
    conventional_name = models.CharField(max_length=100, blank=True, null=True)
    standardized_name = models.CharField(max_length=100, blank=True, null=True)
    main_target_value_chain = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.conventional_name

class LoansIssued(models.Model):
    loan_code = models.CharField(max_length=100)
    organization=models.ForeignKey(Cooperative, on_delete=models.CASCADE, blank=True, null=True,) 
    date_issued = models.DateField(blank=True, null=True)
    amount_issued = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    org_loan_type_code = models.CharField(max_length=100, blank=True, null=True)
    terms_days = models.IntegerField(blank=True, null=True)
    expected_payment_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.loan_code

class LoansPaid(models.Model):
    loan_code = models.CharField(max_length=100, blank=True, null=True)
    date_paid = models.DateField(blank=True, null=True)
    principal_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    par = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.loan_code


class Dashboards(models.Model):
    ROLE_CHOICES = (
        ('admin', 'Administrator'),
        ('national', 'National'),
        ('county', 'County'),        
        ('sp', 'Service Provider'),
        ('fa', 'Funding Agency'),
        ('os', 'Other Stakeholders')
    )
    title = models.CharField(max_length=255, unique=True, blank=True, null=True)
    role = models.CharField(max_length=255, choices=ROLE_CHOICES, blank=True, null=True,)
    link = models.CharField(max_length=512, blank=True, null=True)
    scope = models.ForeignKey(County, on_delete=models.CASCADE, blank=True, null=True,)
    publish = models.BooleanField(default=True, blank=True, null=True)
    def __str__(self):
        return self.link