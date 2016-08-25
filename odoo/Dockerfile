FROM camptocamp/odoo-project:9.0-1.3.0
MAINTAINER Camptocamp

# Install additional debian packages if needed
# RUN set -x; \
#         apt-get update \
#         && apt-get install -y --no-install-recommends \
#         python-shapely \
#         && apt-get clean \
#         && rm -rf /var/lib/apt/lists/*

# Install additional python packages if needed
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

ENV ADDONS_PATH="/opt/odoo/src/addons, \
  /opt/odoo/external-src/bank-payment, \
  /opt/odoo/external-src/connector, \
  /opt/odoo/external-src/connector-ecommerce, \
  /opt/odoo/external-src/product-attribute, \
  /opt/odoo/external-src/sale-workflow" \
  LIMIT_TIME_CPU=86400 \
  LIMIT_TIME_REAL=86400 \
  LIMIT_MEMORY_SOFT=1342177280 \
  LIMIT_MEMORY_HARD=1610612736
