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
* user: `demo@prestashop.com`
* password: `prestashop_demo`
