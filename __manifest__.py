{
    'name': 'ONT INV',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Customization for Product Template',
    'author': 'Janani',
    'depends': ['base', 'product','purchase'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/product_details_views.xml',
        'report/purchase_order_report_template.xml'

    ],
    'installable': True,
    'application': True,
}
