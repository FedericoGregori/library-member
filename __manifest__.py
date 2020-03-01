{
    'name': 'Library Members',
    'description': 'Manage library members who could borrow books.',
    'author': 'Federico Gregori',
    'website': 'https://github.com/FedericoGregori',
    'category': 'Library',
    'depends': ['library_app','mail'],

    'application': False,

    'data': [
        'security/library_security.xml',
        'security/ir.model.access.csv',
        'views/library_menu.xml',
        'views/book_view.xml',
        'views/member_view.xml',
        'views/book_list_template.xml',
    ],
}