from b2blaze import B2
b2 = B2(key_id='0005844062529630000000001', application_key='K000YQB8wtAH0aXyOg+5F49YjjpVCT4')
bucket = b2.buckets.get('hashcards-test')
files = bucket.files.all()

# b2_api.authorize_account("production", application_key_id, application_key)

# bucket = b2_api.get_bucket_by_name('hashcards-test')
# bucket.upload_local_file(
#         local_file='Assests/test1.png',
#         file_name='test1.png'
#     )
# b2 = B2()
# bucket = b2.buckets.get('test_bucket')
#bucket = b2.buckets.create('test_bucket', security=b2.buckets.public)

# bucket_by_name = b2.buckets.get('test_bucket')
# bucket_by_id = b2.buckets.get(bucket_id='abcd')
text_file = open('Assests/test1.png', 'rb')
new_file = bucket.files.upload(contents=text_file, file_name='test.png')
print(new_file)
file_by_id = bucket.files.get(file_name='test.png')
print(file_by_id)
# file = bucket.files.get(file_name='folder/hello.txt')
# downloaded_file = file.download()
