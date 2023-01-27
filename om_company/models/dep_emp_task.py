from odoo import api, fields, models
import re

class Department(models.Model):
    _name = "department"

    name = fields.Char(string="Department Name", required=True)

class Employee(models.Model):
    _name = "employee"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    age = fields.Integer(string="Age", required=True, widget='age')
    email = fields.Char(string="Email", required=True, widget='email', size=256)
    address = fields.Char(string="Address", required=True)

    department = fields.Many2one("department", string="Department", required=True)
    @api.constrains('age', 'email')
    def _validate_email_and_age(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(regex, self.email):
            raise ValueError("Email is not valid !")
        if self.age < 18:
            raise ValueError("You must be 18 or older !")


class Tasks(models.Model):
    _name = "tasks"

    name = fields.Char(string="Name", required=True)
    task = fields.Text(string="Task", required=True)
    employee_id = fields.Many2one("employee", string="Employee", required=True)
    employee_name = fields.Char(related="employee_id.name", string="Name")
    employee_surname = fields.Char(related="employee_id.surname", string="Surname")
