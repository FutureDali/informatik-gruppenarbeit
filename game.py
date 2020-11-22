print("""Moderator: Tja guten Abend meine Damen und Herren. Herzlich Willkommen auch unsere Kandidaten. Guten Abend Frau Surbier.""")
print("Frau Surbier: Guten Abend")
print("Moderator: Guten Abend Herr Hacker ")
print("Herr Hacker: Guten Abend")
print("Moderator: Fühlen sie sich im Vollbesitz ihrer geistigen Kräfte?")
print("Herr Hacker: Aber immer!")
print("Frau Surbier nickt")
print("""Moderator: Na gut dann können wir ja anfangen. Ähm Herr Hacker, Frau Surbier ihr Spezielgebiet ist 'Rembrandt'. Frage 1: Am 20.06.1630 erhält Rembrandt den Besuch eines Abgesandten der spanischen Krone. Wie hieß der Maler der diesen Besuch erhielt?""")
a = input("Wer soll antworten? [Frau Surbier / Herr Hacker]: ")
if a == "Frau Surbier":
    print("Frau Surbier: Hmm Ägypten?")
    print("Moderator schaut verdattert (Gelächter)")
    print("Moderator: Das ist leider Falsch. Und das Beendet unsere Runde auch leider schon!")
elif a == "Herr Hacker":
    print("Herr Hacker: Äh Rembrandt?")
    print("Moderator: Das ist Richtig. (Applaus und Gelächter)")
    print("Moderator: Die nächste Frage. Bei einem Bild von Rembrandt, wird die Frau des Malers als Göttin der Jagt dargestellt.")
    print("Moderator: Wie hieß der Mann, der Frau, des Malers?")
    b = input("Wer soll antworten? [Frau Surbier / Herr Hacker]: ")
    if b == "Frau Surbier":
        print("Frau Surbier: Walter?")
        print("Moderator: Nein tut mir leid.")
        print("Moderator zieht vor Dummheit eine Grimasse (Gelächter im Hintergrund)")
        print("Frau Surbier: Achso sie meinen den Nachnamen. Ne den weiß ich nicht. (Mehr Gelächter)")
        print("Moderator: Das war es leider für sie (Applaus)")
    elif b == "Herr Hacker":
        print("Herr Hacker: Wie... wie welches Malers? Rembrandt?")
        print("Moderator (enthusiastisch): Absolut korrekt (Applaus und Gelächter) ")
        print("Herr Hacker, Frau Surbier die letzte Frage für sie")
        print("Moderator: Das Haus in dem Rembrandt vierzig Jahre seines Lebens verbrachte, wurde nach seinem Tode nach einem Mann benannt, \n der darin einen Großteil seines Lebens verbrachte. Wie war der Name dieses Mannes? ")
        c = input("Wer soll antworten? [Frau Surbier / Herr Hacker]: ")
        if c == "Frau Surbier":
            print("Frau Surbier: Ne das weiß ich leider nicht?")
            print("Moderator: Schade, dann wäre dies auch das Ende unserere Runde. Frau Surbier, Herr Hacker für das Erreichen der letzten Runde dürfen sie sich nun etwas wünschen")
            print("Frau Surbier: Ähm ein Toster, eine Blumenvase, so so so'n Kochsatz, Schuhe, \n ein Fragezeichen, ein Doppelpunkt, ein Anführungszeichen oben ähm und ich wünsch mir so ne französische Köchin die mir ein französisches Gericht serviert!")
        elif c == "Herr Hacker":
            print("Herr Hacker: Ein Mann?")
            print("Moderator: Ja")
            print("Herr Hacker: Und der soll lange da gelebt haben? Im Rembrandhaus?")
            print("Herr Hacker: Hat da denn noch jemand drin gewohnt? Hat der untervermietet?")
            print("Moderator: Wer denn?")
            print("Herr Hacker: Naja der der der Hauptmieter da, der der Rembrandt")
            print("Moderator: Absolut Korrekt und damit sind sie der Hauptgewinner dieses Abends! (Applaus und Siegesklang)")
        else:
            print("Schweigen...")
            print("Moderator: Nun ich nehme ihr Schweigen als Antwort wahr. Dies Beendet dann auch unsere Runde!")
    else:
        print("Schweigen...")
        print("Moderator: Nun ich nehme ihr Schweigen als Antwort wahr. Dies Beendet dann auch unsere Runde!")
else:
    print("Schweigen...")
    print("Moderator: Nun ich nehme ihr Schweigen als Antwort wahr. Dies Beendet dann auch unsere Runde!")
    
