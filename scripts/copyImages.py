from glob import glob
import os
import shutil

def func(unixPath="./lines/**/*", targetDir="./docs/gd/gdL/"):
    for file in glob(unixPath):
        if file.endswith(".md"):
            continue
        tgt = targetDir+os.path.dirname(file).split("/")[-1]
        os.makedirs(tgt, exist_ok=True)
        shutil.copyfile(file, f"{tgt}/{os.path.basename(file)}")



func("./git-guidelines/zones/**/*", targetDir="./docs/gd/gdZ/")
func("./git-guidelines/lines/**/*", targetDir="./docs/gd/gdL/")
