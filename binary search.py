def m(arr):
        if len(arr)>1:
                mid=len(arr)//2
                left_arr=arr[:mid]
                right_arr=arr[mid:]
                m(left_arr)
                m(right_arr)
                i=0
                j=0
                k=0
                while i<len(left_arr) and j<len(right_arr):
                        if left_arr[i]<right_arr[j]:
                                arr[k]=left_arr[i]
                                i+=1
                                k+=1
                        else: 
                                arr[k]=right_arr[j]
                                j+=1
                                k+=1
                while i<len(left_arr):
                        arr[k]=left_arr[i]
                        i+=1
                        k+=1
                while j<len(right_arr):
                        arr[k]=right_arr[j]
                        j+=1
                        k+=1
        return arr
def bin_search(arr,num):
        begin=0
        end=len(arr)-1
        while begin<=end:
                mid=begin+(end-begin)//2
                mid_value=arr[mid]
                if mid_value==num:
                        return mid
                elif mid_value<num:
                        begin=mid+1
                else:
                        end=mid-1
        return None
nur=[5,3,6,9,7,0,0,1,98]
m(nur)
print(nur)
num=input("num ")
print(bin_search(nur,int(num)))
