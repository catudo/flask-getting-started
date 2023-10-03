import traceback

class ErrorException(Exception):

    
    def __init__(self, error, status_code, status_message, details=None):
        self.status_code = int(status_code)
        self.error_title = error
        self.error_message = status_message
        self.error_detail = details
        self.stacktrace = traceback.format_exc()


    def to_json(self):
        jsonObj = {
                'error_detail': self.error_detail,
                'error_message': self.error_message,
                'error_code':self.status_code,
                'stacktrace':self.stacktrace
            }
        return jsonObj

    def get_http_code(self):
        return self.status_code


    @classmethod 
    def init_from_exception(cls, exc):
        if isinstance(exc, ErrorException):
        	raise exc
        return cls(exc,500,None,None)   