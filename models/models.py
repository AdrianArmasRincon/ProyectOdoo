# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proyectoadrianarmas_empresas_contratadoras(models.Model):
     _name = 'proyectoadrianarmas.empresas_contratadoras'
     _description = 'proyectoadrianarmas.empresas_contratadoras'

     name = fields.Char(string="Empresa contratada")
     email = fields.Char(string="Correo electronico")
     phone = fields.Integer(string="Número de Teléfono")
     project = fields.One2many("project.project","empresas",string="Proyectos")
     numero_empleados = fields.Integer(string="Número de empleados")
     tam_empresa = fields.Char(string="Tamaño de la empresa",compute="_tamempresa",store=True)

     @api.depends('numero_empleados')
     def _tamempresa(self):
          for r in self:
               if r.numero_empleados > 0:
                    r.tam_empresa = 'Pequeña'
               if r.numero_empleados > 50:
                    r.tam_empresa = 'Mediana'
               if r.numero_empleados > 100:
                    r.tam_empresa = 'Grande'
class proyectoadrianarmas_proyectos(models.Model):
     _name = 'project.project'
     _inherit = "project.project"

     empresas = fields.Many2one("proyectoadrianarmas.empresas_contratadoras",string="Nombre de la empresa",required=True,ondelete="cascade")

class proyectoadrianarmas_tareas(models.Model):
     _name = 'project.task'
     _inherit = "project.task"

# class proyectoadrianarmas_tareas(models.Model):
#      _name = 'proyectoadrianarmas_tareas'
#      _description = 'proyectoadrianarmas_tareas'

#      name = fields.Char(string="Nombre de la tarea")
#      description = fields.Text(string="Descripcion de la tarea")

    
# class proyectoadrianarmas_subtareas(models.Model):
#      _name = 'proyectoadrianarmas_subtareas'
#      _description = 'proyectoadrianarmas_subtareas'

#      name = fields.Char(string="Nombre de la subtarea")
#      description = fields.Text(string="Descripcion de la subtarea")
