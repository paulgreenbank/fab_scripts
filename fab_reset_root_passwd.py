# Script version 1.0

import os
import string
import random
import time

from fabric.operations import local as lrun
from fabric.api import *
from fabric.contrib import *
from string import lower
from crypt import crypt

@hosts('localhost','cwa-fujitsu-P1610')
def root_passwd_local():
	root_passwd()

@hosts('ero.govt.nz,bankomb.org.nz,nzblood.co.nz')
def root_passwd_lhxen01():
	root_passwd()

@hosts('learningmedia.co.nz,charter-live')
def root_passwd_lhxen02():
	root_passwd()

@hosts('hubs-db,hubs-web1,hubs-web2,hubs-java,hubs-proxy1,hubs-proxy2,hubs-moodle')
def root_passwd_hubs():
	root_passwd()

@hosts('eztki-db,eztki-web1,eztki-web2,eztki-proxy1,eztki-proxy2')
def root_passwd_tki():
	root_passwd()

@hosts('digidb-prod,digiweb-prod,proxy-prod,fedora-mms-live,eztki-solr')
def root_passwd_scootle():
	root_passwd()

@hosts('ceismic-dev,nzblood-dev,bankomb-dev,ezpub-smb-dev,ezfind-smb-dev')
def root_passwd_dev():
	root_passwd()

@hosts('ceismic-staging,nzblood-staging,bankomb-staging,ezpub-smb-staging,ezfind-smb-staging')
def root_passwd_staging():
	root_passwd()

@hosts('hubs-db-preprod,hubs-web-preprod,hubs-proxy-preprod,hubs-java-preprod,hubs-moodle-preprod')
def root_passwd_preprod_hubs():
	root_passwd()

@hosts('eztki-db-preprod,eztki-web-preprod,eztki-proxy-preprod,eztki-solr-preprod')
def root_passwd_preprod_tki():
	root_passwd()

def root_passwd():
    password = open('passwd_file', 'r').readline()
    crypted_password = crypt(password, 'salt')
    sudo('usermod --password %s root' % (crypted_password), pty=False)

