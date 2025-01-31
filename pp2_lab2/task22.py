#union=|(type not main) intersection=&(type main) update,intersection_update   
# difference=-(type main) difference_update,symmetric_difference=^(type main)
# symmetric_difference_update()
s1={1,2,3}
s2={"a","b","c"}
print(s1.union(s2))
res=s1.union(s2)
print(res)
print(s1|s2)
s3={"qwe","rty","uio"}
s4={"!","@","$"}
print(s2.union(s1,s3,s4))
print(s1|s2|s3|s4)
res1=s1.update(s2)
print(res1)
print(s1)
a=[11,22,33]
print(s1.symmetric_difference_update(a))
print(s1)