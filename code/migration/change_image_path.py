import os,re

path_content = '/Users/ayakomuro/Code/blog/content/blog/'

files_list = os.listdir(path_content)
for file_name in files_list:
    if file_name != '.DS_Store':
        with open(path_content + file_name) as f:
            for num, line in enumerate(f):
                if 'code.popowa.com' in line:
                    p = re.compile('[¥w][:¥/_-]')
                    t = p.match(line)
                    print(t)
