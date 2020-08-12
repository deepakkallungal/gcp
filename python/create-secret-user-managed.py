import argparse

from google.oauth2 import service_account

KEY_PATH = "<SERVICE ACCOUNT KEY FILE PATH>"
SCOPES = ["https://www.googleapis.com/auth/cloud-platform"]
VERSION = "latest"
payload = []

#Create Secret 
def create_secret(project_id, secret_id):

    credentials = service_account.Credentials.from_service_account_file(KEY_PATH, scopes=SCOPES,)
    # Import the Secret Manager client library.
    from google.cloud import secretmanager

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()

    # Build the resource name of the parent project.
    parent = client.project_path(project_id)

    # Create the secret.
    response = client.create_secret(parent, secret_id, {
        'replication': {
            'user_managed': {'replicas': [{'location': 'europe-north1'}]},
        },
    })

    # Print the new secret name.
    print('Created secret: {}'.format(response.name))

    return response


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('project_id', help='id of the GCP project')
    parser.add_argument('secret_id', help='id of the secret to create')
    args = parser.parse_args()

    #CREATE SECRET
    create_secret(args.project_id, args.secret_id)
