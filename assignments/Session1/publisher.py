#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:24:58 2018

@author: nicolasduwavrent
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 15:50:02 2018

@author: nicolasduwavrent
"""
import os
import pika
import key
amqp_url=key.key

url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 50
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel = connection.channel()
channel.queue_declare(queue='hello',durable='true')
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Hello World !',
                      properties = pika.BasicProperties(delivery_mode=2,))
print ("[x] Sent 'Hello World'")
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Bonjour monde',
                      properties = pika.BasicProperties(delivery_mode=2,))
print ("[x] Sent 'Bonjour monde'")
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='Good morning city',
                      properties = pika.BasicProperties(delivery_mode=2,))
print ("[x] Sent 'Good morning city'")
channel.basic_publish(exchange='',
                      routing_key='hello',
                      body='hey hi hello World',
                      properties = pika.BasicProperties(delivery_mode=2,))
print ("[x] Sent 'hey hi hello World'")
connection.close()
