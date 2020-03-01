from odoo import fields, models


class Member(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    card_number = fields.Char()
    partner_id = fields.Many2one(
        'res.partner',
        delegate=True,
        ondelete='cascade',
        required=True
    )

# With delegation inheritance, the library.member Model embeds the inherited Model, res.partner, so that when a
# new Member record is created, a related Partner is automatically created and referenced in the partner_id field.

# Note that the same is not true for Model methods:
# the methods from the Partner Model are not made available in the Member Model.

