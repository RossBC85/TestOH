from odoo import fields, models, api

class VehicleTest(models.Model):
    _name='vehicle.test'


    license=fields.Char(string='license')
    driver_id=fields.Many2one('res.partner', string='Driver')


