from odoo import models, fields

class AssetDepartment(models.Model):
    _name = 'asset.department'
    _description = 'Department'

    name = fields.Char(string="Department Name", required=True)
    code = fields.Char(string="Department Code")
    active = fields.Boolean(string="Active", default=True)