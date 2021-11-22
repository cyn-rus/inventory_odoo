# -*- coding: utf-8 -*-
{
    'name': "Inventarisasi",
    'summary': 'Module Odoo untuk sistem inventaris.',
    'description': 'Module Odoo untuk menyimpan dan menampilkan data bahan baku dan produk dari suatu perusahaan.',
    'sequence': -100,
    'author': "Sejahtera",
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/inventory_menus.xml',
        'views/inventory_trees.xml',
        'views/inventory_forms.xml',
    ],
    'qweb': [
 
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
