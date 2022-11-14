from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient, PublicAccess
import os 

# getting environment variable : connection string to the previously created azure storage account 
connect_str = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
container_name = "blob-container-01" 


def upload_file(source, dest): 
    ''' upload an individual file'''
    with open(source, 'rb') as data:
      client.upload_blob(name=dest, data=data)

def upload_dir(source, dest):
    ''' upload the whole file structure and files'''
    prefix = '' if dest == '' else dest + '/'
    prefix += os.path.basename(source) + '/'
    for root, dirs, files in os.walk(source):
        for name in files:
            dir_part = os.path.relpath(root, source)
            dir_part = '' if dir_part == '.' else dir_part + '/'
            file_path = os.path.join(root, name)
            blob_path = prefix + dir_part + name
            upload_file(file_path, blob_path)

# execute the logic            
try:
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    client = blob_service_client.get_container_client(container_name)
    upload_dir("data", '')
except Exception as ex:
    print('An exception has occured!')

