import logging


def migrate(cr, version):
    """
    The old module website_facebook_pixel was replaced by another with the same name.
    To ensure correct installation of the new module, we need to manually delete the
    old view.
    """
    logger = logging.getLogger("odoo.addons.website_google_tag_manager.migrations."
                               "odoo16.7567")
    cr.execute(
        """
        delete from ir_ui_view v
        using ir_model_data d
        where d.res_id = v.id
            and d.name = 'res_config_settings_view_form_google_tag_manager'
            and d.module = 'website_google_tag_manager'
        """
    )
    logger.info(
        "Deleted %s views regarding res_config_settings_views",
        cr.rowcount
    )
    cr.execute(
        """
        delete from ir_model_data d
        where d.name = 'res_config_settings_view_form_google_tag_manager'
            and d.module = 'website_google_tag_manager'
        """
    )
    logger.info(
        "Deleted %s model data entries regarding res_config_settings_views",
        cr.rowcount
    )
