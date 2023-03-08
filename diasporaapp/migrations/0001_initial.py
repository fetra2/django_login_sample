# Generated by Django 4.0.8 on 2023-03-07 13:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agence',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('agc_nom', models.CharField(max_length=45, null=True)),
                ('agc_codique', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Authentification',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Titulaire_Tit_id', models.PositiveIntegerField()),
                ('auth_utilisateur', models.CharField(max_length=20, null=True)),
                ('auth_pass', models.CharField(default='P@ssw0rd', max_length=20)),
                ('auth_mail', models.CharField(max_length=100, null=True)),
                ('date_connexion', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avoir_annuel',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Compte_cpte_id', models.PositiveIntegerField()),
                ('avoir_annee', models.DateTimeField(null=True)),
                ('avoir_montant', models.FloatField(null=True)),
                ('avoir_interet', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('cpte_num', models.CharField(max_length=20)),
                ('cpte_type', models.CharField(max_length=20, null=True)),
                ('cpte_date_ouverture', models.DateTimeField(null=True)),
                ('cpte_date_cloture', models.DateTimeField(null=True)),
                ('cpte_ref_cloture', models.CharField(max_length=20, null=True)),
                ('cpte_solde', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Demandeur',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Dem_nom', models.CharField(max_length=255, null=True)),
                ('Dem_prenom', models.CharField(max_length=255, null=True)),
                ('Dem_date_nais', models.DateTimeField(null=True)),
                ('Dem_lieu_nais', models.CharField(max_length=255, null=True)),
                ('Dem_nationalite', models.CharField(max_length=45, null=True)),
                ('Dem_profession', models.CharField(max_length=45, null=True)),
                ('Dem_adr_actuelle', models.CharField(max_length=255, null=True)),
                ('Dem_adr_mg', models.CharField(max_length=255, null=True)),
                ('Dem_home_tel', models.CharField(max_length=20, null=True)),
                ('Dem_mob_tel', models.CharField(max_length=20, null=True)),
                ('Dem_email', models.CharField(max_length=100, null=True)),
                ('Dem_sexe', models.CharField(max_length=20, null=True)),
                ('Dem_sit_fam', models.CharField(max_length=20, null=True)),
                ('Dem_type_piece', models.CharField(max_length=20, null=True)),
                ('Dem_num_piece', models.CharField(max_length=20, null=True)),
                ('Dem_date_piece', models.DateTimeField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dossier',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('Compte_cpte_id', models.PositiveIntegerField()),
                ('Demandeur_Dem_id', models.PositiveIntegerField()),
                ('dos_cin', models.CharField(max_length=255, null=True)),
                ('dos_photo', models.CharField(max_length=255, null=True)),
                ('dos_residence', models.DateTimeField(null=True)),
                ('dos_copie', models.CharField(max_length=255, null=True)),
                ('dos_act_tut', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Titulaire',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Tit_nom', models.CharField(max_length=255, null=True)),
                ('Tit_prenom', models.CharField(max_length=255, null=True)),
                ('Tit_date_nais', models.DateTimeField(null=True)),
                ('Tit_lieu_nais', models.CharField(max_length=255, null=True)),
                ('Tit_nationalite', models.CharField(max_length=45, null=True)),
                ('Tit_profession', models.CharField(max_length=45, null=True)),
                ('Tit_pays', models.CharField(max_length=45, null=True)),
                ('Tit_adr_actuelle', models.CharField(max_length=255, null=True)),
                ('Tit_adr_mg', models.CharField(max_length=255, null=True)),
                ('Tit_home_tel', models.CharField(max_length=20, null=True)),
                ('Tit_mob_tel', models.CharField(max_length=20, null=True)),
                ('Tit_email', models.CharField(max_length=100, null=True)),
                ('Tit_sexe', models.CharField(max_length=20, null=True)),
                ('Tit_sit_fam', models.CharField(max_length=20, null=True)),
                ('Tit_type_piece', models.CharField(max_length=20, null=True)),
                ('Tit_num_piece', models.CharField(max_length=20, null=True)),
                ('Tit_date_piece', models.DateTimeField(null=True)),
                ('Tit_agence', models.CharField(max_length=45, null=True)),
            ],
            options={
                'db_table': 'Titulaire',
            },
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('op_date', models.DateTimeField(null=True)),
                ('op_montant', models.IntegerField(null=True)),
                ('op_reference', models.CharField(max_length=45, null=True)),
                ('op_partenaire', models.CharField(max_length=45, null=True)),
                ('op_etat', models.CharField(max_length=45, null=True)),
                ('op_quinze', models.IntegerField(null=True)),
                ('op_interet', models.CharField(max_length=2, null=True)),
                ('op_annee', models.IntegerField(null=True)),
                ('Compte_cpte_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='diasporaapp.compte')),
            ],
        ),
    ]