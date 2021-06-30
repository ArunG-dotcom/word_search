from random import randrange
from random import choice
from sys import exit

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
directions = {'NW': [-1,-1],'N':[0,-1],'NE':[1,-1],'E': [1,0],'SE':[1,1],'S':[0,1], 'SW': [-1,1], 'W': [-1,0]} # need to add directions along with coordinates that corespond with directions to place each word in the grid
config = open('config.txt', 'r')
config_list = config.read().split("\n")


print(config_list)
config.close()



length = int(config_list[0])
height = int(config_list[1])
word_list = config_list[2:]

#creates random_letters
random_letters = lambda: alphabet[randrange(25)]
# creates random_coordinates with respect to length and height
random_coords = lambda: (choice(range(length)), choice(range(height)))
#creates a new grid with length and height
new_grid = lambda: [["" for _ in range(length)] for _ in range(height)]
# checks if the words in config.txt fit in the 10X10 grid
for word in config_list:
    if len(word) >= length:
        exit("You have entered an inavlid input. Please try again")

#check starting point, ensure it will fit on the board
def check_if_word_fits_on_grid(word, grid,direction):
    """
    word = string: represents a word that needs to be added to the grid
    grid = nested lists: Inner lists are rows
    direction = string: Can be used with directiosn mapped to retrieve distance between letters
    """
    starting_point = random_coords()
    current_point = starting_point

    for letter in word:
        row = current_point[1]
        column = current_point[0]
        try:
            current_element = grid[row][column]
            if current_element == "" or current_element == letter:
                d_tup = directions[direction]
                current_point = (column + d_tup[0], row + d_tup[1])
                if current_point[0] < 0 or current_point[1]<0:
                    return False
            else:
                return False
        except:
            return False
    # if not check for a new starting point until you find one that fits
    return starting_point


#add the word to the grid based on the starting point
def put_word_into_the_grid(word, grid, direction, starting_point):
    """
    word = string: represents a word that needs to be added to the grid
    grid = nested lists: Inner lists are rows
    direction = string: Can be used with directision mapped to retrieve distance between letters
    starting_point = (int,int): First starting point
    """
  
    d_tup = directions[direction]
    #breakpoint()
    try:
        for letter in word:
            row = starting_point[1]
            column = starting_point[0]
            grid[row][column] = letter
        
            starting_point = (column + d_tup[0], row + d_tup[1])
    except:
        return False


#check every location in grid, replace all the empty string with random letters
#for getting random letter, use random_letters lamda function
def fill_grid_with_random_letters(grid):
    """
    grid = nested lists: Inner lists are rows
    """

    for row in range(length):
        for column in range(height):
            grid[row][column] = choice(alphabet)


    return grid


#making the grid look more profound or more like an array
def perfecting_grid(grid):
    for nested_lists in grid:
        print(" ".join(nested_lists))
    return None


if __name__ == "__main__":
    pass
    grid = new_grid()
    #for each word, check if the word fits in the grid if so put it into the grid
    for word in word_list:
        counter = 0
        while counter < 500:
            counter += 1
            storing_directions = choice(list(directions.keys()))
            starter = check_if_word_fits_on_grid(
                                            word,
                                            grid,
                                            storing_directions,
                                                )
            if starter:
                put_word_into_the_grid(word, grid, storing_directions, starter) 
                break  
        #breakpoint()
        if counter == 500:
            print("error, grid is too short")
    fill_grid_with_random_letters(grid)
    perfecting_grid(grid)
    #new_config_list = [string.replace("'","") for string in config_list]
    #new_config_list = [string.replace("'","") for string in config_list]
    print("word_bank:")
    print("\n".join(config_list))