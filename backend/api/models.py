# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class PnpAcademicos(models.Model):
    pnp_aca_id = models.AutoField(db_column='PNP_ACA_ID', primary_key=True)  # Field name made lowercase.
    pnp_aca_ano = models.IntegerField(db_column='PNP_ACA_ANO', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_regiao = models.CharField(db_column='PNP_ACA_REGIAO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_uf = models.CharField(db_column='PNP_ACA_UF', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_estado = models.CharField(db_column='PNP_ACA_ESTADO', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_org_academica = models.CharField(db_column='PNP_ACA_ORG_ACADEMICA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_instituicao_sigla = models.CharField(db_column='PNP_ACA_INSTITUICAO_SIGLA', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_instituicao_nome = models.CharField(db_column='PNP_ACA_INSTITUICAO_NOME', max_length=100, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_nome_curso = models.CharField(db_column='PNP_ACA_NOME_CURSO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_tipo_curso = models.CharField(db_column='PNP_ACA_TIPO_CURSO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_tipo_eixo_tecnologico = models.CharField(db_column='PNP_ACA_TIPO_EIXO_TECNOLOGICO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_subeixo_tecnologico = models.CharField(db_column='PNP_ACA_SUBEIXO_TECNOLOGICO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_tipo_oferta = models.CharField(db_column='PNP_ACA_TIPO_OFERTA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_turno_oferta = models.CharField(db_column='PNP_ACA_TURNO_OFERTA', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_modalidade_ensino = models.CharField(db_column='PNP_ACA_MODALIDADE_ENSINO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_fonte_financiamento = models.CharField(db_column='PNP_ACA_FONTE_FINANCIAMENTO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_cursos = models.IntegerField(db_column='PNP_ACA_QTD_CURSOS', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_ingressantes = models.IntegerField(db_column='PNP_ACA_QTD_INGRESSANTES', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_inscritos = models.IntegerField(db_column='PNP_ACA_QTD_INSCRITOS', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_matriculas = models.IntegerField(db_column='PNP_ACA_QTD_MATRICULAS', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_vagas = models.IntegerField(db_column='PNP_ACA_QTD_VAGAS', blank=True, null=True)  # Field name made lowercase.
    pnp_aca_qtd_matricula_equivalente = models.IntegerField(db_column='PNP_ACA_QTD_MATRICULA_EQUIVALENTE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pnp_academicos'
