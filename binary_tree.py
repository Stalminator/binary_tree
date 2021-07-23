import random
#from pyvis.network import Network
import pyvis

net = pyvis.network.Network(height=800,width=2000,layout=True)
net.options.physics.enabled = False
net.options.layout.hierarchical.sortMethod = 'directed'

class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.q={}

    def add_node(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.add_node(data)
                else:
                    self.left=BinaryTree(data)
            elif data > self.data:
                if self.right:
                    self.right.add_node(data)
                else:
                    self.right=BinaryTree(data)
        else: self.data=data

    def print_all(self):
        print(self.data)
        if self.left: self.left.print_all()
        if self.right: self.right.print_all()

    #BFS and adding nodes
    def nodes_setup(self):
        que=[] #queue to allow obtain tree level
        #q={} #dic to store all nodes at specific level
        #adding to queue tree node, first level and data node
        que.append((self,1,self.data))
        while len(que)>0:
            tmp=que.pop()
            net.add_node(self.data)
            if tmp[0].left:
                que.append((tmp[0].left,tmp[1]+1,tmp[0].data))
                net.add_node(tmp[0].left.data,color='Blue')
                net.add_edge(tmp[0].data,tmp[0].left.data)
            if tmp[0].right:
                que.append((tmp[0].right,tmp[1]+1,tmp[0].data))
                net.add_node(tmp[0].right.data,color='Green')
                net.add_edge(tmp[0].data,tmp[0].right.data)

            self.q[tmp[1]] = self.q.get(tmp[1],[]) + [(tmp[2],tmp[0].data)]

    def print_lvls(self):
        for i,j in self.q.items():
            if i!=1:
                print('Level ',i,': ',*[','.join(str(x) for x in j)],sep='')
            else:
                print('Level 1:', self.data)

    def create_graph(self,x):
        y=set()
        while len(y) < x:
            z = random.randrange(1, x + 1)
            self.add_node(z)
            y.add(z)

drzewo = BinaryTree()
drzewo.create_graph(int(input('Podaj ilość węzłów: ')))
drzewo.nodes_setup()
#drzewo.print_lvls()

#net.show_buttons()

net.show('test.html')


