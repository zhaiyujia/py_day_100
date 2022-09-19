'''
练习1：在屏幕上显示跑马灯文字。
'''
import os
import time


def main():
    content = '北京欢迎你为你开天辟地…………'
    while True:
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()