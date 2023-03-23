import json
import unittest

import pytest
from Utilities.configReader import readConfig
import requests
import datetime

header = {
    'Authorization': 'Bearer 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',
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'
}
Today = datetime.datetime.now().strftime("%H-%M-%S")
username = "chanreddy800"
reponame = "testingWorld" + Today
sha_code = None
shacode1 = None


class gitHub():

    @pytest.mark.order(1)
    def git_login(self):
        end_point = "/user"
        url = readConfig("url", "web_url") + end_point
        response = requests.get(url, headers=header)
        statusCode = response.status_code
        jsonData = response.json()
        assert statusCode == 200
        print(jsonData['login'])

    @pytest.mark.order(2)
    def post_repo(self):
        end_point = "/user/repos"
        url = readConfig("url", "web_url") + end_point
        file = open("//home//chandrakiran//PycharmProjects//APiAutomation//Data//repo.json", "r")
        payload = file.read()
        json_input = json.loads(payload)
        json_input['name'] = reponame
        repoName = json_input['name']
        response = requests.post(url, headers=header, json=json_input)
        statuscode = response.status_code
        assert statuscode == 201
        print(repoName)

    @pytest.mark.order(3)
    def put_main_branch(self):
        url = readConfig("url", "web_url") + "/repos/chanreddy800/" + str(reponame) + "/contents/main"
        print(url)
        file = open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/mainbranch.json', 'r')
        json_file = json.loads(file.read())
        response = requests.put(url, headers=header, json=json_file)
        print(response.status_code)

        if response.status_code == 201:
            assert True
        else:
            assert False
        json_data = response.json()
        sha = json_data['commit']['sha']
        global sha_code
        sha_code = sha

    @pytest.mark.order(4)
    def createBranch_Post(self):
        print(str(sha_code))
        end_point = "/repos/chanreddy800/" + str(reponame) + "/git/refs"

        url = readConfig("url", "web_url") + end_point
        file = open("/home/chandrakiran/PycharmProjects/pythonProject10/Data/branch.json", "r")
        json_input = json.loads(file.read())
        json_input["sha"] = sha_code

        # with open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/branch.json', 'r') as file:
        #     json_file = json.loads(file.read())
        # json_file["sha"] = sha_code
        # with open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/branch.json', 'w') as file:
        #     file.write(json.dumps(json_file, indent=4))
        response = requests.post(url, headers=header, json=json_input)

        print(response.status_code)
        if response.status_code == 201:
            assert True
        else:
            assert False

    @pytest.mark.order(5)
    def createFileBranch(self):
        url = readConfig("url", "web_url") + "/repos/chanreddy800/" + reponame + "/contents/intel"
        file = open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/newfile.json', 'r')
        jsonFile = json.loads(file.read())

        response = requests.put(url, headers=header, json=jsonFile)
        print(response.status_code)
        if response.status_code == 201:
            assert True
        else:
            assert False
        json_data = (response.json())
        print(json_data)
        shaUpdate = json_data['content']['sha']
        print(shaUpdate)
        global shacode1
        shacode1 = shaUpdate
        print(shacode1)

    @pytest.mark.order(6)
    def pull_request(self):
        url = readConfig("url", "web_url") + "/repos/chanreddy800/" + reponame + "/pulls"
        file = open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/pullrequest.json', 'r')
        jsonfile = json.loads(file.read())

        response = requests.post(url, headers=header, json=jsonfile)

        print(response.status_code)
        if response.status_code == 201:
            assert True
        else:
            assert False

    @pytest.mark.order(7)
    def updateFileinBranch(self):
        url = readConfig("url", "web_url") + "/repos/chanreddy800/" + reponame + "/contents/intel"
        file = open('/home/chandrakiran/PycharmProjects/pythonProject10/Data/updateFile.json', 'r')
        json_input = json.loads(file.read())
        json_input['sha'] = shacode1

        response = requests.put(url, headers=header, json=json_input)
        print(response.status_code)
        if response.status_code == 200:
            assert True
        else:
            assert False
