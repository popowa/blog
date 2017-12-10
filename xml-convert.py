import os,linecache,re
path = '/Users/ayakomuro/code/blog/convert-xml-original/'
path_content = '/Users/ayakomuro/code/blog/content/'

files_list = os.listdir(path)

def cleanup(line):
    if ':::' not in line:
        p = re.compile(r"<[^>]*?div>")
        line = p.sub("", line)
        p = re.compile(r"{[^>]*?}")
        return p.sub("", line)

for file_name in files_list:
    with open(path + file_name) as f:
        post = ""
        title = ["Title: ", "タイトル未設定"]
        date = ["Date: ", "2017-01-01 11:30"]
        category = ["Category: ", "tech"]
        status = "Status: published"
        content = ["", ""]
        for num, line in enumerate(f):
            line = cleanup(line)
            if num == 0:
                title = line.split(":")
            elif num == 1:
                date = line
            elif num == 3:
                category = line.split(":")
            elif num == 5:
                status = line
            elif num == 7 and "+" in line:
                content = line.split("+")
            if line and num >= 8:
                post += line

        row = "{}\n{}{}\n{}{}{}{}\n{}\n".format(
            title[0] + ": " + content[0], #Title
            date, #Date
            "Authors: ayakomuro" , #Author/lines[2]
            "Tags: " + category[1], #Category
            "Slug:" + title[1].lstrip(' /').replace(".html", ""), #Slug
            status, #Status
            "",
            content[1])
        f.close()
        f2 = open(path_content+file_name, 'w')
        f2.write(row+post)
        f2.close()
