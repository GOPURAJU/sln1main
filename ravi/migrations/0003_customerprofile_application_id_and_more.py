# Generated by Django 5.0.7 on 2024-10-05 03:06

import django.db.models.deletion
import ravi.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ravi', '0002_remove_customerprofile_application_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='application_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='application_loan_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='dsaref_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='empref_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='franrefCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customerprofile',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='application_id',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='application_loan_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='created_at',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='dsaref_code',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='empref_code',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='franrefCode',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='personaldetail',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='applicationverification',
            name='personal_detail',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='applicationverification', to='ravi.personaldetail'),
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='co_applicant_age',
            field=models.DateField(max_length=30, validators=[ravi.models.validate_age]),
        ),
        migrations.AlterField(
            model_name='homebasicdetail',
            name='phone_number',
            field=models.BigIntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pldisbursementdetails',
            name='verification',
            field=models.OneToOneField(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, related_name='disbursementdetail', to='ravi.personaldetail'),
        ),
    ]
