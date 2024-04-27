from odoo import fields, models

class PropertyModel(models.Model):
    _name = "esate_model",
    _description = "Real Estate Model"
    
    # columns in the PropertyModel table
    name = fields.Char("Name",required=True)
    description = fields.Text("Description", required=True)
    postcode  = fields.Char("Post Code")
    date_availability  = fields.Datetime("Date Availability", required=True)
    expected_price  = fields.Float("Expected Price", required=True)
    selling_price = fields.Float("Selling Price", required= True)
    bedrooms  = fields.Integer("Bed Rooms", required=True)
    living_area  = fields.Integer("Living Area", required=True)
    facades = fields.Integer("Facades", required=True)
    garage = fields.Boolean("Garage")
    garden  = fields.Boolean("Garden")
    garden_area = fields.Integer("Garden Area")
    garden_orientation  = fields.Selection("Garden Orientation",[
        ('north', 'NORTH'),
        ('south', 'SOUTH'),
        ('east', 'EAST'),
        ('west', 'WEST'),
    ])

