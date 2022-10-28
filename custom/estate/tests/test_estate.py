from odoo.tests.common import TransactionCase
from odoo.exceptions import UserError
from odoo.tests import tagged
#from odoo.tests.common import Form

@tagged('post_instal','-at_install')
class TestEstate(TransactionCase):

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
        
        # 58a71ce83358
        
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