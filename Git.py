import requests
import json

def getInfo(gitUser):
    #URL = ("https://api.github.com/users/"+gitUser+"/repos")
    #a = requests.get(URL)
    #b = json.loads(a.text)
    b = requests.get(f"https://api.github.com/users/{gitUser}/repos").json()

    c = []
    
    for x in b:
        try:
            c.append(x.get("name"))
        except:
            c = []
         
    return c

def getData(gitUser, repoName):          
    URL = "https://api.github.com/repos/"+gitUser+"/"+repoName+"/commits"
    #info = requests.get(URL)
    #commits = json.loads(info.text)
    commits = requests.get(URL).json()
    number = len(commits)

    return number
        

if __name__ == "__main__":
    gitUser = input("Enter Github username: ")     
    c = getInfo(gitUser) 
    print("User: " + gitUser)
    for x in c:              
        number = getData(gitUser, x)
        print("Repo: " + x + " Number of Commits: " + str(number))

