from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *


# Register your models here.

@admin.register(Cooperative)
class CooperativesAdmin(ImportExportModelAdmin):
    list_display = ('organization_name', 'is_automated', 'secretariate_county', 'secretariate_ward')
    search_fields = ('organization_name', 'is_automated', 'secretariate_county', 'secretariate_ward')



@admin.register(BookKeeperRegister)
class BookKeeperRegisterAdmin(ImportExportModelAdmin):
    list_display = ('book_keeper_name', 'organization')
    search_fields = ('book_keeper_name', 'organization')


@admin.register(AmountsDisbursedToOrganisations)
class AmountsDisbursedToOrganisationsAdmin(ImportExportModelAdmin):
    list_display = ('organization', 'financial_year', 'amount_received')
    search_fields = ('organization', 'financial_year', 'amount_received')

@admin.register(MemberRegister)
class MemberRegisterAdmin(ImportExportModelAdmin):
    list_display = ('organization', 'full_name', 'gender')
    search_fields = ('organization', 'full_name', 'gender')

@admin.register(MemberSavings)
class MemberSavingsAdmin(ImportExportModelAdmin):
    list_display = ('organization', 'member', 'member_savings')
    search_fields = ('organization', 'member', 'member_savings')


@admin.register(LoanType)
class LoanTypeAdmin(ImportExportModelAdmin):
    list_display = ('organization', 'loan_type_code', 'standardized_name', 'main_target_value_chain')
    search_fields = ('organization', 'loan_type_code', 'standardized_name', 'main_target_value_chain')

@admin.register(LoansIssued)
class LoansIssuedAdmin(ImportExportModelAdmin):
    list_display = ('organization', 'date_issued', 'amount_issued')
    search_fields = ('organization', 'date_issued', 'amount_issued')


@admin.register(LoansPaid)
class LoansPaidAdmin(ImportExportModelAdmin):
    list_display = ('principal_amount', 'amount_paid', 'balance', 'par')
    search_fields = ('principal_amount', 'amount_paid', 'balance', 'par')

@admin.register(Dashboards)
class DashboardsAdmin(ImportExportModelAdmin):
    list_display = ('title', 'role', 'link')
    search_fields = ('title', 'role', 'link')
