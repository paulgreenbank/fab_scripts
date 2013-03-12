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

@hosts('localhost','cwa-fujitsu-P1610')
def install_pkg_local():
	install_pkg()

@hosts('ero.govt.nz,bankomb.org.nz,nzblood.co.nz')
def install_pkg_lhxen01():
	install_pkg()

@hosts('learningmedia.co.nz,charter-live')
def install_pkg_lhxen02():
	install_pkg()

@hosts('hubs-db,hubs-web1,hubs-web2,hubs-java,hubs-proxy1,hubs-proxy2,hubs-moodle')
def install_pkg_hubs():
	install_pkg()

@hosts('eztki-db,eztki-web1,eztki-web2,eztki-proxy1,eztki-proxy2')
def install_pkg_tki():
	install_pkg()

@hosts('digidb-prod,digiweb-prod,proxy-prod,fedora-mms-live,eztki-solr')
def install_pkg_scootle():
	install_pkg()

@hosts('ceismic-dev,nzblood-dev,bankomb-dev,ezpub-smb-dev,ezfind-smb-dev')
def install_pkg_dev():
	install_pkg()

@hosts('ceismic-staging,nzblood-staging,bankomb-staging,ezpub-smb-staging,ezfind-smb-staging')
def install_pkg_staging():
	install_pkg()

@hosts('hubs-db-preprod,hubs-web-preprod,hubs-proxy-preprod,hubs-java-preprod,hubs-moodle-preprod')
def install_pkg_preprod_hubs():
	install_pkg()

@hosts('eztki-db-preprod,eztki-web-preprod,eztki-proxy-preprod,eztki-solr-preprod')
def install_pkg_preprod_tki():
	install_pkg()

def install_pkg(pkg=None):
	if pkg is not None:
		env["pkg"] = pkg
	elif pkg is None and env.get("pkg") is None:
		env["pkg"] = prompt("Which package? ")
	if is_apt() is True:
		sudo('apt-get install -y %s' % env["pkg"])
	else:
		sudo('yum install -y %s' % env["pkg"]) 
