def insertionSortList( head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a=len(head)
        for i in range(1,a):
                minim=head[i]
                while head[i-1]>minim and i>0:
                        head[i],head[i-1]=head[i-1],head[i] 
                        i=i-1
        return head
print(insertionSortList([5,3,6,9,7,0,1,98]))