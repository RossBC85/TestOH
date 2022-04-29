from odoo import models, fields, api

class FleetServicesTest(models.Model):
    _name='fleet.services.test'

    service_name=fields.Char(string='Service name')
    service_id=fields.Many2one('services', string='Service')
    vehicle_id=fields.Many2one('vehicle.test', string='Vehicle')
