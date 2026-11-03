# class Solution:

#     # def countDigit(self,n):
#     #     count=0
#     #     while n>0:
#     #         n=n//10
#     #         count+=1
#     #     return count
#     def decToBinary(self, n):
#         # code here
        
#         binary=""
#         # power=f1.countDigit(n)
        
#         while n>0:
#             a=n%2
#             binary=str(a*(2**power))+binary
#             power-=1
#             n=n//2
#         print(binary)
#         return binary

# n=int(input("Enter the number: "))
# f1=Solution()
# # f1.countDigit(n)
# f1.decToBinary(n)



class Solution:
    def binary(self,n):
        binary=""
        count=-1
        while n>0:
            r=n%2
            binary=str(r)+binary
            n=n//2
            count+=1
        return binary


    # def calculate_binary(result):

    def binary_cal(self,n):
            binary=""
            power=int(binary(n))
            while n>0:
                r=n%2
                bin=str(r*(2**power))+bin
                power-=1
                n=n//2
                count+=1
            return bin




n=int(input("Enter a number: "))
f1=Solution()
# result,binary_num=f1.binary(n)
result=f1.binary(n)
print(result)
# print(binary_num)
final=f1.binary_cal(n)