"""
    Hey, little train! We are all jumping on
The train that goes to the kingdom.
We're happy, ma, we're having fun,
And the train ain't even left the station.


Hey, little train! Wait for me!
I once was blind but now I see.
Have you left a seat for me?
Is that such a stretch of the imagination?


Hey, little train! Wait for me!
I was held in chains but now I'm free.
I'm hanging in there, don't you see,
In this process of elimination.


Hey, little train! We are all jumping on
The train that goes to the kingdom.
We're happy, ma, we're having fun.
It's beyond my wildest expectation.
"""

texto = """Hey, little train! We are all jumping on
The train that goes to the kingdom.
We're happy, ma, we're having fun,
And the train ain't even left the station.


Hey, little train! Wait for me!
I once was blind but now I see.
Have you left a seat for me?
Is that such a stretch of the imagination?


Hey, little train! Wait for me!
I was held in chains but now I'm free.
I'm hanging in there, don't you see,
In this process of elimination.


Hey, little train! We are all jumping on
The train that goes to the kingdom.
We're happy, ma, we're having fun.
It's beyond my wildest expectation."""
texto = texto.split()

for palavra in texto:
    for letra in palavra:
        if letra == 'H':
            letra = 'f'