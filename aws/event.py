import logging

S3_RECORDS = "Records"
API_HTTP_METHOD = "httpMethod"
CLOUD_WATCH_EVENT_ID = "id"

log = logging.getLogger()
log.setLevel(logging.INFO)


def cloud_watch_trigger_event_check(func):
    def _check(*args, **kwargs):
        try:
            event_id = args[0][CLOUD_WATCH_EVENT_ID]
            log.info("Cloud watch trigger event id : {}".format(event_id))
            if event_id:
                return func(*args, **kwargs)
            else:
                log.warning("Invalid event id")
        except KeyError as ke:
            if ke.args[0] is CLOUD_WATCH_EVENT_ID:
                log.error("No event id : {}".format(ke))
            else:
                raise Exception(ke)
        except Exception as e:
            log.error("Error while parsing event : {}".format(e))
            raise Exception(e)

    return _check


def s3_trigger_event_check(func):
    def _check(*args, **kwargs):
        try:
            s3_object = args[0][S3_RECORDS]
            if s3_object:
                return func(*args, **kwargs)
            else:
                log.warning("Invalid s3 event")
        except KeyError as ke:
            if ke.args[0] is S3_RECORDS:
                log.error("No s3 event : {}".format(ke))
            else:
                raise Exception(ke)
        except Exception as e:
            log.error("Error while parsing event : {}".format(e))
            raise Exception(e)

    return _check


def api_gateway_trigger_event_check(func):
    def _check(*args, **kwargs):
        try:
            http_method = args[0][API_HTTP_METHOD]
            log.info("API gateway http method : {}".format(http_method))
            if http_method:
                return func(*args, **kwargs)
            else:
                log.warning("Invalid http method")
        except KeyError as ke:
            if ke.args[0] is API_HTTP_METHOD:
                log.error("No event id : {}".format(ke))
            else:
                raise Exception(ke)
        except Exception as e:
            log.error("Error while parsing event : {}".format(e))
            raise Exception(e)

    return _check
