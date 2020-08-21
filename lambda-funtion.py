s3= boto3.client('s3')

def lambda_handler(event,context):


    head_tail = os.path.split(event['name'])
    newfilename = head_tail[1]
    newfilepath = head_tail[0]

    awsprep_auth_token = 'xxxxxxxxxxxxxxx'
    aws_planid = 99999999
    plannode_handle = 'abcdef'
    overrideKey = 'param1'

    if context.event_type == 'google.storage.object.finalize' and newfilepath == 'landingzone':

        print('Run Plan on new file: {}'.format(newfilename))

        aws_runjob_endpoint = '/v4/plans/' + aws_planid + '/run'
        aws_plan_pram = {
            "wrangledDataset": {"id": aws_jobid},
            "planNodeOverrides":   [{"handle": plannode_handle,"overrideKey": overrideKey, "value": newfilenam }]
        }
        print('Run aws plan with param override: {}'.format(aws_plan_pram))
        aws_headers = {
            "Content-Type":"application/json",
            "Authorization": "Bearer "+awsprep_auth_token
        }        

        resp = requests.post(
            url=aws_runjob_endpoint,
            headers=aws_headers,
            data=json.dumps(aws_plan_pram)
        )

        print('Status Code : {}'.format(resp.status_code))      
        print('Result : {}'.format(resp.json()))

    return 'End File event'.format(newfilename)
