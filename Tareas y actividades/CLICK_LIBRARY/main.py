'''
Click usage example.
'''

import click
from datetime import datetime
import random
import string
import os

@click.group()
def cli():
    pass


@cli.command()
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", prompt="Your name", help="The person to greet.")
def hello(count, name):
    for _ in range(count):
        click.echo(f"Hello, {name}!")


@cli.command()
def timenow():
    print(f'\n(datetime.now())\n')

@cli.command()
@click.option('--length', default=12, help='Longitud de la contraseña.')
def generatepassword(length):
    if length < 4:
        click.echo("Lo siento, la contraseña debe tener un mínimo de 4 caracteres.")
        return

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    click.echo(f"Tu contraseña generada es: {password}")

@cli.command()
@click.option('--operation', type=click.Choice(['sum', 'subtract', 'multiply', 'divide']), prompt='Operación (sum, subtract, multiply, divide)')
@click.option('--a', type=float, prompt='Primer número')
@click.option('--b', type=float, prompt='Segundo número')
def calculator(operation, a, b):
    """Realiza cálculos simples."""
    if operation == 'sum':
        result = a + b
    elif operation == 'subtract':
        result = a - b
    elif operation == 'multiply':
        result = a * b
    elif operation == 'divide':
        if b == 0:
            click.echo('Error: no se puede dividir por cero.')
            return
        result = a / b

    click.echo(f"El resultado de {operation} es: {result}")

if __name__ == '__main__':
    cli()