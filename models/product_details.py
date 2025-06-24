from odoo import models , fields,api


class ProductDetails(models.Model):
    _inherit="product.template"

    ordered_qty=fields.Float(string="Ordered Qty")
    sold_qty=fields.Float(string="Sold Qty")
    primary_vendor=fields.Many2one('res.partner', string="Primary Vendor",domain=[('supplier_rank', '>', 0)])
    mfg_ids=fields.Many2many('product.template',
        'product_template_mfg_rel',   # Explicit relation table
        'product_id',                 # Source column
        'mfg_product_id',              # Target column
        string="Mfg#",compute='_compute_mfg_ids',
        store=True,
        help="Populated from vendor product codes matching default codes of other products")

    filter_by_product=fields.Many2one("product.template", string="Filter by product")
    active_status=fields.Selection([("active","Active"),("inactive","Inactive")],string="Custom Active Status")

    purchase_order_ids = fields.One2many('purchase.order.line', 'product_tmpl_id', string="Purchase Order")

    @api.onchange('filter_by_product')
    def _onchange_filter_by_product(self):
            product = self.filter_by_product
            if product:
                self.name = product.name
                self.list_price = product.list_price
                self.standard_price = product.standard_price
                self.categ_id = product.categ_id.id
                self.detailed_type = product.detailed_type
                self.weight = product.weight
                self.volume = product.volume
                self.primary_vendor = product.primary_vendor.id
                self.ordered_qty = product.ordered_qty
                self.sold_qty = product.sold_qty
                self.active_status = product.active_status
                self.mfg_ids = [(6, 0, product.mfg_ids.ids)]

    @api.depends('seller_ids.product_code')
    def _compute_mfg_ids(self):
        for rec in self:
            product_codes = rec.seller_ids.mapped('product_code')
            matched_templates = self.env['product.template'].search([
                ('default_code', 'in', product_codes)
            ])
            rec.mfg_ids = [(6, 0, matched_templates.ids)]

