"""
chr(x) 返回整数x在ASCII码表对应的字符。参数x范围是0~255的整数，可以是二进制，十进制，十六进制
ord(c) 返回字符c在ASCII码表对应的数值。返回值是十进制数
ASCII码表 ：
https://tool.ip138.com/ascii_code/

"""
print(chr(48))
print(chr(0x30))    # “0x”表示16进制，数字0

print(ord('a'))