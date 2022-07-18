# application/order_api/routes.py
from flask import request
from . import test_executor_blueprint
from .services.TestExecutorService import TestExecutorService
from ...run import app
from celery import make_celery

celery = make_celery(app)

@test_executor_blueprint.route('/test-executor/v1/execute', methods=['POST'])
def checkout():
    content = request.get_json()
    print(content)
    TestExecutorService.executeTest(content)
    return "True"

# @test_executor_blueprint.route('/test-executor/v1/create', methods=['GET'])
# def checkout():
#     content = request.get_json()
#     print(content)
#     #file = EvidenceFile(evidence_id = 'ef756480876', file_name = 'test.txt', evidence_uri = '/home/edgar/evidences', test_execution_id = 'te456468574')
#     #db.session.add(file)
#     #db.session.commit()
#     #evidence = CaseEvidence(evidence_id = file.evidence_id, evidence_text = 'esto es una prueba')
#     #db.session.add(evidence)
#     #db.session.commit()
#     result = EvidenceFile.get_file("tsest.txt", "te456468d574")
#     print(result)
#     return "True"
# 
# try:
#     connection = pika.BlockingConnection(pika.ConnectionParameters(host="127.0.0.1",
#                                                                     port=5672,
#                                                                     credentials=pika.PlainCredentials("admin", "admin"),
#                                                                 ))
# except pika.exceptions.AMQPConnectionError as exc:
#     print("Failed to connect to RabbitMQ service. Message wont be sent.")
#     raise exc
#
#channel = connection.channel()
#    
#def callback(ch, method, properties, body):
#    print(" Received %s" % body.decode())
#    print(" Done")
#
#    ch.basic_ack(delivery_tag=method.delivery_tag)
#
#channel.basic_qos(prefetch_count=1)
#channel.basic_consume(queue='execute_test', on_message_callback=callback)
#channel.start_consuming()
#