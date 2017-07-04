#-*- coding:utf-8 -*-

from sys import argv

script, input_file = argv

def print_all(f):
    # 读出文件所有内容
    print f.read()


def rewind(f):
    # 回到文件开头
    f.seek(0)

def print_a_line(line_count, f):
    # 打印一行
    print line_count, f.readline()


current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind, kind of like a tape."
rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# line number plus 1
current_line = current_line + 1
# print the current line
print_a_line(current_line, current_file)
