from aws.event import s3_trigger_event_check


@s3_trigger_event_check
def handler(event, context):
    try:
        pass
    except Exception as e:
        raise e


try:
    handler(None, None)
except Exception as e:
    print(e)
