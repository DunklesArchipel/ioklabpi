#from confluent_kafka import Producer
import pika
import sys
import csv
import json

topic="atopic"

connection = pika.BlockingConnection(pika.ConnectionParameters('iokserver'))
channel = connection.channel()
channel.exchange_declare(exchange=topic, exchange_type='fanout')
# reader = csv.reader(sys.stdin)

while True:
    line = sys.stdin.readline()
    if not line: break
    channel.basic_publish(exchange=topic, routing_key='', body=line)
print("done.")
