# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'TipoObservatorio'
        db.create_table('contraparte_tipoobservatorio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('contraparte', ['TipoObservatorio'])

        # Adding model 'Observatorio'
        db.create_table('contraparte_observatorio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('informe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Informe'])),
            ('tipo_observatorio', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.TipoObservatorio'])),
            ('accion', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('contraparte', ['Observatorio'])

        # Adding model 'ParticipacionComision'
        db.create_table('contraparte_participacioncomision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('informe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Informe'])),
            ('tipo_comision', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Comision'])),
            ('tipo_accion', self.gf('django.db.models.fields.IntegerField')()),
            ('estado', self.gf('django.db.models.fields.IntegerField')()),
            ('ambito', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('contraparte', ['ParticipacionComision'])

        # Adding model 'Comision'
        db.create_table('contraparte_comision', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('contraparte', ['Comision'])

        # Adding model 'AgendaPublica'
        db.create_table('contraparte_agendapublica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('informe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.Informe'])),
            ('tipo_accion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['contraparte.AccionAgenda'])),
            ('tema', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['fed.Tema'])),
            ('ambito', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('contraparte', ['AgendaPublica'])

        # Adding model 'AccionAgenda'
        db.create_table('contraparte_accionagenda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('contraparte', ['AccionAgenda'])


    def backwards(self, orm):
        
        # Deleting model 'TipoObservatorio'
        db.delete_table('contraparte_tipoobservatorio')

        # Deleting model 'Observatorio'
        db.delete_table('contraparte_observatorio')

        # Deleting model 'ParticipacionComision'
        db.delete_table('contraparte_participacioncomision')

        # Deleting model 'Comision'
        db.delete_table('contraparte_comision')

        # Deleting model 'AgendaPublica'
        db.delete_table('contraparte_agendapublica')

        # Deleting model 'AccionAgenda'
        db.delete_table('contraparte_accionagenda')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'contraparte.accionagenda': {
            'Meta': {'object_name': 'AccionAgenda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'contraparte.accionimplementada': {
            'Meta': {'object_name': 'AccionImplementada'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"})
        },
        'contraparte.accionimpulsada': {
            'Meta': {'object_name': 'AccionImpulsada'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {})
        },
        'contraparte.agendapublica': {
            'Meta': {'object_name': 'AgendaPublica'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'tema': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Tema']"}),
            'tipo_accion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.AccionAgenda']"})
        },
        'contraparte.comision': {
            'Meta': {'object_name': 'Comision'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'contraparte.informe': {
            'Meta': {'object_name': 'Informe'},
            'anio_desde': ('django.db.models.fields.IntegerField', [], {}),
            'anio_hasta': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mes_desde': ('django.db.models.fields.IntegerField', [], {}),
            'mes_hasta': ('django.db.models.fields.IntegerField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'proyecto': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Proyecto']"})
        },
        'contraparte.observatorio': {
            'Meta': {'object_name': 'Observatorio'},
            'accion': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'tipo_observatorio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.TipoObservatorio']"})
        },
        'contraparte.participacioncomision': {
            'Meta': {'object_name': 'ParticipacionComision'},
            'ambito': ('django.db.models.fields.IntegerField', [], {}),
            'estado': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'informe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Informe']"}),
            'tipo_accion': ('django.db.models.fields.IntegerField', [], {}),
            'tipo_comision': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contraparte.Comision']"})
        },
        'contraparte.tipoobservatorio': {
            'Meta': {'object_name': 'TipoObservatorio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'fed.donante': {
            'Meta': {'object_name': 'Donante'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '25'})
        },
        'fed.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'antecedentes': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'default': "'email@example.com'", 'max_length': '75', 'blank': 'True'}),
            'estrategias': ('django.db.models.fields.TextField', [], {'default': "''", 'blank': 'True'}),
            'fecha': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 14)', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'no_inss': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_mingob': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'no_ruc': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '50', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '25'}),
            'obj_gral': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '250', 'blank': 'True'}),
            'representante_legal': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '120', 'blank': 'True'}),
            'sitio_web': ('django.db.models.fields.URLField', [], {'default': "'www.example.com'", 'max_length': '200', 'blank': 'True'}),
            'telefono': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'telefono_contacto': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '15', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'fed.proyecto': {
            'Meta': {'object_name': 'Proyecto'},
            'cobertura': ('django.db.models.fields.IntegerField', [], {}),
            'codigo': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100', 'primary_key': 'True'}),
            'fecha_fin': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 14)'}),
            'fecha_inicio': ('django.db.models.fields.DateField', [], {'default': 'datetime.date(2011, 6, 14)'}),
            'modalidad': ('django.db.models.fields.IntegerField', [], {}),
            'monto_contrapartida': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'monto_fed': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'monto_otros': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '2', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.TextField', [], {}),
            'organizacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['fed.Organizacion']"}),
            'otros_donantes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fed.Donante']", 'null': 'True', 'blank': 'True'}),
            'resultados': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['fed.Resultado']", 'null': 'True', 'blank': 'True'})
        },
        'fed.resultado': {
            'Meta': {'object_name': 'Resultado'},
            'codigo': ('django.db.models.fields.IntegerField', [], {}),
            'descripcion': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '35'})
        },
        'fed.tema': {
            'Meta': {'object_name': 'Tema'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['contraparte']
