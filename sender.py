import pika
port = 32771
credentials = pika.PlainCredentials('guest', 'salo123')
connection = pika.BlockingConnection(pika.ConnectionParameters(
               'localhost',port,'/',credentials))
channel = connection.channel()

channel.queue_declare(queue='hello')
text = raw_input("Mesaj:")
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=text)
print(" [x] Sent ",text)
connection.close()
