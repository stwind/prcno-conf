#!/usr/bin/env python

import sys, os, string, argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-t','--tags')
    parser.add_argument('env', type=str, help='environment to provision')
    return parser.parse_args(sys.argv[1:])

def get_cmd(options):
    cmd = ['ansible-playbook','ansible/playbooks/site.yml',
            '-i','ansible/hosts/' +  options.env,
            '--module-path=ansible/library/']
    if options.tags:
        cmd += ['-t',options.tags]
    return string.join(cmd)

if __name__ == '__main__':

    cmd = get_cmd(parse_args())

    sys.exit(os.system(cmd))
