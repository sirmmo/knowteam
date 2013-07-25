# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Term.accepted'
        db.add_column(u'ktree_term', 'accepted',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Term.accepted'
        db.delete_column(u'ktree_term', 'accepted')


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
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'primary': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wikipedia': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['ktree']