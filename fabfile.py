import os
import time
from fabric.api import local, cd, run, env, lcd
from fabric.context_managers import hide

import nose
import requests


def clean():
    print "Removing *.pyc files"
    local("find . -name \"*.pyc\" -exec rm -v '{}' ';'")
    print "Removing *.un~ files"
    local("find . -name \"*.un~\" -exec rm -v '{}' ';'")


# GIT FUNCTIONS

def push(branch):
    switch(branch)
    git_command('push origin', branch=branch)


def sync(branch):
    switch(branch)
    update(branch)
    push(branch)


def pull(branch):
    update(branch)


def update(branch):
    switch(branch)
    git_command('pull origin', branch=branch)


def remote_branch(branch_name):
    git_command('fetch', branch=branch_name)
    git_command('checkout -b {}'.format(branch_name),
                branch='origin/{}'.format(branch_name))


def branch(branch_name):
    git_command('checkout -b', branch=branch_name)


def switch(branch):
    git_command('checkout', branch=branch)


def status():
    git_command('status')


def git_command(command, branch=''):
    dirs = ['arbytrage']
    for d in dirs:
        print "=" * 80
        print d
        print "=" * 80
        with lcd(d):
            local('git {} {}'.format(command, branch))