l1=input("contri and project: ")
contri=int(l1.split()[0])
contri_list={}

project=int(l1.split()[1])
project_list={}

for i in range(contri):
    l2=input("name and skill: ")
    name=l2.split()[0]
    skills=int(l2.split()[1])
    contri_skill={}
    for j in range(skills):
        l3=input("skill: ")
        contri_skill[l3.split()[0]]=int(l3.split()[1])
    contri_list[name]=contri_skill
for i in range(project):
    l4=input("project and skill: ")
    name=l4.split()[0]
    days=int(l4.split()[1])
    score=int(l4.split()[2])
    best_before=int(l4.split()[3])
    no_of_roles=int(l4.split()[4])
    project_skill={}
    for j in range(no_of_roles):
        l5=input("role and skill: ")
        project_skill[l5.split()[0]]=int(l5.split()[1])
    project_list[name]=[days,score,best_before,no_of_roles,project_skill]
print(contri_list)
print(project_list)