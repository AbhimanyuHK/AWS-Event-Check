from aws.event import cloud_watch_trigger_event_check


@cloud_watch_trigger_event_check
def handler(event, context):
    try:
        pass
    except Exception as e:
        raise e
