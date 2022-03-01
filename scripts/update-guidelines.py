import yaml
import glob
import os.path

with open("mkdocs.yml") as f:
    yml = yaml.load(f)


def replace(dic, keys, new_val):
    for val in dic:
        if keys and keys[0] in val:
            k = keys.pop(0)
            if keys:
                replace(val[k], keys, new_val)
            else:
                val[k] = new_val


replace(yml["nav"], ["Guidelines", "Zones"], [
    {
        os.path.basename(filename.replace(".md", "")): filename.replace("./docs/", "")
    }
    for filename in sorted(glob.glob("./docs/gd/gdZ/**/*.md"))
])

replace(yml["nav"], ["Guidelines", "Lines"], [
    {
        os.path.basename(filename.replace(".md", "")): filename.replace("./docs/", "")
    }
    for filename in sorted(glob.glob("./docs/gd/gdL/**/*.md"))
])


with open("mkdocs.yml", "w") as f:
	f.write(yaml.dump(yml))
