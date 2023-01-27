from odoo import api, fields, models

class Department(models.Model):
    _name = "department"

    name = fields.Char(string="Department Name", required=True)

class Employee(models.Model):
    _name = "employee"

    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    age = fields.Integer(string="Age", required=True)
    mail = fields.Char(string="Email", required=True)
    address = fields.Char(string="Address", required=True)

    department = fields.Many2one("department", string="Department", required=True)


class Tasks(models.Model):
    _name = "tasks"

    name = fields.Char(string="Name", required=True)
    task = fields.Text(string="Task", required=True)
    employee_id = fields.Many2one("employee", string="Employee", required=True)
    employee_name = fields.Char(related="employee_id.name", string="Name")
    employee_surname = fields.Char(related="employee_id.surname", string="Surname")
