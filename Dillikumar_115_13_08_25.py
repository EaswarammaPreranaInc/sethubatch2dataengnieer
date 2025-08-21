# s=str(input("enter string :"))
# #kumar
# # s="RaMA  rAo".upper()
# vowels="AEIOUaeiou"
# res=""
# for ch in s:
#     if ch in vowels and ch not in res:
#          res=res+ch+" "
# print("vowels in above string are :",res)
        

# s=input("enter string :")
# #kumar
# # s="RaMA  rAo".upper()
# vowels="AEIOUaeiou"
# cnt=0
# res=""
# for ch in s:
#     if ch in vowels and ch not in res:
#          res=res+ch+" "
#          cnt=cnt+1
# print("vowels in above string are :",res)
# print(f"count of vowels in '{s}' is {cnt} times ")
        
s=input("enter string :").upper()
vowels="AEIOU"
res=""
for ch in s:
    if ch in vowels and ch not in res :
        
        res=res+ch
        #
        # 
        # 
        # print(f"vowels in string '{s}' are : {res}")
        print(f"{ch} is {s.count(ch)} times")
    
    