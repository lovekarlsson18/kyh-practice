"""def wordcount():
    text = input("Skriv en mening: ").split()
    print(f"Du skrev {len(text)} ord")"""

"""def vokaler_uppg():
    intervju = """– Det är en slags inflammatorisk skada i ryggmärgen. Det kan orsakas av infektioner, inflammationer eller liknande, säger Matti Sällberg, biomedicinsk analytiker och professor vid Karolinska universitetet.
Om försökpersonens sjukdom är en biverkning av vaccinet är ännu för tidigt att slå fast.
– Man ska ha klart för sig att när man vaccinerar så pass många som man gör i dessa studierna, kanske 10 000, 30 000 eller 50 000 personer, så är det inte konstigt om sådant här inträffar helt oberoende av vaccinationen.
"""
    vokaler = "a,e,i,o,u,y,å,ä,ö"
    count = 0

    for char in intervju:
        if char in vokaler:
            count += 1

    print(count)
"""


if __name__ == '__main__':
    wordcount()

