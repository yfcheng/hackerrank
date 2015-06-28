class Node(object):
    def __init__(self):
        self.value = ""
        self.neighbours = []

objs = []

s_node = Node() 
s_node.value = "s"

e_node = Node() 
e_node.value = "e"

n_node = Node() 
n_node.value = "n"

t_node = Node() 
t_node.value = "t"

h_node = Node() 
h_node.value = "h"

r_node = Node() 
r_node.value = "r"

i_node = Node() 
i_node.value = "i"

l1_node = Node() 
l1_node.value = "l"

l2_node = Node() 
l2_node.value = "l"

s_node.neighbours.append(e_node) 
s_node.neighbours.append(h_node)

e_node.neighbours.append(s_node) 
e_node.neighbours.append(n_node) 
e_node.neighbours.append(t_node)

h_node.neighbours.append(s_node) 
h_node.neighbours.append(t_node) 
h_node.neighbours.append(l1_node) 
h_node.neighbours.append(i_node)

t_node.neighbours.append(e_node) 
t_node.neighbours.append(n_node) 
t_node.neighbours.append(h_node) 
t_node.neighbours.append(r_node)

n_node.neighbours.append(e_node) 
n_node.neighbours.append(t_node) 
n_node.neighbours.append(r_node)

r_node.neighbours.append(t_node) 
r_node.neighbours.append(n_node) 
r_node.neighbours.append(i_node)

l1_node.neighbours.append(h_node)

l2_node.neighbours.append(i_node)

i_node.neighbours.append(h_node) 
i_node.neighbours.append(r_node) 
i_node.neighbours.append(l2_node)

objs.append(s_node)
objs.append(e_node)
objs.append(n_node)
objs.append(t_node)
objs.append(h_node)
objs.append(r_node)
objs.append(i_node)
objs.append(l1_node)
objs.append(l2_node)

print s_node.neighbours
print e_node.neighbours


def find_string(curr,search,idx):
    if idx >= len(search):
        return True
    if curr.value != search[idx]:
        return False
    for next in curr.neighbours:
        if find_string(next,search,idx+1):
            return True
    return False


if __name__ == "__main__":
    
    print find_string(objs[0],"senthil",0)
    print find_string(objs[0],"sht",0)
    print find_string(objs[0],"setd",0)
    print find_string(objs[0],"setrihl",0)
    print find_string(objs[0],"setrihlm",0)
    print find_string(objs[0],"sentr",0)
    print find_string(objs[0],"sethirne",0)
    print find_string(objs[0],"deepa",0)
    print find_string(objs[0],"ssssss",0)
