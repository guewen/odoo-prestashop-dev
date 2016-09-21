#!/bin/bash

address=$(docker inspect --format '{{ .NetworkSettings.Networks.odooprestashopdev_default.IPAddress }}' odooprestashopdev_prestashop_1)
docker run --rm -it --net=odooprestashopdev_default --link odooprestashopdev_mysql_1:mysql \
  --rm mysql:5.6 sh -c "exec mysql -h'mysql' -P'3306' -uroot -p'admin' prestashop --execute=\"UPDATE ps_shop_url SET domain = '${address}', domain_ssl = '${address}'\""
echo "Current prestashop address is: $address"
