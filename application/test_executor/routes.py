# application/order_api/routes.py
from flask import request
from . import test_executor_blueprint
from .services.TestExecutorService import TestExecutorService
from ..jms.jms_client import PikaClient

@test_executor_blueprint.route('/test-executor/v1/execute', methods=['POST'])
def checkout():
    content = request.get_json()
    print(content)
    TestExecutorService.executeTest(content)
    return "True"