from cassandra.cqlengine import columns
from cassandra.cqlengine.models import Model


class BaseActivity(Model):
    feed_id = columns.Ascii(primary_key=True, partition_key=True)
    activity_id = columns.Ascii(primary_key=True, clustering_order='desc')


class Activity(BaseActivity):
    actor = columns.Ascii(required=False)
    extra_context = columns.Bytes(required=False)
    object = columns.Ascii(required=False)
    target = columns.Ascii(required=False)
    time = columns.DateTime(required=False)
    verb = columns.Integer(required=False)


class AggregatedActivity(BaseActivity):
    activities = columns.Bytes(required=False)
    created_at = columns.DateTime(required=False)
    group = columns.Ascii(required=False)
    updated_at = columns.DateTime(required=False)
