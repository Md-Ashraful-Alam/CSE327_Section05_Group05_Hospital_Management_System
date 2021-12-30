# Generated by Django 3.2.8 on 2021-12-28 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('appointment_id', models.CharField(db_column='Appointment_Id', max_length=15, primary_key=True, serialize=False)),
                ('patient_id', models.CharField(max_length=10)),
                ('doctor_id', models.CharField(max_length=10)),
                ('appointment_date', models.DateTimeField(blank=True, db_column='Appointment_Date', null=True)),
            ],
            options={
                'db_table': 'appointment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('bed_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('bed_type', models.CharField(db_column='Bed_Type', max_length=15)),
                ('vacancy', models.CharField(db_column='Vacancy', max_length=1)),
                ('bed_charge', models.IntegerField(db_column='Bed_Charge')),
            ],
            options={
                'db_table': 'bed',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='BloodDonate',
            fields=[
                ('patient_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=5)),
                ('contact_num', models.CharField(blank=True, max_length=11, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('need_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'blood_donate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('doctorid', models.CharField(db_column='Doctorid', max_length=6, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('doctor_name', models.CharField(db_column='Doctor_Name', max_length=15)),
                ('contact_num', models.CharField(max_length=11)),
                ('email', models.CharField(max_length=30)),
                ('meet_link', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'doctor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('medicine_id', models.CharField(db_column='Medicine Id', max_length=15, primary_key=True, serialize=False)),
                ('medicine_name', models.CharField(db_column='Medicine Name', max_length=20)),
                ('patient_id', models.CharField(max_length=10)),
                ('expired_date', models.DateTimeField(db_column='Expired Date')),
                ('price', models.SmallIntegerField(db_column='Price')),
            ],
            options={
                'db_table': 'medicine',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Nurse',
            fields=[
                ('nurse_id', models.CharField(db_column='Nurse_ID', max_length=6, primary_key=True, serialize=False)),
                ('nurse_name', models.CharField(db_column='Nurse_Name', max_length=15)),
                ('floor_no', models.IntegerField(db_column='Floor_No')),
                ('bed_no', models.CharField(db_column='Bed_No', max_length=30)),
            ],
            options={
                'db_table': 'nurse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='OrganDonate',
            fields=[
                ('patient_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('user_id', models.CharField(max_length=10)),
                ('blood_group', models.CharField(max_length=5)),
                ('contact_num', models.CharField(blank=True, max_length=11, null=True)),
                ('location', models.CharField(blank=True, max_length=20, null=True)),
                ('need_date', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'organ_donate',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('patient_id', models.CharField(db_column='Patient_Id', max_length=5, primary_key=True, serialize=False)),
                ('patient_name', models.CharField(db_column='Patient_Name', max_length=20)),
                ('contact_num', models.CharField(max_length=11)),
                ('age', models.IntegerField(db_column='Age')),
                ('address', models.CharField(db_column='Address', max_length=50)),
                ('patient_blood_group', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'patient',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient_id', models.CharField(max_length=10)),
                ('story_date', models.DateField()),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'story',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('test_id', models.CharField(db_column='Test_Id', max_length=6, primary_key=True, serialize=False)),
                ('patient_id', models.CharField(db_column='Patient_ID', max_length=5)),
                ('test_charge', models.IntegerField()),
            ],
            options={
                'db_table': 'test',
                'managed': False,
            },
        ),
    ]
