import random
#from pyvis.network import Network
import pyvis

net = pyvis.network.Network(height=800,width=800,layout=True)

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_node(self, data):
        if self.data:
            if data < self.data:
                if self.left:
                    self.left.add_node(data)
                else:
                    self.left=Node(data)
            elif data > self.data:
                if self.right:
                    self.right.add_node(data)
                else:
                    self.right=Node(data)

    def print_all(self):
        print(self.data)
        if self.left: self.left.print_all()
        if self.right: self.right.print_all()

    #BFS
    def print_lvl(self):
        que=[]
        q={}
        s=1
        #adding tou queue tree node, number of level and current node data
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
            #net.add_node(tmp[2])
            #net.add_node((tmp[0].data))
            #net.add_edge(tmp[2],tmp[0].data)
        for i,j in q.items():
            '''
            net.add_node(i)
            for x in j:
                for y in x:
                    net.add_node(y)
                    '''
            if i!=1:
                print('Level ',i,': ',*[','.join(str(x) for x in j)],sep='')
            else:
                print('Level 1:', self.data)




x=int(input('Podaj ilość wezłów: '))
y=set()
y.add(random.randrange(1,x+1))

drzewo = Node(next(iter(y)))
while len(y)<x:
#for k in range(x):
    z=random.randrange(1,x+1)
    drzewo.add_node(z)
    y.add(z)
    #print(len(y))



drzewo.print_lvl()
#print(net.get_nodes())
net.options.physics.enabled = False
net.show_buttons()

net.show('test.html')


