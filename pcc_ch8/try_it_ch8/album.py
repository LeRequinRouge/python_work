def make_album(artists, albums, songs=None):
    new_album = {
        'artist': artists,
        'album': albums,
    }
    if songs:
        new_album['song_amount'] = songs
    return new_album


print(make_album('randicious', 'forever none', songs=12))
print(make_album('as the crow flies', 'murder me slowly'))
print(make_album('tencil town', 'short-stack', songs=7))