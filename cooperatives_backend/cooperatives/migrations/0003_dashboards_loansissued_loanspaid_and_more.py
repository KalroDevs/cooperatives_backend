# Generated by Django 5.0.7 on 2024-10-20 10:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cooperatives', '0002_remove_cooperative_contact_person_other_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('role', models.CharField(blank=True, max_length=100, null=True)),
                ('link', models.CharField(blank=True, max_length=100, null=True)),
                ('publish', models.BooleanField(blank=True, default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoansIssued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_code', models.CharField(max_length=100)),
                ('sacco_code', models.CharField(max_length=100)),
                ('date_issued', models.DateField(blank=True, null=True)),
                ('amount_issued', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('org_loan_type_code', models.CharField(blank=True, max_length=100, null=True)),
                ('terms_days', models.IntegerField(blank=True, null=True)),
                ('expected_payment_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LoansPaid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_code', models.CharField(blank=True, max_length=100, null=True)),
                ('date_paid', models.DateField(blank=True, null=True)),
                ('principal_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('amount_paid', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('par', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='cooperative',
            name='asp_organization_code',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='common_bond',
            field=models.CharField(blank=True, choices=[('Agricultural Production', 'Agricultural Production'), ('Common Employer', 'Common Employer'), ('Fisheries', 'Fisheries'), ('Interest in Real Estate and Housing', 'Interest in Real Estate and Housing'), ('Interest in the Transport Sector', 'Interest in the Transport Sector'), ('Livestock Production', 'Livestock Production'), ('Marketing', 'Marketing'), ('Same Locality', 'Same Locality'), ('Shared Economic Interest', 'Shared Economic Interest'), ('Shared Faith', 'Shared Faith'), ('other', 'Shared Faith')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='cooperative',
            name='organization_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name='AmountsDisbursedToOrganisations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_disbursed', models.DateField(blank=True, null=True)),
                ('date_recieved', models.DateField(blank=True, null=True)),
                ('amount_received', models.DecimalField(decimal_places=2, max_digits=10)),
                ('financial_year', models.CharField(blank=True, choices=[('2020/2021', '2020/2021'), ('2021/2022', '2021/2022'), ('2022/2023', '2022/2023'), ('2023/2024', '2023/2024'), ('2024/2025', '2024/2025'), ('2025/2026', '2025/2026'), ('2027/2028', '2027/2028'), ('2029/2030', '2029/2030')], max_length=255, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperative')),
            ],
        ),
        migrations.CreateModel(
            name='BookKeeperRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_keeper_name', models.CharField(blank=True, max_length=100, null=True)),
                ('book_keeper_phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('book_keeper_national_id', models.CharField(blank=True, null=True)),
                ('book_keeper_highest_education_qualification', models.CharField(blank=True, choices=[('PhD', 'PhD'), ('Masters', 'Masters'), ('Bachelor', 'Bachelor'), ('Higher Diploma/Diploma/Certificate', 'Higher Diploma/Diploma/Certificate'), ('Craft Certificate', 'Craft Certificate'), ('Secondary Education', 'Secondary Education'), ('Primary Education', 'Primary Education')], max_length=255, null=True)),
                ('course_considered_for_qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('is_contract_issued', models.BooleanField(blank=True, default=False, null=True)),
                ('contracting_term_period_months', models.IntegerField(blank=True, null=True)),
                ('salary_range', models.CharField(blank=True, choices=[('Below 5000', 'Below 5000'), ('5000-10000', '5000 – 10,000'), ('10001-15000', '10,001 – 15,000'), ('15001-20000', '15,001 – 20,000'), ('20001-25000', '20,001 – 25,000'), ('25001-50000', '25,001 – 50,000'), ('50001-100000', '50,001 – 100,000'), ('100001-150000', '100,001 – 150,000'), ('150000+', '150,000+')], default='5000-10000', max_length=20, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperative')),
            ],
        ),
        migrations.CreateModel(
            name='LoanType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_loan_type_code', models.CharField(max_length=100)),
                ('loan_type_code', models.CharField(blank=True, max_length=100, null=True)),
                ('conventional_name', models.CharField(blank=True, max_length=100, null=True)),
                ('standardized_name', models.CharField(blank=True, max_length=100, null=True)),
                ('main_target_value_chain', models.CharField(blank=True, max_length=100, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperative')),
            ],
        ),
        migrations.CreateModel(
            name='MemberRegister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_registration', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('pnts', 'Prefer Not to Say')], max_length=100, null=True)),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('id_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('year_of_birth', models.IntegerField(blank=True, null=True)),
                ('member_shares_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('member_registration_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_committee_member', models.BooleanField(blank=True, default=False, null=True)),
                ('is_active', models.BooleanField(blank=True, default=False, null=True)),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperative')),
            ],
        ),
        migrations.CreateModel(
            name='MemberSavings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_savings', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.memberregister')),
                ('organization', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooperatives.cooperative')),
            ],
        ),
    ]