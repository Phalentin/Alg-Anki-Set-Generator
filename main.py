import genanki as ga, kociemba
from cubestring import *

allowed_chars = "RLUDFBMESrludfbxyzw'23 "

def solve(alg):
    cubestring = scramble_to_cubestring(alg)
    scramble = kociemba.solve(cubestring)
    return scramble
    #moves = alg.split()
    #inverted_alg = []
    #inverted_algstring = ""

    #for move in moves:
    #    cleaned_move = move.replace("(", "").replace(")", "")
    #    if "'" in cleaned_move:
    #        inverted_move = cleaned_move.replace("'", "")

    #        inverted_alg.insert(0, inverted_move)
    #    elif "2" in cleaned_move:
    #        inverted_move = cleaned_move

    #        inverted_alg.insert(0, inverted_move)
    #    else:
    #        inverted_move = cleaned_move + "'"

    #        inverted_alg.insert(0, inverted_move)
    #
    #for i in range(len(inverted_alg)):
    #    inverted_algstring += inverted_alg[i] + " "

    #return inverted_algstring

def create_cards(algs, deck):
    for i in range(len(algs)):
        alg = algs[i]
        scramble = solve(alg)
        
        note = ga.Note(
            model=default_model,
            fields=[scramble, alg]
        )

        deck.add_note(note)


default_model = ga.Model(
  1540995705,
  'Default Model',
  fields=[
    {'name': 'Scramble'},
    {'name': 'Algorithm'}
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Scramble}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Algorithm}}',
    }
  ]
)

algs = []

with open("algs.txt") as alg_file:
    lines = alg_file.readlines()
    
    deck_name = lines[0].replace("\n", "").replace("\t", "")
    lines.pop(0)

    for line in lines:
        stripped_line = line.replace("\n", "")
        
        if stripped_line != "":
            algs.append(stripped_line)
    alg_file.close()

deck = ga.Deck(
    1770553627,
    deck_name
)

create_cards(algs, deck)

package_name = deck_name.lower() + ".apkg"
package_name = package_name.replace(" ", "_")
ga.Package(deck).write_to_file(package_name)