#!/usr/bin/python3
import time
from fabric.api import local, run, hosts, env, put
import os

env.hosts = ['35.231.20.106', '35.229.86.150']
"""
,Deploy webstatic
"""


def do_deploy(archive_path):
    """
    Method to deploy files
    """
    if not archive_path:
        return False
    if not os.path.exists(archive_path):
        return False

    filename = archive_path.split("/")[-1]
    put(archive_path, "/tmp/{}".format(filename))

    run("sudo mkdir -p /data/web_static/releases/{}".format(filename))
    run("sudo tar -xzf /tmp/{} -C /data/web_static/releases/{}"
        .format(filename, filename))
    run("sudo rm /tmp/{}".format(filename))
    run("sudo mv /data/web_static/releases/{}/web_static/*"
        " /data/web_static/releases/{}"
        .format(filename, filename))
    run("sudo rm -rf /data/web_static/releases/{}/web_static"
        .format(filename))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s /data/web_static/releases/{}/ /data/web_static/current"
        .format(filename))
    print("New version successfully deployed!")
