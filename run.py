import pyfiglet

# 生成艺术字并替换为空格为指定符号
def generate_ascii_art(text, font='banner3-D', fill_char='#', background_char=' '):
    # 使用 pyfiglet 生成艺术字
    ascii_art = pyfiglet.figlet_format(text, font=font)
    
    # 替换填充字符和背景字符
    ascii_art = ascii_art.replace(' ', background_char).replace('#', fill_char)
    
    return ascii_art

# 定义要打印的文本
text = "Happy Teachers' Day, Mr. Wang"

# 生成并打印艺术字，使用 banner3-D 字体和 # 号作为填充符号，空格作为背景
ascii_art = generate_ascii_art(text, font='banner3-D', fill_char='#', background_char=' ')
print(ascii_art)
