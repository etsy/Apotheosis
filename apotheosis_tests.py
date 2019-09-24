from oauth2client.client import GoogleCredentials
import oauth2client
from googleapiclient import discovery
import unittest
import json
import imp
import time
import subprocess
import os
apotheosis = imp.load_source("apotheosis", os.getcwd() + "/apotheosis")
#these can be taken from the defaults or filled in:
test_resource = apotheosis.default_resource
test_member = apotheosis.default_member
test_role = apotheosis.default_role
test_service_account = apotheosis.default_service_account

class TestGetToken(unittest.TestCase):
    def test_get_token(self):
        token = apotheosis.get_token(test_service_account)
        try:
            token
            token = True
        except:
            token = False
        self.assertTrue(token)

class TestModifyPolicies(unittest.TestCase):
    def test_modify_policy(self):
        policy = { "bindings": [
        {
            "role": "roles/owner",
            "members": [
            "user:mike@example.com",
            "group:admins@example.com",
            "domain:google.com",
            "serviceAccount:my-other-app@appspot.gserviceaccount.com"
        ]
        },
        {
            "role": "roles/viewer",
            "members": ["user:sean@example.com"]
        }
        ]
        }
        policy_copy_of_original = json.loads(json.dumps(policy))
        role = "roles/viewer"
        member = "user:test@test.com"
        policy_with_addition = apotheosis.modify_policy_add_member(policy, role, member)
        for binding in policy_with_addition['bindings']:
            if binding['role']  == role:
                self.assertTrue(member in binding['members'])
        policy_with_removal = apotheosis.modify_policy_remove_member(policy, role, member)
        for binding in policy_with_removal['bindings']:
            if binding['role']  == role:
                self.assertTrue(member not in binding['members'])
        self.assertTrue(policy_with_removal == policy_copy_of_original)

class ApotheosisSuccessfulRun(unittest.TestCase):
    def test_sucessful_run(self):
        test_resource = apotheosis.default_resource
        result = apotheosis.add_role(test_role, test_member, test_resource, test_service_account)  
        self.assertTrue(result)


if __name__ == '__main__':
    unittest.main()

