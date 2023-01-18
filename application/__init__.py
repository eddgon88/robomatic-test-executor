# application/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .test_executor.services.TestExecutorService import TestExecutorService
from .jms.jms_client import PikaClient
import pika
import ast
import asyncio

db = SQLAlchemy()

def make_pika():
    params = pika.URLParameters('amqp://admin:admin@127.0.0.1:5672')
    connection = pika.BlockingConnection(params)
    channel = connection.channel() # start a channel
    #channel.queue_declare(queue='tasks.execute_test') # Declare a queue

    def execute_test(ch, method, properties, body):
        body_str = body.decode("UTF-8")
        content = ast.literal_eval(body_str)        
        print(content)
        TestExecutorService.executeTest(content)

    def stop_test_execution(ch, method, properties, body):
        body_str = body.decode("UTF-8")
        content = ast.literal_eval(body_str)        
        print(content)
        TestExecutorService.stop_test(content)
    
    channel.basic_consume('tasks.execute_test',
    execute_test,
    auto_ack=True)

    channel.basic_consume('tasks.stop_test_execution',
    stop_test_execution,
    auto_ack=True)

    # start consuming (blocks)
    channel.start_consuming()
    connection.close()

async def make_pika_listener():
    loop = asyncio.get_running_loop()
    pikaClient = PikaClient(TestExecutorService.executeTest)
    task = loop.create_task(pikaClient.consume(loop))
    await task

def create_app():    
    app = Flask(__name__)
    environment_configuration = os.environ['CONFIGURATION_SETUP']
    app.config.from_object(environment_configuration)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    with app.app_context():
        make_pika()

    with app.app_context():
        from .test_executor import test_executor_blueprint
        app.register_blueprint(test_executor_blueprint)
        return app
        
