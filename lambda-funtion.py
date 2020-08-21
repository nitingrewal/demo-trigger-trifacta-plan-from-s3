    #pip install requests
    import json
    import urllib.parse
    import boto3
    import urllib3
    import urllib.request
    import ssl
    
    print('Loading function')
    
    s3 = boto3.client('s3')
    
    def lambda_handler(event, context):
    
        # Get the object from the event and show its content type
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')
        try:
            response = s3.get_object(Bucket=bucket, Key=key)
            trifacta_auth_token = {{token}}
            run_plan_endpoint = '{{url}}/v4/plans/71/run'
            data = urllib.parse.urlencode({'planNodeOverrides' : [{'handle': '93','overrideKey': 'City_param','value': 'Phoenix'}]}).encode('ascii')
            
            print('data: {}'.format(data))
            trifacta_headers = {
                "Content-Type":"application/json",
                "Authorization": "Bearer "+trifacta_auth_token
            }   
            context = ssl._create_unverified_context()
            req = urllib.request.Request(run_plan_endpoint, json.dumps({'planNodeOverrides' : [{'handle': '93','overrideKey': 'City_param','value': 'Phoenix'}]}).encode("utf-8"), trifacta_headers)
            with urllib.request.urlopen(req, context=context) as response:
                 the_page = response.read()
    
        except Exception as e:
            print(e)
            print('Error getting object {} from bucket {}. Make sure they exist and your bucket is in the same region as this function.'.format(key, bucket))
            raise e
