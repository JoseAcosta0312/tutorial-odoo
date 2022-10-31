# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'estate',
    'depends': [
        'base_setup',
        'web',
    ],
    'data':[
      'security/security.xml',
      'security/ir.model.access.csv',
      'views/testmodel_action.xml',
      'views/estate_property_type_views.xml',
      'views/estate_property_tag_views.xml',
      'views/estate_property_offer_views.xml',
      'views/res_users_views.xml',
      'views/estate_menus.xml',
      'data/estate.property.type.csv',
      'report/estate_reports.xml',
      'report/estate_model_templates.xml',
      'report/estate_info_view.xml'
    ],
     "demo": [
         "data/estate_property.xml"
        #"demo/estate_tag.xml",
        #"demo/estate_model.xml",
        #"demo/estate_offer.xml",
    ],
    'category': 'Real Estate/Brokage',
    'installable': True,
    'application': True,
    'auto_install': False
}