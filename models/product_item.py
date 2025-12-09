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
    description=fields.Text(string="Description")

    category = fields.Selection([
        ('kitchen', 'Kitchen'),
        ('electric', 'Electric'),
        ('decor', 'Decor'),
        ('furniture', 'Furniture'),
    ], string="Category", required=True)

    barcode = fields.Char(string="Barcode")

    cost_price = fields.Float(string="Cost Price")
    sale_price = fields.Float(string="Sale Price")

    image = fields.Image(string="Image")

    vendor_id = fields.Many2one('res.partner', string="Vendor")

