from django.db import models

class Lobby(models.Model):
	filing_id = models.CharField(max_length=45,unique=True)
	year = models.CharField(max_length=4)
	received = models.DateField()
	amount = models.CharField(max_length=45)
	type = models.CharField(max_length=45)
	period = models.CharField(max_length=45)
	registrant_id = models.CharField(max_length=45)
	registrant_name = models.CharField(max_length=255)
	address = models.TextField()
	registrant_country = models.CharField(max_length=45)
	registrant_ppbcountry = models.CharField(max_length=45)	
	client_name = models.CharField(max_length=45)
	client_id = models.CharField(max_length=45)
	client_status = models.CharField(max_length=45)
	contact_fullname = models.CharField(max_length=45)
	client_country = models.CharField(max_length=45)
	client_ppbcountry = models.CharField(max_length=45)
	client_state = models.CharField(max_length=45)
	client_ppbstate = models.CharField(max_length=45)
	
	class Meta:
		db_table = 'data_lobby'
	
	def __unicode__(self):
		return self.filing_id

class AffiliatedOrg(models.Model):
	filing = models.ForeignKey('Lobby',to_field='filing_id')
	affiliated_orgname = models.CharField(max_length=255)
	affiliated_orgcountry = models.CharField(max_length=45)
	affiliated_orgppbcountry = models.CharField(max_length=45)

	class Meta:
		db_table = 'data_affiliatedorgs'

	def __unicode__(self):
		return self.affiliated_orgname
		
class Agency(models.Model):
	filing = models.ForeignKey('Lobby',to_field='filing_id')
	gov_entity_name = models.CharField(max_length=255)

	class Meta:
		db_table = 'data_agencies'

	def __unicode__(self):
		return self.gov_entity_name

class ForeignEntity(models.Model):
	filing = models.ForeignKey('Lobby',to_field='filing_id')
	foreign_entity_name = models.CharField(max_length=255)
	foreign_entity_country = models.CharField(max_length=45)
	foreign_entity_ppbcountry = models.CharField(max_length=45)
	foreign_entity_status = models.CharField(max_length=45)
	foreign_entity_ownpercentage = models.CharField(max_length=45)
	foreign_entity_contribution = models.CharField(max_length=45)
	
	class Meta:
		db_table = 'data_foreignentity'
	
	def __unicode__(self):
		return self.foreign_entity_name

class Issue(models.Model):
	filing = models.ForeignKey('Lobby',to_field='filing_id')
	issue_code = models.CharField(max_length=45)
	specific_issue = models.TextField()
	
	class Meta:
		db_table = 'data_issues'
	
	def __unicode__(self):
		return self.issue_code

class Lobbyist(models.Model):
	filing = models.ForeignKey('Lobby',to_field='filing_id')
	lobbyist_name = models.CharField(max_length=100)
	lobbyist_status = models.CharField(max_length=45)
	lobbyist_indicator = models.CharField(max_length=45)
	official_position = models.TextField()	

	class Meta:
		db_table = 'data_lobbyists'

	def __unicode__(self):
		return self.lobbyist_name
