from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
from odoo.tests.common import Form

@tagged('post_instal','-at_install')
class EstateTestCase(TransactionCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        cls.buyer = cls.env['res.partner'].create({
            'name': 'buyer',
        })
        
        cls.properties = cls.env['estate.model'].create([{
            'name': 'property_op',
            'expected_price': 99999,
        }])
        
        cls.offers = cls.env['estate.property.offer'].create([{
            'partner_id': cls.buyer.id,
            'property_id': cls.properties[0].id,
            'price': 9999,
        }])
        
    def test_action(self):
         with self.assertRaises(UserError):
            self.properties.action_sold()
             
         self.offers.action_accept()
         self.properties.action_sold()
         self.assertRecordValues(self.properties, [
            {'state': 'sold'},
         ])
         
         with self.assertRaises(UserError):
            self.env['estate.property.offer'].create([{
                'partner_id': self.buyer.id,
                'property_id': self.properties[0].id,
                'price': 99999,
            }])
            
            # docker exec -it e2595ed76d22 odoo --log-level=test --test-tags=/estate:TestEstate.test_action -d test10 --stop-after-init -p 10989 -r odoo -w odoo
            
            # docker exec -it e2595ed76d22 odoo -i estate --http-port=5000 --test-enable --log-level=test -d test2 -r odoo -w odoo --stop-after-init
            
    def test_property_form(self):
        with Form(self.properties[0]) as prop:
            self.assertEqual(prop.garden_area, 0)
            self.assertIs(prop.garden_orientation, False)
            prop.garden = True
            self.assertEqual(prop.garden_area, 10)
            self.assertEqual(prop.garden_orientation, "N")
            prop.garden = False
            self.assertEqual(prop.garden_area, 0)
            self.assertIs(prop.garden_orientation, False)        