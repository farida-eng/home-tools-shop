from odoo import models, fields

class ProductCustomer(models.Model):
    _name = 'product.customer'
    _description = 'Customer'

    name = fields.Char(string='Name')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')



