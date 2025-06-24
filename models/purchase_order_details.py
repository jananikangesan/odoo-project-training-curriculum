from odoo import models, fields, api

class PurchaseOrderDetails(models.Model):

    _inherit = "purchase.order.line"

    product_tmpl_id = fields.Many2one("product.template", string="Products")

    @api.onchange("product_id")
    def _onchange_product_tmpl_id(self):
        if self.product_id:
            result = self.env["product.product"].search([('id', '=', self.product_id.id)])
            self.product_tmpl_id = result.product_tmpl_id
