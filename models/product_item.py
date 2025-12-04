from email.policy import default

from pkg_resources import require

from odoo import models,fields
class ProductItem(models.Model):
    _name="product.item"
    _description=" home tools product"


    name=fields.Char(string="product name",requirerd=True)
    price=fields.Float(string="price" ,required=True)
    quantity=fields.Integer(string="Available Quantity" ,default=0)
    category_id = fields.Many2one("product.category", string="Category")
