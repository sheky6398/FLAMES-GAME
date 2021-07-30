name1=list(input("Enter Your Name: ").lower())
name2=list(input("Enter Your Partner's Name: ").lower())
count=0

for i in name1[:]:
    
    if i in name2:
        name1.remove(i)
        name2.remove(i)
count=len(name1)+len(name2)
        

flames=['Friends','Love','Affection','Marriage','Enemy','Siblings']
i=0
current_count=0
while len(flames)>1:
    if current_count==count-1:
        flames.pop(i)
        current_count=0
    i=(i+1)%len(flames)
    current_count+=1
print(flames)
#end
        
        
