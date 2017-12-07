import os,linecache,re
path = '/Users/ayakomuro/code/blog/convert-xml/'


files_list = os.listdir(path)

for file_name in files_list:
    f = open(path + file_name)
    lines = f.readlines()

    title = lines[0].split(":")
    content = lines[7].split("+")

    row = "{}{}{}{}{}{}{}\n{}\n".format(
        title[0] + ": " + content[0], #Title
        lines[1], #Date
        lines[2], #Author
        lines[3], #Category
        "Slug:" + title[1].lstrip(' /').replace(".html", ""), #Slug
        lines[5], #Status
        "",
        content[1])
    print(row)
    f.close()
