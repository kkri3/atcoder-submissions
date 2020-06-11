import os

contest = "ABC"
abc_old = 125
abc_latest = 168
add = 169

# for i in range(abc_old):
#     new_dir_path = f"./{contest}{i+1:03}"
#     os.mkdir(new_dir_path)
#     for new_filename in ["a.py","b.py","c.py","d.py"]:
#         with open(os.path.join(new_dir_path, new_filename), mode="w") as f:
#             f.write("")

# for i in range(abc_old,abc_latest):
#     new_dir_path = f"./{contest}{i+1:03}"
#     os.mkdir(new_dir_path)
#     for new_filename in ["a.py","b.py","c.py","d.py","e.py","f.py"]:
#         with open(os.path.join(new_dir_path, new_filename), mode="w") as f:
#             f.write("")

new_dir_path = f"./{contest}{add:03}"
os.mkdir(new_dir_path)
for new_filename in ["a.py","b.py","c.py","d.py","e.py","f.py"]:
    with open(os.path.join(new_dir_path, new_filename), mode="w") as f:
        f.write("")