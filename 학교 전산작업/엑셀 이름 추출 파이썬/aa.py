f = open("sangsang.txt", 'rt', encoding = "UTF8")
sangf = f.read()
sangf_tmp = str(sangf.replace("\n", ","))

sangsang = sangf_tmp.split(",")

f = open("project.txt", 'rt', encoding = "UTF8")
projectf = f.read()
projectf_tmp = str(projectf.replace("\n", ","))

project = projectf_tmp.split(",")

sangsanglist = []
projectlist = []
anslist = []

[sangsanglist.append(x) for x in sangsang if x not in sangsanglist]

[projectlist.append(x) for x in project if x not in projectlist]

for name in sangsanglist:
    if name not in projectlist:
        anslist.append(name)
        print(name, end = " ")

# print(anslist)
