import unittest
import pytest
from pageObjects.test_taskGithub import gitHub


class gitHubAPI(unittest.TestCase):

    def test_login(self):
        lp = gitHub()
        lp.git_login()
        lp.post_repo()
        lp.put_main_branch()
        lp.createBranch_Post()
        lp.createFileBranch()
        lp.pull_request()
        lp.updateFileinBranch()

