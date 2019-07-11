from aws.event import api_gateway_trigger_event_check


@api_gateway_trigger_event_check
def handler(event, context):
    try:
        pass
    except Exception as e:
        raise e
