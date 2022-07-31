import os


dirs=[
    os.path.join("data","raw"),
    os.path.join("data","processed"),
    
    "noteboks",
    "saved_models",
    "src"

]


for i in dirs:
    os.makedirs(i,exist_ok=True)
    with open(os.path.join(i,".gitkeep"),"w") as f:
        pass



files=[

    "dvc.yaml",
    "param.yaml",
    "gitignore",
 
    os.path.join("src","__init__.py")

]

for x in files:
    with open(x,"w") as ff:
        pass





