def make_album(artist_name, album_title, songs = None):
    album = {'Artist_name':artist_name, 'Album_title':album_title}

    if songs:
        album['Songs'] = songs

    return album

album_1 = make_album('Imagine Dragons','Art Film')
album_2 = make_album('Phoenix','SATV', 53)
album_3 = make_album('Jah Prayzah','MUDHARA ACHAUY')
print(album_1)
print('********************************************************')
print(album_2)
print('********************************************************')
print(album_3)
