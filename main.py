from random import random
def word_search_maker(array,columns,rows):
    _1_row = ["_"]*columns
    grid = [_1_row]*rows
    print(grid)

if __name__ == "__main__":
    array = ["red","blue","yellow","orange", "purple","grey", "black","white"]
    columns = 10
    rows = 10
    word_search_maker(array,columns,rows)

