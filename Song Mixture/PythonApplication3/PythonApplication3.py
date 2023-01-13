print("Song mixture depending on Chords")
user=input("Which instrument you would like to play: ").lower()
if user=="guitar":
    print("Great choice!!")
elif user=="keyboard":
    print("Great choice!!")
else:
    print("Other instruments sheet is still upgrading.")
songs=[]
song1=input("Which song would you like to add: ").upper()
scale1=input("On what scale it is: ").upper()
song2=input("Which song would you like to add: ").upper()
scale2=input("On what scale it is: ").upper()
if scale1==scale2:
    songs.append(song1)
    songs.append(song2)
    chords1=input("What are the chords of song 1: ").upper()
    chords2=input("What are the chords of song 2: ").upper()
    if chords1=="E" and chords2=="G":
        print("The songs cann be collaberated")
    print(songs)
else:
    print("Sorry!! The songs are on different scale.")