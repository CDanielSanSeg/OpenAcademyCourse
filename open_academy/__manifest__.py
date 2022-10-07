{
    'name': "open_academy",
    'license': "LGPL-3",
    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",
    'author': "Vauxoo",
    'website': "http://www.yourcompany.com",
    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        # Check the order, 1. security, 2 views, 3 menus
        'security/ir.model.access.csv',
        'security/open_academy_security.xml',
        'views/open_academy_course_views.xml',
        'views/open_academy_session_views.xml',
        'views/open_academy_course_menu_views.xml',
        'views/res_partner_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/open_academy_course_demo.xml',
    ],
}
