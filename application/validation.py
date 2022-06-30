from email.policy import HTTP
from werkzeug.exceptions import HTTPException
from flask import make_response
import json

class NotFoundError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 404)

class CourseError(HTTPException):
    def __init__(self, error_code, error_message):
        message = {
            "error_code": error_code,
            "error_message": error_message
        }
        self.response = make_response(json.dumps(message), 400)

class AlreadyExistsError(HTTPException):
    def __init__(self, message):
        self.response = make_response(message, 409)

class StudentError(HTTPException):
    def __init__(self, error_code, error_message):
        message = {
            "error_code": error_code,
            "error_message": error_message
        }
        self.response = make_response(json.dumps(message), 400)

class EnrollmentError(HTTPException):
    def __init__(self, error_code, error_message):
        message = {
            "error_code": error_code,
            "error_message": error_message
        }
        self.response = make_response(json.dumps(message), 400)