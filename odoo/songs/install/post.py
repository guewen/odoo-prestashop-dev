# -*- coding: utf-8 -*-
# Copyright 2016 Camptocamp SA
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html)

import anthem


@anthem.log
def setup_company(ctx):
    """ Setup company """
    company = ctx.env.ref('base.main_company')
    company.name = 'Old Curiosity Shop'


@anthem.log
def setup_language(ctx):
    """ Installing language and configuring locale formatting """
    for code in ('fr_FR', 'de_DE'):
        ctx.env['base.language.install'].create({'lang': code}).lang_install()
    ctx.env['res.lang'].search([]).write({
        'grouping': [3, 0],
        'date_format': '%d/%m/%Y',
    })


@anthem.log
def main(ctx):
    """ Main: creating demo data """
    setup_company(ctx)
    setup_language(ctx)
