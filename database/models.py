from django.db import models

# Create your models here.

class Ruolo(models.Model):
    id_ruolo = models.AutoField(primary_key=True)
    descrizione = models.CharField(max_length=50)
    def __unicode__(self):
        return self.descrizione
    class Meta:
        verbose_name_plural = 'Ruoli'

class Anagrafica(models.Model):
	id_anagrafica = models.AutoField(primary_key=True, max_length=10)
	id_ruolo = models.ForeignKey(Ruolo, null=True)
	nickname = models.CharField(max_length=20)
	nome = models.CharField(max_length=50)
	cognome = models.CharField(max_length=50)
	ragione_sociale = models.CharField(max_length=50, blank=True)
	indirizzo = models.CharField(max_length=100)
	cf = models.CharField(max_length=16, blank=True)
	pi = models.CharField(max_length=11, blank=True)
	telefono = models.CharField(max_length=20)
	cellulare = models.CharField(max_length=20)
	fax = models.CharField(max_length=20, blank=True)
	email = models.CharField(max_length=10, blank=True)
	sito = models.CharField(max_length=200)
	#imponibile = models.CharField(max_length=20)
	#imposta = models.CharField(max_length=5)
	#importo = models.CharField(max_length=20)
	def __unicode__(self):
	    return u"%s %s" % (self.nome, self.cognome)
	class Meta:
	    verbose_name_plural = "Anagrafiche"

class UnitaDiMisura(models.Model):
    id_misura = models.AutoField(primary_key=True)
    nome_unita = models.CharField(max_length=135)
    def __unicode__(self):
        return self.nome_unita
    class Meta:
        verbose_name = "UM"
        verbose_name_plural = "UM"
	
class Prodotto(models.Model):
	id = models.AutoField(primary_key=True)
	descrizione = models.CharField(max_length=30)
	unita_di_misura_id = models.ForeignKey(UnitaDiMisura, null=True, blank=True)
	quantita = models.CharField(max_length=10)
	def __unicode__(self):
	    return self.descrizione
	class Meta:
	    verbose_name_plural = "Prodotti"
	
class Ordine(models.Model):
    id_ordine = models.AutoField(primary_key=True, max_length=20)
    prodotto = models.ForeignKey(Prodotto)
    cliente = models.ForeignKey(Anagrafica)
    def __unicode__(self):
	    return u"Ordine n.%s di %s" % (self.id_ordine, self.cliente)
    class Meta:
        verbose_name_plural = "Ordini"

class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nome_categoria = models.CharField(max_length=135)   
    def __unicode__(self):
        return self.nome_categoria
    class Meta:
        verbose_name_plural = "Categorie"


class CondizioniDiVendita(models.Model):
    id_condizione_di_vendita = models.AutoField(primary_key=True)
    tipo_condizione = models.CharField(max_length=135)
    descrizione_condizione = models.CharField(max_length=135, blank=True)
    def __unicode__(self):
        return self.tipo_condizione
    class Meta:
        verbose_name_plural = 'Condizioni di Vendita'