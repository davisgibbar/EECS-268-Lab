"""
Takes in file name from user and runs code from other class
"""

from executive import Executive


def main():
    file_name = input("Enter the name of the input file: ")
    my_exec = Executive()
    my_exec.file_name(file_name)

main()