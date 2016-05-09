This script retrieves the reserved instances expire time from AWS and checks its status using the thresholds passed as parameters.
The script is prepared to work with Nagios, and the return codes match with the expected Nagios values.

The AWS credentials are taken using the [Named profiles in the AWS config file](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html#cli-multiple-profiles).

Example:

```bash
# check_aws_reserved -c 10 -w 45 -p aws_profile
O: 5 c3.2xlarge instances expires on [11/30/16 17:48:23]
O: 2 t2.medium instances expires on [11/30/16 17:48:20]
W: 8 t2.micro instances expires on [06/22/16 10:26:39]
O: 1 m3.large instances expires on [11/30/16 17:48:21]
W: 4 t2.medium instances expires on [06/22/16 10:26:39]
W: 3 c3.xlarge instances expires on [06/22/16 10:26:46]
C: 11 c3.2xlarge instances expires on [05/18/16 13:17:59]
```

The status of each instance type is shown in the first character:
- 'O': OK
- 'W': Warning
- 'C': Critical

The date format is shown using locale configuration.
