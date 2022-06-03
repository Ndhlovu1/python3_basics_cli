def make_album(artist_name, album_title, songs = None):
    album = {'Artist_name':artist_name, 'Album_title':album_title, 'Songs':songs}
    return album

while True:
    print("\nEnter 'q' to Quit")
    print("PLEASE PROVIDE THE FOLLOWING DATA:\n")

    ar_name = input("Artist Name\n")
    if ar_name == 'q':
        break

    ar_album = input("Album Title:\n")
    if ar_album == 'q':
        break


    ar_songs = input("Album Songs:\n")
    if ar_songs == 'q':
        break

    formatted_album = make_album(ar_name, ar_album,ar_album)
    print(formatted_album)


"""
album_1 = make_album('Imagine Dragons','Art Film')
album_2 = make_album('Phoenix','SATV', 53)
album_3 = make_album('Jah Prayzah','MUDHARA ACHAUY')
print(album_1)
print('********************************************************')
print(album_2)
print('********************************************************')
print(album_3)
"""
