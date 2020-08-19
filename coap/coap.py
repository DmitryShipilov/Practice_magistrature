#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import logging
import aiocoap
 
logging.basicConfig(level=logging.INFO)
 
# CoAP message codes
Code = aiocoap.numbers.codes.Code
 
async def CoAP_request(code, uri, payload=None):
	protocol = await aiocoap.Context.create_client_context()
 
	if payload:
		request = aiocoap.Message(code=code, uri=uri, payload=payload)
	else:
		request = aiocoap.Message(code=code, uri=uri)
 
 
	try:
		response = await protocol.request(request).response
	except Exception as e:
		print('Failed to fetch resource:')
		print(e)
	else:
		print ("Result code:", response.code,"\n",
		"Payload:", response.payload)
 
"""
if __name__ == "__main__":

	asyncio.get_event_loop().run_until_complete(CoAP_request(
	code=Code.GET,
	uri='coap://localhost/other/block'
	))
"""

print("\nPUT")

size = 1
asyncio.get_event_loop().run_until_complete(CoAP_request(
code=Code.PUT,
uri='coap://localhost/other/block',
payload = b"bytes_is10" * size
))

"""
print("\nGET")
 
asyncio.get_event_loop().run_until_complete(CoAP_request(
code=Code.GET,
uri='coap://127.0.0.1/other/block',
))
"""

"""
print("\nPUT")
 
asyncio.get_event_loop().run_until_complete(CoAP_request(
code=Code.PUT,
uri='coap://localhost/other/block',
payload = b"xxx xxx xxx\n" * size
))
print("\nGET")
 
asyncio.get_event_loop().run_until_complete(CoAP_request(
code=Code.GET,
uri='coap://localhost/time',
))
print("\n")
"""
