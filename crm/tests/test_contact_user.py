# -*- encoding: utf-8 -*-
# from django.db import IntegrityError
# from django.test import TestCase
#
# from crm.tests.model_maker import (
#     make_contact,
#     make_user_contact,
# )
# from crm.tests.scenario import (
#     default_scenario_crm,
# )
# from login.tests.scenario import (
#     default_scenario_login,
#     get_user_fred,
#     get_user_sara,
#     user_contractor,
# )
#
#
# class TestContactUser(TestCase):
#
#     def test_link_user_to_contact(self):
#         """Create a contact and link it to a user"""
#         user_contractor()
#         default_scenario_login()
#         default_scenario_crm()
#         user = get_user_fred()
#         self.assertIn("Fred's Farm", user.usercontact.contact.name)
#
#     def test_one_contact_per_user(self):
#         """Make sure a user can only link to one contact"""
#         user_contractor()
#         default_scenario_login()
#         default_scenario_crm()
#         self.assertRaises(
#             IntegrityError,
#             make_user_contact,
#             get_user_sara(),
#             make_contact('zoo', 'Bristol Zoo')
#         )
