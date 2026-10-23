{
    'name': 'Presales Demo',
    'version': '1.0.0',
    'summary': 'Demo addon that depends on the Purchase module',
    'author': 'Your Company',
    'website': 'https://www.example.com',
    'category': 'Sales',
    'depends': ['purchase'],
    'data': [
        'views/purchase_order_view.xml',
    ],
    'installable': True,
    'application': False,
}
