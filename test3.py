a=[]
b=[]
c=[]
for _ in range(int(input())):
   name = input()
   score = float(input())
   a.append(score)
   b.append([name,score])

print(a)
sorted_a=sorted(a)
unique_sorted_a=sorted(set(sorted_a))
print(unique_sorted_a)
second_lowest_marks=unique_sorted_a[1]

for i in range(len(b)):
   if b[i][1]==second_lowest_marks:
      c.append(b[i][0])
   
sorted_name=sorted(c)
print (sorted_name)