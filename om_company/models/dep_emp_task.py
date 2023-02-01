from odoo import api, fields, models
import re


class Department(models.Model):
    _name = "department"

    name = fields.Char(string="Department Name", required=True)


class Employee(models.Model):
    _name = "employee"

    full_name = fields.Char(string="Full Name", compute="_compute_full_name")
    name = fields.Char(string="Name", required=True)
    surname = fields.Char(string="Surname", required=True)
    age = fields.Integer(string="Age", required=True, widget='age')
    email = fields.Char(string="Email", required=True, widget='email', size=256)
    address = fields.Char(string="Address", required=True)
    gross_salary = fields.Float(string="Gross Salary", required=True)
    net_salary = fields.Float(string="Net Salary", compute="_compute_net_salary")
    # tasks_model_id = fields.Many2one("tasks")
    # task_name = fields.Char(related="tasks_model_id.name", string="Task name",
    #                         compute="_compute_tasks")
    department = fields.Many2one("department", string="Department", required=True)

    def _compute_tasks(self):
        pass

    def _compute_full_name(self):
        for record in self:
            record.full_name = record.name + " " + record.surname

    def _compute_net_salary(self):
        for record in self:
            record.net_salary = record.gross_salary - (record.gross_salary * 20 / 100)

    @api.constrains('age')
    def _validate_age(self):
        if self.age < 18:
            raise ValueError("You must be 18 or older !")

    @api.constrains('email')
    def _validate_email(self):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,7}\b'
        if not re.match(regex, self.email):
            raise ValueError("Email is not valid !")


class Tasks(models.Model):
    _name = "tasks"

    name = fields.Char(string="Name", required=True)
    task = fields.Text(string="Task", required=True)
    employee_id = fields.Many2one("employee", string="Employee", required=True,
                                  ondelete="cascade")
    employee_name = fields.Char(related="employee_id.name", string="Name")
    employee_surname = fields.Char(related="employee_id.surname", string="Surname")

