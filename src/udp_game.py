'''
CS 3700 - Networking & Distributed Computing - Fall 2024
Instructor: Thyago Mota
Student:
Description: Homework 04 - UDP Game
'''

import asyncio
from websockets import serve
from random import randint

HOST = '127.0.0.1'
PORT = 4000
BUFFER = 1024
READY = 0
BUSY = 1

async def handle_connection(ws, _):
    number = randint(1, 100)
    print(f'Ready to play...')
    print(f'number to be guessed is {number}')
    msg = 'guess a number between 1 and 100' 
    await ws.send(msg)
    attempts = 0
    while True: 
        msg = await ws.recv()
        guess = int(msg)
        print(f'client guessed {guess}')
        attempts += 1
        if guess == number: 
            msg = f'guessed after {attempts} attempts'
        elif guess > number: 
            msg = f'the number is < {guess}'
        else: 
            msg = f'the number is > {guess}'
        await ws.send(msg)
        if guess == number: 
            break

if __name__ == "__main__":
    ws = serve(handle_connection, HOST, PORT)
    asyncio.get_event_loop().run_until_complete(ws)
    print("WebSocket server is running on ws://localhost:8080")
    asyncio.get_event_loop().run_forever()
