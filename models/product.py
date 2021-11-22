from odoo import models, fields

class Product(models.Model):
    _name = 'inventory.product'
    _description = 'Deskripsi Produk'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Name already exists!")
    ]
    
    id = fields.Char(string="ID", required=True)
    name = fields.Char(string="Nama", required=True)
    description = fields.Char(string="Deskripsi", required=True)
    stock = fields.Integer(string="Jumlah stok (buah)", required=True)
    type = fields.Selection(selection=[
        ('0', 'Pupuk'), ('1', 'Pangan')
    ], string="Jenis", required=True)
    price = fields.Integer(string="Harga", required=True)
