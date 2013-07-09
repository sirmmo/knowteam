# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Term'
        db.create_table(u'ktree_term', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('wikipedia', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
        ))
        db.send_create_signal(u'ktree', ['Term'])

        # Adding model 'LinkType'
        db.create_table(u'ktree_linktype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'ktree', ['LinkType'])

        # Adding model 'Link'
        db.create_table(u'ktree_link', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('a', self.gf('django.db.models.fields.related.ForeignKey')(related_name='starts', to=orm['ktree.Term'])),
            ('b', self.gf('django.db.models.fields.related.ForeignKey')(related_name='ends', to=orm['ktree.Term'])),
            ('name', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['ktree.LinkType'])),
            ('bidirectional', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'ktree', ['Link'])


    def backwards(self, orm):
        # Deleting model 'Term'
        db.delete_table(u'ktree_term')

        # Deleting model 'LinkType'
        db.delete_table(u'ktree_linktype')

        # Deleting model 'Link'
        db.delete_table(u'ktree_link')


    models = {
        u'ktree.link': {
            'Meta': {'object_name': 'Link'},
            'a': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'starts'", 'to': u"orm['ktree.Term']"}),
            'b': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'ends'", 'to': u"orm['ktree.Term']"}),
            'bidirectional': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['ktree.LinkType']"})
        },
        u'ktree.linktype': {
            'Meta': {'object_name': 'LinkType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        u'ktree.term': {
            'Meta': {'object_name': 'Term'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ktree']