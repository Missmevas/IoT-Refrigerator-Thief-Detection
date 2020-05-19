import boto3
bucketname = 'dorota-raspberrypi' # replace with your bucket name
filename = '5.jpg' # replace with your object key
s3 = boto3.resource('s3')
s3.Bucket(bucketname).download_file(filename, 'downloaded_from_aws.jpg')