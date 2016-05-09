#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from sys import exit
import argparse
import boto3
import datetime
from dateutil.tz import tzutc, tzlocal


states = ['ok', 'warning', 'critical', 'unknown']


def get_reservations(profile):
    session = boto3.Session(profile_name=profile)
    ec2 = session.client('ec2')
    filters = [{'Name': 'state', 'Values': ['active']}]
    rsv_instances = ec2.describe_reserved_instances(Filters=filters)
    return rsv_instances['ReservedInstances']


def get_options():
    hlpDsc = "Check the expiration time of AWS reserved instances"
    optParser = argparse.ArgumentParser(description=hlpDsc)
    optParser.add_argument("-c", "--critical", required=True,
                           help="critical threshold",
                           metavar="days", type=int,
                           dest="crit", default=15)
    optParser.add_argument("-p", "--profile", required=True,
                           help="AWS profile in credentials file",
                           metavar="profile", type=str,
                           dest="profile", default='')
    optParser.add_argument("-w", "--warning", required=True,
                           help="warning threshold",
                           metavar="days", type=int,
                           dest="warn", default=30)
    return optParser.parse_args()


def check_instances(instances, warning, critical):
    global_state = 0
    for ri in instances:
        state = 0
        remaining = ri['End'] - datetime.datetime.now(tzutc())
        if remaining.days <= warning:
            if remaining.days <= critical:
                state = 2
            else:
                state = 1
        print('%s: %s %s instances expires on %s' %
              (states[state][0].upper(),
               ri['InstanceCount'],
               ri['InstanceType'],
               ri['End'].astimezone(tzlocal()).strftime('[%x %X]')))
        if state > global_state:
            global_state = state
    return global_state


def main():
    state = 3
    args = get_options()
    if args.crit > args.warn:
        print('Critical threshold cannot be higher than warning.')
    else:
        try:
            rsv_inst = get_reservations(args.profile)
        except Exception:
            print('Error retrieving AWS info.\n',
                  '\rCheck the connection or the config file and try again.')
        else:
            state = check_instances(rsv_inst, args.warn, args.crit)
    exit(state)
    return

if __name__ == "__main__":
    main()
