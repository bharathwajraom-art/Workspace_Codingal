grade={
    "bharath":100,
    "waj":92,
    "rao":87,
    "sunitha":30,
    "balagi":55    
}
total=0
for score in grade.values():
    total=total+score
avg=total/len(grade)
print(f"class avg:{avg:.2f}")
top_stud=max(grade,key=grade.get)
bottom_stud=min(grade,key=grade.get)
print(f"top_stud:{top_stud} with {grade[top_stud]}marks")
print(f"bottom_stud:{bottom_stud} with {grade[bottom_stud]}marks")
name=input("enter a stud name ")
score=grade.get(name)
if score is not None:
    print(f"{name}'s score is {score}")
else:
    print("student name not found")
