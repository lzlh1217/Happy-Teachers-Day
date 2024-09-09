import pyfiglet


def generate_ascii_art(text, font='banner3-D', fill_char='#', background_char=' '):
    ascii_art = pyfiglet.figlet_format(text, font=font)
    
    ascii_art = ascii_art.replace(' ', background_char).replace('#', fill_char)
    
    return ascii_art

text = "Happy Teachers' Day, Mr. Wang"

ascii_art = generate_ascii_art(text, font='banner3-D', fill_char='#', background_char=' ')
print(ascii_art)
