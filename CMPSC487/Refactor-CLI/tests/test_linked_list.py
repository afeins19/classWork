import sys 
sys.path.append('/Users/aaronfeinberg/Projects/Refactor-CLI/')

from assignmentlistssolutions import Node, DoublyLinkedList

# creating and populating a doubly linked list #dlL should have 4 elements!!!!!!!
dL = DoublyLinkedList()

for i in range(4):
    dL.add_last(Node(i))

def test_sobv():
    assert 1 == 0+1

# Testing Node Creation 
def test_node_creation():
    n = Node(1) 
    assert n.get_element() == 1 

# Testing Size 

def test_doubly_linked_list_size():
    assert dL.size() == 4

# Testing Retrieving Itens

def test_doubly_linked_list_get_first():
    assert str(dL.get_first()) == f"(0, (1, (2, (3, ('Trailer', None)))))"

def test_doubly_linked_list_get_last():
    assert str(dL.get_last()) == f"(3, ('Trailer', None))"

def test_doubly_linked_list_get_previous():
    assert str(dL.get_last().get_previous()) == "(2, (3, ('Trailer', None)))"

def test_doubly_linked_list_get_next():
    assert str(dL.get_first().get_next()) == "(1, (2, (3, ('Trailer', None))))"

# Testing Adding Items

def test_doubly_linked_list_add_sequence():
    dL.add_after(Node(42),dL.get_first())
    dL.add_before(Node(34),dL.get_last())

    assert str(dL) == "(0, (42, (1, (2, (34, (3, ('Trailer', None)))))))"

def test_doubly_linked_list_add_first_add_last():
    dL.add_first(Node(7))
    dL.add_last(Node(-1))

    assert str(dL) == "(7, (0, (42, (1, (2, (34, (3, (-1, ('Trailer', None)))))))))"

# Testing Node Removal

def test_doubly_linked_list_node_removal():
    dL.remove(dL.get_first())
    print(dL.get_first())
    assert dL.get_first().get_element() == 0

# Testing Mapping 

def test_doubly_linked_list_mapping():
    dL.map(lambda x: x**2)
    assert str(dL) == "(0, (1764, (1, (4, (1156, (9, (1, ('Trailer', None))))))))"


def test_doubly_lniked_list_twenties():
    LL = DoublyLinkedList()

    for t in range(20,30):
        LL.add_last(Node(t))
    LL.map(lambda x: x+10)

    assert str(LL) == "(30, (31, (32, (33, (34, (35, (36, (37, (38, (39, ('Trailer', None)))))))))))"


