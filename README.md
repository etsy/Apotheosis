# Apotheosis

Apotheosis is a tool you can run in the command line to grant yourself temporary Google Cloud Platform (GCP) Identity and Access Management (IAM) privileges which will expire after a specified amount of time. It is meant to allow high privilege users, who would otherwise have `Owner` or `Org Admin` roles, not to have any roles themselves except for `Service Account User` and `Service Account Token Creator` on a service account which will have the `Owner` role which would otherwise be assigned to these users.

To run the application:
```sh
git clone git@github.com:etsy/Apotheosis.git
cd apotheosis
virtualenv -p python2 venv
source venv/bin/activate
sudo python setup.py install
apotheosis -h
```

Usage Examples:

Adding to an organization:

```sh
apotheosis -d 30 -res 305014881247 -r roles/appengine.deployer
Added roles/appengine.deployer to user:amellos@etsy.com for 30 seconds
Removed roles/appengine.deployer from user:amellos@etsy.com
```

Adding to a project:

```sh
apotheosis -d 60 -res apotheosis-test -r roles/viewer -m group:example@etsy.com
Added roles/viewer to group:example@etsy.com for 60 seconds
Removed roles/viewer from group:example@etsy.com
```

It makes sense to configure defaults for the command line arguments. These can be hardcoded in the file apotheosis.py, like:
```
default_resource = "a-project-id"
default_role = "roles/viewer"
default_member = "user:someone@something.com"
default_service_account = "my_service_account@a-project-id.iam.gserviceaccount.com"
```
If you are signed in to gcloud your default credentials should be set. In some cases it may be necessary to run `gcloud auth application-default login` and authenticate with the account which has permissions on the service account.

Also you can press enter in the terminal to revoke the permissions early.
