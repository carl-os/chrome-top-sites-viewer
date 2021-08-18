import os, shutil, sqlite3, csv
from tabulate import tabulate




root_directory = os.path.join(os.path.join(os.path.join(os.path.join(os.path.join(os.environ["USERPROFILE"], "AppData"), "Local"), "Google"), "Chrome"), "User Data")
def check_directory():
    global directory
    if os.path.exists(os.path.join(os.path.join(root_directory, "Default"), "Top Sites")):
        directory = os.path.join(root_directory, "Default")
    else:
        directory = os.path.join(root_directory, "Profile 1")



def view_history():
    check_directory()
    shutil.copy(directory + "\Top Sites", os.path.join((os.path.join(os.environ["USERPROFILE"], "Desktop")), "Top Sites"))
    con = sqlite3.connect(os.path.join((os.path.join(os.environ["USERPROFILE"], "Desktop")), "Top Sites"))
    cur = con.cursor()
    sites = []
    headers = ["URL Ranking", "URL", "Title"]
    for i in cur.execute("select url_rank+1, url, title from top_sites order by url_rank limit 0,10"):
        sites.append(i)
    con.close()
    table = tabulate(sites, headers)
    with open(os.path.join((os.path.join(os.environ["USERPROFILE"], "Desktop")), "top-sites.txt"), "w") as file:
        file.write(table)
        file.close()
    print(table)



if os.path.exists(root_directory):
    view_history()
else:
    print("can't find top sites file (Chrome is not installed in default directory)")



input()