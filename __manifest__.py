{
'name': 'Home Tools Shop',
'version': '1.0',
'category': 'Custom',
'summary': 'Management system for a home tools store',
'author':"farida",
'depends': ['base'],
'data': [
    'security/ir.model.access.csv',
    'views/actions.xml',
    'views/menu.xml',
    'views/product_category_views.xml',
    'views/product_item_views.xml',
    'views/product_customer_views.xml',


],
'application': True,
'installable': True,
}