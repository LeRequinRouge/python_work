# 8-3 standard positional and keyword parameters
def make_shirt(size, message):
    print(f"\nYour shirt is of size: {size},"
          f"\nand reads: {message}!")


make_shirt('small', "Hello, World")
make_shirt(message='Off the Wall', size='medium')

# 8-4 default value modification
def make_shirt_modified(size='large', message='i love python'):
    print(f"\nYour shirt is a {size} and reads: {message.upper()}!")


make_shirt_modified()
make_shirt_modified('medium')
make_shirt_modified('small', 'i wear tiny shirts')