from fabric.api import *
from fabric.contrib.console import confirm

env.hosts = ['root@47.52.235.110']

def push():
    local("git add . && git commit")
    local("git push")

def deploy():
    code_dir = '/www/maimoe'
    with settings(warn_only=True):
        if run("test -d %s" % code_dir).failed:
            run("git clone git@github.com:bydmm/maimoe.git %s" % code_dir)
    with cd(code_dir):
        run("git pull")
        run("service nginx restart")
