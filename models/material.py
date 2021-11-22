from odoo import models, fields

class Material(models.Model):
    _name = 'inventory.material'
    _description = 'Deskripsi Bahan Baku'
    _sql_constraints = [
        ('name_uniq', 'unique(name)', "Name already exists!")
    ]
    
    id = fields.Char(string="ID", required=True)
    name = fields.Char(string="Nama", required=True)
    description = fields.Char(string="Deskripsi", required=True)
    stock = fields.Integer(string="Jumlah stok (kg)", required=True)
    type = fields.Many2one('inventory.material.type', string="Jenis", required=True)
    source = fields.Char(string="Sumber", required=True)

class MaterialType(models.Model):
    _name = 'inventory.material.type'
    _description = 'Jenis Bahan Baku'

    name = fields.Char(string="Nama")