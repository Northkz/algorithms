def Selection_sort_maxtomin( head):
        l=len(head)
        for i in range(0,l):
                max=i
                for j in range(i+1,l):
                        if head[max]<head[j]:
                                max=j
                if max!=i:
                        head[max],head[i]=head[i],head[max]
        return head
def selection_sort_mintomax(head):
        l=len(head)
        for i in range(0,l):
                minim=i
                for j in range(i+1,len(head)):
                        if head[j]<head[minim]:
                                minim=j
                if min!=i:
                        head[minim],head[i]=head[i],head[minim]
        return head

print(Selection_sort_maxtomin([5,3,6,9,7,0,0,1,98]))
print(selection_sort_mintomax([5,3,6,9,7,0,0,1,98]))