# -*- coding: utf-8 -*-
# Definición del manifiesto del módulo 'Hola Mundo'

{
    'name': "Hola Mundo", # Nombre del módulo que aparecerá en la lista de Aplicaciones
    'summary': """Primer módulo de ejemplo para la Práctica 3.""", # Breve descripción
    'description': """
        Módulo básico para demostrar la estructura de archivos
        y la instalación de un nuevo addon en Odoo.
    """, # Descripción detallada
    'author': "Rafael N",
    'website': "https://github.com/rafaAuEs/Tere_Practica_3.git", # Si tienes una web o GitHub
    'category': 'Uncategorized',
    'version': '1.0', # Versión del módulo


    'depends': ['base'], 


    'data': [

    ],
    
    # Este módulo es una aplicación (aparecerá en la vista de Apps)
    'application': True, 
    'installable': True,
    'auto_install': False,
}