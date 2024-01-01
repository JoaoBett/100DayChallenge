number = [1,2,3]

new_numbers = [n+1 for n in number]

new_range = [n_linha*2 for n_linha in range(1,5)]

#Variable_Name = (list)[(what's in your for loop) "for" item in (List,tuple,...)]

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

caps_names = [name.upper() for name in names if len(name) > 5]