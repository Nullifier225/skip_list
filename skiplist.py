import random as rand
import math
from vpython import *

class skiplist:
    class node:
        def __init__(self):
            self.data = None 
            self.up = None
            self.down = None
            self.next = None
            self.box = None
            self.nextarr = None
            self.uparr = None
            self.downarr = None
            self.label = None
  
    def __init__(self):
        self.head = self.node()
        self.head.data = -math.inf
        self.head.box = box(pos=vector(-10,0,0),size=vector(1,1,1),color = color.green)

    def construct(self,elements):

        tempHead = self.head

        elements.sort()

        #CREATING THE ZEROTH LEVEL OF NODES
        for ele in elements:
            rate(4)
            n = self.node() 
            n.box = box(pos=tempHead.box.pos + vector(3,0,0),size=vector(1,1,1),color = color.green)
            n.data = ele
            n.label = label(pos = n.box.pos, text = str(n.data))
            tempHead.next = n  
            tempHead.nextarr = arrow(pos = tempHead.box.pos, axis = n.box.pos - tempHead.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
            tempHead = tempHead.next
    
        #CREATING SUBSEQUENT LAYERS
        tempHead = self.head
        ctr =1
        while(self.length(tempHead)>1):
            rate(4)
            n = self.node()
            n.box = box(pos=tempHead.box.pos + vector(0,3,0),size=vector(1,1,1),color = color.green)
            n.data = -math.inf
            n.label = label(pos = n.box.pos, text = str(n.data))
            tempHead.up = n
            tempHead.uparr = arrow(pos = tempHead.box.pos, axis = n.box.pos - tempHead.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
            n.down = tempHead
            n.downarr = arrow(pos = n.box.pos, axis = tempHead.box.pos - n.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
            tempHead2 = tempHead.up
            curlevelHead = tempHead
            newLevelHead = tempHead2
            while(curlevelHead.next!=None):
                curlevelHead = curlevelHead.next
                curlevelHead.box.color = color.red
                rate(2)
                if(rand.randrange(2)):
                    nn = self.node()
                    nn.box = box(pos=curlevelHead.box.pos + vector(0,3,0),size=vector(1,1,1),color = color.green)
                    nn.data = curlevelHead.data
                    n.label = label(pos = n.box.pos, text = str(n.data))
                    curlevelHead.up = nn
                    curlevelHead.uparr = arrow(pos = curlevelHead.box.pos, axis = nn.box.pos - curlevelHead.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
                    newLevelHead.next = nn
                    newLevelHead.nextarr = arrow(pos = newLevelHead.box.pos, axis = nn.box.pos - newLevelHead.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
                    nn.down = curlevelHead
                    nn.downarr = arrow(pos = nn.box.pos, axis = curlevelHead.box.pos - nn.box.pos, color = color.white, shaftwidth=0.1, headwidth =0.2)
                    newLevelHead = newLevelHead.next
                curlevelHead.box.color = color.green
            tempHead = tempHead2
            if(self.length(tempHead)==0):
                tempHead.down.uparr.visible = False
                del tempHead.down.uparr
                tempHead.downarr.visible = False
                tempHead.label.visible = False
                tempHead.box.visible = False
                del tempHead   
                break
            ctr+=1
            
            ###################################END OF CONSTRUCTION##########################################

    def insert(self,value):
        top = self.head
        n = self.node()
        n.data = value
        l = []
        while(top!=None):
            l.append(top)
            top = top.up

        top = None
        for i in range(len(l)):
            top = l[len(l)-i-1]

            while(top.next!=None):
                top.box.color = color.red
                rate(2)
                if(top.next.data>=value):
                    l[len(l)-i-1] = top
                    break
                top.box.color = color.green
                top = top.next
            
            if(top.next==None and top.data<value):
                top.box.color = color.red
                l[len(l)-i-1] = top
        
        if(l[0].next!=None and l[0].next.data != value):
            #MOVING ALL THE OBJECTS AND ARROWS
            rate(2)
            movenode = l[0].next
            while(movenode!=None):
                movenode.box.pos += vector(3,0,0)
                movenode.label.pos += vector(3,0,0)
                if(movenode.nextarr):
                    movenode.nextarr.pos += vector(3,0,0)
                if(movenode.uparr):
                    movenode.uparr.pos += vector(3,0,0)
                movnup = movenode.up
                while(movnup!=None):
                    movnup.box.pos += vector(3,0,0)
                    if(movnup.uparr):
                        movnup.uparr.pos += vector(3,0,0)
                    if(movnup.nextarr):
                        movnup.nextarr.pos += vector(3,0,0)
                    movnup.downarr.pos += vector(3,0,0)
                    movnup = movnup.up    
                movenode = movenode.next
            #END OF MOVING VISUALLY
            
            temp = l[0].next
            l[0].next = n
            n.next = temp
            n.box = box(pos = l[0].box.pos + vector(3,0,0), size=vector(1,1,1), color= color.green)
            n.nextarr = arrow(pos = n.box.pos, axis = n.next.box.pos - n.box.pos, shaftwidth = 0.1, color= color.white, headwidth =0.2)
            n.label = label(pos = n.box.pos, text = str(n.data))
            
        elif(l[0].next == None and l[0].data != value):
            n.box = box(pos = l[0].box.pos + vector(3,0,0), size=vector(1,1,1), color= color.green)
            n.label = label(pos = n.box.pos, text = str(n.data))
            l[0].nextarr = arrow(pos = l[0].box.pos, axis = n.box.pos - l[0].box.pos, shaftwidth =0.1, color= color.white, headwidth =0.2)
            l[0].next = n
        #END OF THE FIRST LEVEL
        
        ctr = 1
        while(ctr<len(l) and rand.randrange(2)):
            n = self.node()
            n.box = box(pos = l[ctr-1].next.box.pos+ vector(0,3,0), color = color.green, size=vector(1,1,1))
            n.downarr = arrow(pos = n.box.pos, axis = l[ctr-1].next.box.pos - n.box.pos, color = color.white, shaftwidth = 0.1) 
            l[ctr-1].next.uparr = arrow(pos = l[ctr-1].next.box.pos, axis = n.box.pos - l[ctr-1].next.box.pos,color = color.white,shaftwidth = 0.1, headwidth =0.2)
            n.data = value
            if(l[ctr].next!=None and l[ctr].next.data!=value):
                temp = l[ctr].next
                l[ctr].next = n
                n.next = temp
                l[ctr-1].next.up = n
                n.down = l[ctr-1].next
                n.nextarr = arrow(pos = n.box.pos, axis = n.next.box.pos- n.box.pos, shaftwidth = 0.1, color= color.white, headwidth =0.2)

            elif(l[ctr].next==None and l[ctr].data!=value):
                l[ctr].next = n
                l[ctr-1].next.up = n
                n.down = l[ctr-1].next

            ctr+=1
        ctr = 0    
        while(ctr<len(l)):
            l[ctr].box.color = color.green
            if(l[ctr].next):
                l[ctr].nextarr = arrow(pos = l[ctr].box.pos, axis = l[ctr].next.box.pos - l[ctr].box.pos, color = color.white, shaftwidth=0.1, headwidth = 0.2)
            ctr+=1
        ################################################END OF INSERTION ##########################################
            
    def search(self,value):
        top = self.head
    
        while(top.up!=None):
            top = top.up

        while(True):
            top.box.color = color.red
            rate(2)
            if(top.next!=None and top.next.data==value):
                top.box.color = color.green
                for i in range(10):
                    top.next.box.color = color.red
                    rate(2)
                    top.next.box.color = color.green
                    rate(2)
                return True

            elif(top.next!= None and top.next.data<value):
                top.box.color = color.green
                top = top.next
          
            elif((top.next == None or top.next.data>value) and top.down!=None):
                top.box.color = color.green
                top = top.down

            elif((top.next == None or top.next.data>value) and top.down==None):
                top.box.color = color.green
                return False

          ####################################END OF SEARCH###########################################
       
    def delete(self,value):
        top = self.head
        n = self.node()
        n.data = value
        l = []
        while(top!=None):
            l.append(top)
            top = top.up

        top = None
        for i in range(len(l)):
            top = l[len(l)-i-1]

            while(top!=None):
                rate(2)
                top.box.color = color.red
                if(top.next == None):
                    l[len(l)-i-1] = None
                    rate(2)
                    top.box.color = color.green
                    break
                elif(top.next.data==value):
                    l[len(l)-i-1] = top
                    break
                elif(top.next.data > value):
                    l[len(l)-i-1] = top
                    break

                rate(2)
                top.box.color = color.green
                top = top.next

        for i in range(len(l)):
            top = l[len(l)-i-1]
            if(top == None):
                continue
            if(top.next!=None and top.next.data==value):
                temp = top.next
                top.next=top.next.next
                if(temp.box):
                    temp.box.visible = False
                if(temp.label):
                    temp.label.visible = False
                if(temp.uparr):
                    temp.uparr.visible = False
                if(temp.downarr):
                    temp.downarr.visible = False
                if(temp.nextarr):
                    temp.nextarr.visible = False
                del temp
            
            
            start = top.next
            while(start!= None):
                if(start.box):
                    start.box.pos -= vector(3,0,0)
                if(start.label):
                    start.label.pos -= vector(3,0,0)
                if(start.uparr):
                    start.uparr.pos -= vector(3,0,0)
                if(start.downarr):
                    start.downarr.pos -= vector(3,0,0)
                if(start.nextarr):
                    start.nextarr.pos -= vector(3,0,0)
                start = start.next

            if(top.next):
                top.nextarr.axis = top.next.box.pos - top.box.pos
            else:
                if(top.nextarr):
                    top.nextarr.visible = False
            top.box.color = color.green


    # def printSL(self):
    #     n = self.head
    #     while(n!=None):
    #         ntemp = n
    #         while(ntemp.next!=None):
    #             ntemp = ntemp.next
    #             print(ntemp.data,end = " ")
    #         n = n.up
    #         print()

    def length(self,head):
        toret =0
        while(head.next != None):
            toret+=1
            head = head.next
        return toret


# s = skiplist()
# s.construct([5,8,12,15,25,17,35,40,42,48])
# s.delete(40)
# s.search(25)
# s.insert(30)