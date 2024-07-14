def create_album(artists, albums, songs=None):
    new_user_album = {
        'artist': artists.title(),
        'album': albums.title(),
    }
    if songs:
        new_user_album['song_amount'] = int(songs)
    print('\n', new_user_album)


# loop flag
input_artists = True

while input_artists:
    print("Type 'quit' at any time to exit the program.")
    user_songs = 0
    user_artist = input('Enter the artist name: ')
    if user_artist == 'quit':
        break
    user_album = input('Enter the album name: ')
    if user_album == 'quit':
        break
    user_songs_decision = input('Display album song amount? y/n: ')
    if user_songs_decision == 'quit':
        break
    elif user_songs_decision == 'y':
        user_songs = input('Enter album song amount: ')

    # if the user wanted to display album song amount
    # then include user_songs in parameters
    if user_songs_decision == 'y':
        create_album(user_artist, user_album, user_songs)
    # otherwise nothing is passed for that value
    else:
        create_album(user_artist, user_album)


