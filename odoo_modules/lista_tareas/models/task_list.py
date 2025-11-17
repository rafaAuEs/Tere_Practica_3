# -*- coding: utf-8 -*-

from odoo import models, fields

# Definición del modelo (Tabla)
class TaskList(models.Model):
    # 'task.list' es el nombre técnico del modelo (tabla en la BD)
    _name = 'task.list'
    _description = 'Modelo para gestionar la lista de tareas'

    # --- CAMPOS DEL MODELO ---
    
    # Campo de texto (requerido), que se usará como el nombre principal del registro
    name = fields.Char(string='Tarea', required=True)
    
    # Campo booleano (checkbox) para marcar si la tarea está completada
    is_completed = fields.Boolean(string='Completada', default=False)
    
    # Campo de texto multilínea para la descripción detallada
    description = fields.Text(string='Descripción')
    
    # Campo de fecha para registrar la creación (Odoo lo puede hacer automáticamente, pero lo definimos)
    creation_date = fields.Date(string='Fecha de Creación', default=fields.Date.today())