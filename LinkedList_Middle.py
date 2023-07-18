class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def push_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def push_back(self, data):
        if self.head:
            temp = self.head
            while temp.next:
                temp = temp.next
            new_node = Node(data)
            temp.next = new_node
        else:
            self.head = Node(data)
    
    def getLen(self):
        temp = self.head
        cnt = 0
        while temp:
            cnt += 1
            temp = temp.next
        return cnt
    
    # Brute Force Method-------------
    # def getMiddle(self):
    #     temp = self.head
    #     mid = self.getLen()//2
    #     while mid:
    #         temp = temp.next
    #         mid -= 1
    #     return temp.data
    
    # Concept Of Fast And Slow Pointers----------
    def getMiddle(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data
                   
    def Print_List(self):
        temp = self.head
        print("LinkedList:-  ",end="")
        while temp:
            print(temp.data," ",end="")
            temp = temp.next
        print()

llist1 = LinkedList()
llist2 = LinkedList()
# for i in range(1, 6):
#     llist1.push_front(i)
#     llist1.Print_List()

# print(llist1.getLen())
# print(llist1.getMiddle())

for i in range(1,6):
    llist2.push_back(i)
llist2.Print_List()

print("Length:-", llist2.getLen())
print("Middle Element:-", llist2.getMiddle())