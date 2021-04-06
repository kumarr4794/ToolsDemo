import boto3
import argparse


client = boto3.client('route53')

TYPE = ['CNAME',
        'A']

ACTION = ['CREATE',
          'DELETE',
          'UPSERT']

def update_cname_record(Name, action, type, ttl, dns):
    try:
        response = client.change_resource_record_sets(
        HostedZoneId='Z1R8UBAEXAMPLE',
        ChangeBatch= {
                        'Comment': 'add %s -> %s' % (Name, value),
                        'Changes': [
                            {
                             'Action': action,
                             'ResourceRecordSet': {
                                 'Name': Name,
                                 'Type': type,
                                 'AliasTarget': {
                                 'HostedZoneId': "Z2FDTNDATAQYW2",
                                 'DNSName': dns,
                                 'EvaluateTargetHealth': 'false'
                                    },
                            }
                        }]
        })
    except Exception as e:
        print(e)

def main():
    parser = argparse.ArgumentParser(description='Update DNS records on R53')

    parser.add_argument('-N', '--Name', required=True, type=str)
    parser.add_argument('-T', '--Type', choices=TYPE, required=True, type=str)
    parser.add_argument('-a', '--action', choices=ACTION, required=True)
    parser.add_argument('-t', '--ttl', default=300, type=int)
    parser.add_argument('-d', '--dns', required=True)

    args = parser.parse_args()

    update_cname_record(args.Name, args.value, args.action, args.Type, args.ttl)

if __name__ == "__main__":
    main()