# Script version 1.0

import os
import string
import random
import time

from fabric.operations import local as lrun
from fabric.api import *
from fabric.contrib import *
from string import lower

def is_apt():
  """
  Helper function that returns whether we are running on apt based system,
  we assume that we are running on a debian based distro.
  """
  return files.exists('/usr/bin/apt-get')

@hosts('localhost')
def upgrade_local():
	upgrade()

@hosts('ero.govt.nz,bankomb.org.nz,nzblood.co.nz')
def upgrade_lhxen01():
	upgrade()

@hosts('learningmedia.co.nz,charter-live')
def upgrade_lhxen02():
	upgrade()

@hosts('hubs-db,hubs-web1,hubs-web2,hubs-java,hubs-proxy1,hubs-proxy2,hubs-moodle')
def upgrade_hubs():
	upgrade()

@hosts('eztki-db,eztki-web1,eztki-web2,eztki-proxy1,eztki-proxy2')
def upgrade_tki():
	upgrade()

@hosts('digidb-prod,digiweb-prod,proxy-prod,fedora-mms-live,eztki-solr')
def upgrade_scootle():
	upgrade()

def upgrade():
        if is_apt() is True:
                sudo('apt-get update')
		sudo('apt-get dselect-upgrade')
        else:
                sudo('yum -y upgrade')

