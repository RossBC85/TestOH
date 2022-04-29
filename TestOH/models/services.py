from odoo import models, fields, api

class FleetServicesTest(models.Model):
    _name='services'

    name=fields.Char(string='Service name')
