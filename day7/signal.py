
from treelib import Node, Tree

tree = Tree()
tree.create_node(identifier='/', data=0)

with open('day7/input.txt') as f:
    current_direc = '/'
    for line in f:
        print(current_direc)
        if line.startswith('$'):
            if 'cd' in line:
                if '..' in line:
                    print(current_direc, tree.parent(current_direc).identifier)
                    current_direc = tree.parent(current_direc).identifier
                    # include entire string except everything after last slash
                    # current_direc = current_direc[:current_direc.rfind('/')]
                else:
                    print(line.strip().split(' ')[2], 'BOB')
                    new_direc = line.strip().split(' ')[2]

                    if new_direc == '/':
                        current_direc = '/'
                    elif current_direc == '/':
                        current_direc = current_direc + line.strip().split(' ')[2]
                    else:
                        current_direc = current_direc + '/' + line.strip().split(' ')[2]
        else:
            identif = line.strip().split(' ')[1]
            number = line.strip().split(' ')[0]
            if number == 'dir':
                number = 0

            if current_direc == '/':
                tree.create_node(identifier=current_direc+identif, parent=current_direc, data=number)
            else:
                tree.create_node(identifier=current_direc+'/'+identif, parent=current_direc, data=number)


            print(current_direc)
            

def set_size(node):
    if tree.children(node.identifier):
        total_data = 0
        for child in tree.children(node.identifier):
            total_data += set_size(child)
        node.data = str(total_data)
        return total_data
    else:
        # print(node.data)
        return int(node.data)
        

set_size(tree.get_node('/'))
print(tree.show())


min_size = 0

# # print out tree with data
for node in tree.all_nodes():
    # if node has children
    if tree.children(node.identifier):
        if int(node.data) > 3636666:
            print(node.identifier, node.data)
            if int(node.data) < min_size or min_size == 0:
                min_size = int(node.data)



print(min_size)