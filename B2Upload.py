from b2blaze import B2
b2 = B2(key_id='0005844062529630000000001', application_key='K000YQB8wtAH0aXyOg+5F49YjjpVCT4')
bucketname = 'hashcards-test'
bucket = b2.buckets.get(bucketname)
files = bucket.files.all()

def upload(filename):
    baseurl = "https://f000.backblazeb2.com/file/%s/%s" % (bucketname, filename)
    file = open(filename, 'rb')
    new_file = bucket.files.upload(contents=file, file_name=filename)
    return baseurl