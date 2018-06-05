from django.db import models

class ListenerDesperdicio(models.Model):
    projeto = models.CharField(max_length=60, blank=True, null=True)
    colaborador = models.CharField(max_length=300, blank=True, null=True)
    evento = models.CharField(max_length=200, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    tipo_evento = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_desperdicio'


class ListenerHorasfrente(models.Model):
    projeto = models.CharField(max_length=60, blank=True, null=True)
    colaborador = models.CharField(max_length=300, blank=True, null=True)
    data = models.DateField(blank=True, null=True)
    horas = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    cc_ea = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'listener_horasfrente'


class ListenerIssue(models.Model):
    chave = models.CharField(unique=True, max_length=10)
    projeto = models.CharField(max_length=60, blank=True, null=True)
    data_criacao = models.DateField(blank=True, null=True)
    id_jira = models.IntegerField()
    descricao = models.CharField(max_length=200, blank=True, null=True)
    issue_type = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_issue'


class ListenerIssuetypes(models.Model):
    issue_type = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_issuetypes'


class ListenerKeyresult(models.Model):
    descricao = models.CharField(max_length=2000, blank=True, null=True)
    target = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    valor_atual = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    objective = models.ForeignKey('ListenerObjective', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listener_keyresult'


class ListenerLimits(models.Model):
    projeto = models.CharField(max_length=60, blank=True, null=True)
    limite = models.IntegerField()
    tipo_limite = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_limits'


class ListenerLogjson(models.Model):
    json = models.CharField(max_length=30000, blank=True, null=True)
    issue = models.ForeignKey(ListenerIssue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listener_logjson'


class ListenerMaillimits(models.Model):
    email = models.CharField(max_length=80, blank=True, null=True)
    limit = models.ForeignKey(ListenerLimits, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listener_maillimits'


class ListenerObjective(models.Model):
    projeto = models.CharField(max_length=60, blank=True, null=True)
    quarter = models.CharField(max_length=2, blank=True, null=True)
    ano = models.IntegerField()
    descricao = models.CharField(max_length=2000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_objective'


class ListenerProjetos(models.Model):
    projeto = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'listener_projetos'


class ListenerTransition(models.Model):
    data_evento = models.DateField(blank=True, null=True)
    transicao_origem = models.CharField(max_length=50, blank=True, null=True)
    transicao_destino = models.CharField(max_length=50, blank=True, null=True)
    issue = models.ForeignKey(ListenerIssue, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'listener_transition'


class ListenerTransitionorder(models.Model):
    issue_type = models.CharField(max_length=30, blank=True, null=True)
    tipo_fluxo = models.CharField(max_length=30, blank=True, null=True)
    ordem = models.IntegerField()
    transicao_destino = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_transitionorder'


class ListenerValorhorames(models.Model):
    data = models.DateField(blank=True, null=True)
    valor = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'listener_valorhorames'
