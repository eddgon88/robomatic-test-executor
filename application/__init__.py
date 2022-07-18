# application/__init__.py
import config
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .test_executor.services.TestExecutorService import TestExecutorService
import pika
import ast

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
    
    channel.basic_consume('tasks.execute_test',
    execute_test,
    auto_ack=True)

    # start consuming (blocks)
    channel.start_consuming()
    connection.close()


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
        
