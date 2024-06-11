# models.py
from odoo import models, fields


class Purchase(models.Model):
    #    _name = 'custom.purchase'
    _inherit = "res.partner"


    lock_confirmed_po = fields.Boolean("Customer Invoice Double Validate")
