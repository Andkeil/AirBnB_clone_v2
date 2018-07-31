#!/usr/bin/python3
import time
from fabric.api import local, run, hosts, env
"""
Archive webstatic directory
"""


def do_deploy(archive_path):
    """
    Method to compress files
    """
    archive_time = time.strftime("%Y%m%d%H%M%S")
    new_archive_file = "web_static_" + archive_time + ".tgz"
    try:
        local("mkdir - [ versions")
        local("tar -cvzf versions/{} web_static".format(new_archive_file))
        return ("versions/{}".format(new_archive_file))
    except:
        return None
