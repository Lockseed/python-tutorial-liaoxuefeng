import os

print(os.name)
# print(os.environ)
print(f"TAVILY_API_KEY={os.environ.get('TAVILY_API_KEY')}")
print(os.uname())

project_path = os.path.abspath('.')
print(f"Current project path: {project_path}")
print(f"Samples code dir path: {os.path.join(project_path, 'samples')}")

file_pth = os.path.join(project_path, 'samples', 'io', 'some_file.txt')
file_name = os.path.basename(file_pth)
file_ext = os.path.splitext(file_name)[1]
print(f"File name: {file_name}. File ext: {file_ext}")

io_samples_dir = os.path.join(project_path, 'samples', 'io')
io_samples_file_list = [x for x in os.listdir(io_samples_dir) if os.path.isfile(os.path.join(io_samples_dir, x))]
print(f"IO samples file list: {io_samples_file_list}")