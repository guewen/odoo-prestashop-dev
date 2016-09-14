# Odoo PrestaShop

## Pre-requisite

1. to install docker, refers to [this
   documentation](https://docs.docker.com/engine/installation/linux/ubuntulinux/),

2. to install docker-compose, run

        sudo pip install docker-compose

## Installation

```
$ git clone git@github.com:guewen/odoo-prestashop-dev.git
$ cd odoo-prestashop-dev
$ git submodule init
$ git submodule update
$ docker-compose up -d
```

## Accesses

### Odoo

The Odoo docker image is built from the source using:
https://github.com/camptocamp/docker-odoo-project/

* address: http://localhost
* user: admin
* password: admin

### PrestaShop

The PrestaShop docker image is: https://github.com/PrestaShop/docker

* address: http://localhost:8080
* admin address: http://localhost:8080/backoffice
* API address: http://[ip-address]/api where `[ip-address]` is the address you
  are redirected to when you go to http://localhost:8080 (does not work on
  localhost:8080 unfortunately)
* user: `demo@prestashop.com`
* password: `prestashop_demo`

Once logged in the backoffice, you still have to create a webservice key, heads
on: `Advanced Parameters > Webservice` and enable `Enable PrestaShop's
webservice`. Then, on the same page, create a new Webservice key (add all the
accesses).

When the PrestaShop container is restarted (often after a reboot), its IP
address changes. When it happens, the shop url needs to be updated to the new IP with:

```bash
$ ./fix_mysql_address.sh
```
