# -*- coding: utf-8 -*-
{
    'name': "contact_form_leads",

    'summary': """ MODIFICACIONES FORMULARIO DE CONTACTO DE OPORTUNIDADES """,

    'description': """
        Queremos customizar el módulo de oportunidades (CRM) y su formulario de contacto:
• En el modelo de la oportunidad añadir un campo seleccionable donde el usuario deberá de
indicar a través de que fuente ha dado con la empresa: “Terceros/Redes sociales/Búsqueda
en Internet”. Será un campo seleccionable a mostrar en la vista formulario del backend y
frontend (website).
• En la parte website, del formulario de contacto por un lado quitar el teléfono, hacer no
requerido la compañía y además mostrar este campo seleccionable que será requerido en el
que el usuario deberá de seleccionar de que fuente ha dado con la empresa:
“Terceros/Redes sociales/Búsqueda en Internet”.
• Añadir validación al campo del e-mail.
    """,

    'author': "David Conde Cubas",
    'website': "https://www.linkedin.com/in/david-conde-cubas-6a16a619a/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'crm', 'website_crm'],

    # always loaded
    'data': [
        # views
        'views/inherited/crm_lead.xml',

        # templates
        'views/templates/website_crm_contactus_form.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'post_init_hook': 'add_source_to_whitelist'
}
