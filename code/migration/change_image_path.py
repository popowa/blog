import os,re
import shutil

path_content = '/Users/ayakomuro/Code/blog/draft/2011/'
path_content_original  = '/Users/ayakomuro/Code/blog/content/blog/'


files_list = os.listdir(path_content)
print(len(files_list))
ok_files = []
for file_name in files_list:
    flag = True
    if file_name != '.DS_Store':
        with open(path_content + file_name) as f:
            for num, line in enumerate(f):
                if 'cloudstockimg.s3.amazonaws.com/' in line:
                    flag = False
    if flag:
        ok_files.append(file_name)
#        shutil.copyfile(path_content + file_name, path_content_original + file_name)
        print(file_name)

print(len(ok_files))
"""
                if 'code.popowa.com' in line:
                    p = re.compile('[¥w][:¥/_-]')
                    t = p.match(line)
                    print(t)
"""
