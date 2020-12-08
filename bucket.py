from google.cloud import storage
from google.oauth2 import service_account   

storage_client = storage.Client.from_service_account_json('Secret.json')
buckets = storage_client.list_buckets()
# for l in buckets:
#     print(l)
all_bucket_list = list(map(str,buckets))
print(all_bucket_list)


all_blobs = list(storage_client.list_blobs("my-test-project-292816-bucket-1"))
print(all_blobs[0])
# all_blob = list(storage_client.list_blobs(bucket))