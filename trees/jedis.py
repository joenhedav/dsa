from arbol_binario import BinaryTree, get_value_from_file

file_jedi = open('/home/m0rphine/me/dsa/trees/jedis.txt')
read_lines = file_jedi.readlines()
file_jedi.close()

# punto a 
name_tree = BinaryTree()
ranking_tree = BinaryTree()
specie_tree = BinaryTree()

read_lines.pop(0)
for index, line_jedi in enumerate(read_lines):
    jedi = line_jedi.split(';')
    jedi.pop()
    # punto a
    name_tree.insert_node(jedi[0], index+2)
    ranking_tree.insert_node(jedi[1], index+2)
    specie_tree.insert_node(jedi[2], index+2)

# punto b 
print('inorden nombre')
name_tree.inorden()
print()
print('inorden ranking')
ranking_tree.inorden_file('jedis.txt')
print()
# punto c 
print('by_level ranking')
ranking_tree.by_level()
print()
print('by_level especie')
specie_tree.by_level()

# punto d 
print('\ninfo yoda')
index = name_tree.search('yoda')
if index:
    print(get_value_from_file('jedis.txt',index.other_values))
else:
    print('yoda no esta en la lista')

print('\ninfo luke skywalker')
index = name_tree.search('luke skywalker')
if index:
    print(get_value_from_file('jedis.txt',index.other_values))
else:
    print('luke skywalker no esta en la lista')
# punto e 
print('\njedis masters')
name_tree.inorden_jedi_master('jedis.txt','jedi master')
# punto f 
print('\nsable de luz verde')
name_tree.inorden_green_lightsaber('jedis.txt','green')
# punto g
print('\njedis con maestro')
name_tree.inorden_with_master('jedis.txt')
# punto h
spicies_name = ['togruta','cerean']
print('\njedis de la especie togruta o cerean')
name_tree.inorden_by_spicie('jedis.txt',spicies_name)
# punto i 
print('\njedis que contienen letra a en el nombre')
name_tree.inorden_start_with_jedi('A')
print('\ncontienen - en el nombre')
name_tree.inorden_contain_hypen('-')










