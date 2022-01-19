import os
import io
import hashlib


# make a folder at ./mods/ called nlmeta
if not os.path.exists("mods/nlmeta"):
    os.makedirs("mods/nlmeta")


mods = os.listdir("mods")
metafiles = os.listdir("mods/nlmeta/")
md5 = hashlib.md5()
BLOCK_SIZE = 65536


for mod in mods:
    if mod.endswith((".NLMeta")):
        os.remove("mods/"+mod)


for file in metafiles:
    if file.endswith((".NLMeta")):
        os.remove("mods/nlmeta/"+file)


for mod in mods:
    if mod.endswith((".jar")):
        modhash = hashlib.md5(open(f'mods/'+mod,'rb').read()).hexdigest()
        f = open(f"mods/nlmeta/{mod}.NLMeta", "a")
        f.write(f"{mod}\n{modhash}")
        f.close()
        print(f"{modhash} {mod}")

