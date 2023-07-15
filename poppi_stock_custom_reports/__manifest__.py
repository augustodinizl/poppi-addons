# Copyright 2023 Escodoo
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Poppi Stock Custom Reports',
    'summary': """
<<<<<<< HEAD
        Custom QWEB reports for Poppi: "Minuta de transporte" and "Etiqueta de Pacote"""",
=======
        Custom QWEB reports for Poppi: 'Minuta de transporte' and 'Etiqueta de Pacote'""",
>>>>>>> 4e30721 (test1)
    'version': '14.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Escodoo',
    'website': 'https://www.escodoo.com.br',
    'depends': [
        'stock',
        'l10n-br'
    ],
    'data': [
        'report/etiqueta.xml',
        'report/minuta.xml'
    ],
    'demo': [],
    'qweb': [],
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,

}
