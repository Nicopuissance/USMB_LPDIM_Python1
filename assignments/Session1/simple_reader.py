#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 13:25:21 2018

@author: nicolasduwavrent
"""

import os
import pika
import key

amqp_url=key.key
url = os.environ.get('CLOUDAMQP_URL',amqp_url)
params = pika.URLParameters(url)
params.socket_timeout = 100
#initiate the connexion
connection = pika.BlockingConnection(params) # Connect to CloudAMQP
channel=connection.channel()
channel.queu_declare(queu='hello')

def callback(ch,method,properties,body):
    print("[X] Received %r" % body)
    
channel.basic_consume(callback,queue='hello',no_ack=True)

print('[X] Waiting for message. To exit press CTRL+C')
channel.start_consuming()