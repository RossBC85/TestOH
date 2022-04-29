# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

{
    "name": "Fleet Vehicle Services",
    "version": "14.0.1.0.0",
    "category": "Fleet",
    "development_status": "Beta",
    "author": "Rosselyn B",
    "summary": "List of vehicle services",
    "website": "",
    "license": "AGPL-3",
    "depends": ["base", "fleet"],
    "data": ['security/vehicle_groups.xml',
             'security/ir.model.access.csv',
              "data/fleet_demo_data.xml",
              "views/services_form.xml",
             "views/fleet_services_test_form.xml",
             "views/vehicle_test_form.xml"],
    # "pre_init_hook": "pre_init_hook",
    "installable": True,
    "auto_install": False,
}
