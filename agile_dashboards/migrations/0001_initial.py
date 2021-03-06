# Generated by Django 2.0.6 on 2018-06-05 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desperdicio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=60, null=True)),
                ('colaborador', models.CharField(max_length=300, null=True)),
                ('evento', models.CharField(max_length=200, null=True)),
                ('data', models.DateField(null=True)),
                ('tipo_evento', models.CharField(max_length=20, null=True)),
                ('horas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='HorasFrente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=60, null=True)),
                ('colaborador', models.CharField(max_length=300, null=True)),
                ('data', models.DateField(null=True)),
                ('horas', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('cc_ea', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_jira', models.IntegerField(default=0)),
                ('chave', models.CharField(max_length=10)),
                ('projeto', models.CharField(max_length=60, null=True)),
                ('descricao', models.CharField(default=None, max_length=200, null=True)),
                ('data_criacao', models.DateField(null=True)),
                ('issue_type', models.CharField(default=None, max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='IssueTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(default=None, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KeyResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=2000, null=True)),
                ('target', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('valor_atual', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Limits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=60, null=True)),
                ('limite', models.IntegerField()),
                ('tipo_limite', models.CharField(max_length=60, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LogJson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('json', models.CharField(max_length=30000, null=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agile_dashboards.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='MailLimits',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=80, null=True)),
                ('limit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agile_dashboards.Limits')),
            ],
        ),
        migrations.CreateModel(
            name='Objective',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=60, null=True)),
                ('quarter', models.CharField(max_length=2, null=True)),
                ('ano', models.IntegerField(default=2018)),
                ('descricao', models.CharField(max_length=2000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Projetos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('projeto', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Transition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_evento', models.DateField(null=True)),
                ('transicao_origem', models.CharField(max_length=50, null=True)),
                ('transicao_destino', models.CharField(max_length=50, null=True)),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agile_dashboards.Issue')),
            ],
        ),
        migrations.CreateModel(
            name='TransitionOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue_type', models.CharField(default=None, max_length=30, null=True)),
                ('tipo_fluxo', models.CharField(default=None, max_length=30, null=True)),
                ('ordem', models.IntegerField()),
                ('transicao_destino', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ValorHoraMes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('valor', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='keyresult',
            name='objective',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agile_dashboards.Objective'),
        ),
    ]
