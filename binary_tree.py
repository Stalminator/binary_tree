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
    def print_lvls(self):
        que=[]
        q={}
        s=1
        #adding to queue tree node, number of level and current node data
        que.append((self,s,self.data))
        while len(que)>0:
            tmp=que.pop()
            s=tmp[1]
            net.add_node(self.data)
            if tmp[0].left:
                que.append((tmp[0].left,s+1,tmp[0].data))
                net.add_node(tmp[0].left.data,color='Blue')
                net.add_edge(tmp[0].data,tmp[0].left.data)
            if tmp[0].right:
                que.append((tmp[0].right,s+1,tmp[0].data))
                net.add_node(tmp[0].right.data,color='Green')
                net.add_edge(tmp[0].data,tmp[0].right.data)

            q[s] = q.get(s ,[]) + [(tmp[2],tmp[0].data)]

        for i,j in q.items():
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
drzewo.print_lvls()

#net.show_buttons()

net.show('test.html')


