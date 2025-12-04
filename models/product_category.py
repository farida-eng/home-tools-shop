from odoo import models ,fields
class ProductCategory(models.Model):
    _name="product.category"
    _description="product category"



    name= fields.Char(string='Category Name',required=True)
    description = fields.Text(string="Description")