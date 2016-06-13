import pika
from subprocess import call
port = 32771
credentials = pika.PlainCredentials('guest','salo123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost',port,'/',credentials))
channel = connection.channel()
channel.queue_declare(queue='hello')
def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)
    arguments = body.split(" ")
    call(["bash","processor.sh",arguments[0],arguments[1]])
    print("Executed")
channel.basic_consume(callback,
                      queue='hello',
                      no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
