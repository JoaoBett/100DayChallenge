import random

print("Welcome to the Maze Runner\n\n")

maze = [
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
    ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', ' ', '#', ' ', '#', '#', ' ', '#'],
    ['#', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', ' ', '#', '#', '#', '#', '#', '#', ' ', '#'],
    ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
]

#Starting position
player_X=1
player_Y=1

#Exit position
exit_X=random.randint(0,len(maze[0])-1)
exit_Y=random.randint(0,len(maze)-1)
maze[exit_Y][exit_X]='G'

print("You are on a Maze and you need to find the exit!\n")
input("")

def at_end():
    return maze[player_Y][player_X]=='G'

def move(x,y):
    maze[y][x]= ' '
    maze[player_Y][player_X] = '*'
    return y,x

def turn_left(x,y):
    if maze[y][x-1] == ' ':
        return x-1,y
    return y,x

def turn_right(x,y):
    if maze[y][x+1] == ' ':
        return y,x+1
    return y,x

def turn_up(x,y):
    if maze[y-1][x] == ' ':
        return y-1,x
    return y,x

def turn_down(x,y):
    if maze[y+1][x] == ' ':
        return y+1,x
    return y,x

while not at_end():
    for row in maze:
        print("".join(row))

    if player_X < exit_X:
        player_X, player_Y = turn_right(player_X,player_Y)
    if player_X > exit_X:
        player_X, player_Y = turn_left(player_X,player_Y)
    if player_Y < exit_Y:
        player_X, player_Y = turn_down(player_X,player_Y)
    if player_Y > exit_Y:
        player_X, player_Y = turn_up(player_X,player_Y)

    player_Y, player_X = move(player_X,player_Y)

    if at_end():
        print("Congratulations you have found the exit!\n\n")

input("\nPress any key to continue...")