from django.db import models

# Create your models here.

class Agence(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    agc_nom = models.CharField(max_length=45, null=True)
    agc_codique = models.CharField(max_length=20, null=True)
    def __str__(self):
        return self.agc_codique

class Authentification(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    Titulaire_Tit_id = models.PositiveIntegerField()
    auth_utilisateur = models.CharField(max_length=20, null=True)
    auth_pass = models.CharField(max_length=20, default='P@ssw0rd')
    auth_mail = models.CharField(max_length=100, null=True)
    date_connexion = models.DateTimeField(null=True)
    def __str__(self):
        return self.auth_utilisateur    

class Avoir_annuel(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    Compte_cpte_id = models.PositiveIntegerField()
    avoir_annee = models.DateTimeField(null=True)
    avoir_montant = models.FloatField(null=True)
    avoir_interet = models.FloatField(null=True)
    def __str__(self):
        return self.avoir_montant

class Compte(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    cpte_num = models.CharField(max_length=20)
    cpte_type = models.CharField(max_length=20, null=True)
    cpte_date_ouverture = models.DateTimeField(null=True)
    cpte_date_cloture = models.DateTimeField(null=True)
    cpte_ref_cloture = models.CharField(max_length=20, null=True)
    cpte_solde = models.FloatField(null=True)
    def __str__(self):
        return self.cpte_num

class Demandeur(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    Dem_nom = models.CharField(max_length=255, null=True)
    Dem_prenom = models.CharField(max_length=255, null=True)
    Dem_date_nais = models.DateTimeField(null=True)
    Dem_lieu_nais = models.CharField(max_length=255, null=True)
    Dem_nationalite = models.CharField(max_length=45, null=True)
    Dem_profession = models.CharField(max_length=45, null=True)
    Dem_adr_actuelle = models.CharField(max_length=255, null=True)
    Dem_adr_mg = models.CharField(max_length=255, null=True)
    Dem_home_tel = models.CharField(max_length=20, null=True)
    Dem_mob_tel = models.CharField(max_length=20, null=True)
    Dem_email = models.CharField(max_length=100, null=True)
    Dem_sexe = models.CharField(max_length=20, null=True)
    Dem_sit_fam = models.CharField(max_length=20, null=True)
    Dem_type_piece = models.CharField(max_length=20, null=True)
    Dem_num_piece = models.CharField(max_length=20, null=True)
    Dem_date_piece = models.DateTimeField(null=True)
    def __str__(self):
        return self.Dem_nom

class Dossier(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    Compte_cpte_id = models.PositiveIntegerField()
    Demandeur_Dem_id = models.PositiveIntegerField()
    dos_cin = models.CharField(max_length=255, null=True)
    dos_photo = models.CharField(max_length=255, null=True)
    dos_residence = models.DateTimeField(null=True)
    dos_copie = models.CharField(max_length=255, null=True)
    dos_act_tut = models.CharField(max_length=255, null=True)
    def __str__(self):
        return self.id

class Titulaire(models.Model):
    id = models.AutoField(primary_key=True)
    Tit_nom = models.CharField(max_length=255, null=True)
    Tit_prenom = models.CharField(max_length=255, null=True)
    Tit_date_nais = models.DateTimeField(null=True)
    Tit_lieu_nais = models.CharField(max_length=255, null=True)
    Tit_nationalite = models.CharField(max_length=45, null=True)
    Tit_profession = models.CharField(max_length=45, null=True)
    Tit_pays = models.CharField(max_length=45, null=True)
    Tit_adr_actuelle = models.CharField(max_length=255, null=True)
    Tit_adr_mg = models.CharField(max_length=255, null=True)
    Tit_home_tel = models.CharField(max_length=20, null=True)
    Tit_mob_tel = models.CharField(max_length=20, null=True)
    Tit_email = models.CharField(max_length=100, null=True)
    Tit_sexe = models.CharField(max_length=20, null=True)
    Tit_sit_fam = models.CharField(max_length=20, null=True)
    Tit_type_piece = models.CharField(max_length=20, null=True)
    Tit_num_piece = models.CharField(max_length=20, null=True)
    Tit_date_piece = models.DateTimeField(null=True)
    Tit_agence = models.CharField(max_length=45, null=True)

    class Meta:
        db_table = "Titulaire"
    def __str__(self):
        return self.Tit_nom



class Operation(models.Model):
    id = models.IntegerField(primary_key=True)
    Compte_cpte_id = models.ForeignKey(Compte, on_delete=models.CASCADE)
    op_date = models.DateTimeField(null=True)
    op_montant = models.IntegerField(null=True)
    op_reference = models.CharField(max_length=45, null=True)
    op_partenaire = models.CharField(max_length=45, null=True)
    op_etat = models.CharField(max_length=45, null=True)
    op_quinze = models.IntegerField(null=True)
    op_interet = models.CharField(max_length=2, null=True)
    op_annee = models.IntegerField(null=True)    
    def __str__(self):
        return self.id

class Profession(models.Model):
    id = models.IntegerField(primary_key=True)
    profession = models.CharField(max_length=45, null=True)
    def __str__(self):
        return self.profession

class TypeCompte(models.Model):
    id = models.IntegerField(primary_key=True)
    typeCompte = models.CharField(max_length=45, null=True)
    def __str__(self):
        return self.typeCompte

class PieceJoint(models.Model):
    id = models.IntegerField(primary_key=True)
    RefDossier = models.CharField(max_length=45, null=True)
    PieceType = models.CharField(max_length=45, null=True)
    PieceTypeImg = models.CharField(max_length=45, null=True)
    PieceType1 = models.CharField(max_length=45, null=True)
    PieceTypeImg1 = models.CharField(max_length=45, null=True)
    DateCreation = models.DateField()
    def __str__(self):
        return self.PieceType

class PaysNationalite(models.Model):
    id = models.IntegerField(primary_key=True)
    pays = models.CharField(max_length=45, null=True)
    def __str__(self):
        return self.pays

class AgencePostal(models.Model):
    id = models.IntegerField(primary_key=True)
    Agence = models.CharField(max_length=45, null=True)
    Codique = models.CharField(max_length=45, null=True)
    def __str__(self):
        return self.Agence

class tbl_mois(models.Model):
    id = models.IntegerField(primary_key=True)
    mois_nom = models.CharField(max_length=45, null=True)
    mois_date_min = models.IntegerField(null=True)
    mois_date_max = models.IntegerField(null=True)
    mois_quinze = models.IntegerField(null=True)
    def __str__(self):
        return self.mois_nom

