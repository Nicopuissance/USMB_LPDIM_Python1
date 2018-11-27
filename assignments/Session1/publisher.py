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
                      body='Hello World !')
print ("[x] Sent 'Hello World'")
print ("[x] Sent 'Bonjour monde'")
print ("[x] Sent 'Good morning city'")
print ("[x] Sent 'hey hi hello World'")
connection.close()
