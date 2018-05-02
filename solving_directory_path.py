import os

path = os.path.normpath(os.getcwd())
path = path.split(os.sep)

print(path)

path = [p for p in path if p]

print(path)
root = ['~']
current_dir = [path[-1]]
print(current_dir, root)

path = path[:-1]
if 'home' in path[0]:
    path = path[2:]
print(path)
# potential_path = os.sep.join(path[
    # path = os.sep.join(['~'] + path[3:])

max_x = 13

index = 0
potential_path = os.sep.join(root + path + current_dir)
while len(potential_path) > max_x:
    if index < len(path):
        path[index] = '+'
        potential_path = os.sep.join(root + path + current_dir)
        index += 1
    if index == len(path):
        potential_path = ''
    


print(len(potential_path))
print(potential_path)
