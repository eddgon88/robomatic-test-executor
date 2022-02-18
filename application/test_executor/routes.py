# application/order_api/routes.py
from flask import jsonify, request, make_response
from . import test_executor_blueprint
from .services.TestExecutorService import TestExecutorService

@test_executor_blueprint.route('/test-executor/v1/execute', methods=['POST'])
def checkout():
    content = request.get_json()
    print(content)
    status = TestExecutorService.executeTest(content)
    print(status)
    return "True"
