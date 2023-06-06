from odoo import http


class DeliveryUPS(http.Controller):
    @http.route(["/ups/confirm"], type="http", auth="user", methods=["GET"])
    def ups_oauth_confirm(self):
        # TODO: Add logic
        return http.redirect_with_hash("/web")
