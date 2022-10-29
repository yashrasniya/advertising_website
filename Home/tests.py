# from django.test import TestCase
#
# # Create your tests here.
# import razorpay
#
# client = razorpay.Client(auth=("rzp_test_vlK7qms1BtJdXt", "GmrIdfs0XYoLWtXsY2E7D5pk"))
#
# # r = client.qrcode.create({
# #     "type": "upi_qr",
# #     "name": "Store Front Display",
# #     "usage": "single_use",
# #     "fixed_amount": True,
# #     "payment_amount": 300,
# #     "description": "For Store 1",
# #     "customer_id": "cust_K2HwuIbPNILo7O",
# #     "close_by": 1681615838,
# #     "notes": {
# #         "purpose": "Test UPI QR Code notes"
# #     }
# # })
# # print(r)
#
# p = client.payment_link.create({
#     "amount": 1000,
#     "currency": "INR",
#     "accept_partial": False,
#     "first_min_partial_amount": 100,
#     "reference_id": "0142",
#     "callback_url": "https://yashraniya.pythonanywhere.com/",
#     "description": "Payment for policy no #23456",
#     "customer": {
#         "name": "Gaurav Kumar",
#         "contact": "+918938095294",
#         "email": "yashrasniya3@gmail.com"
#     },
#     "notify": {
#         "sms": False,
#         "email": False
#     },
#     "reminder_enable": True,
#     "options": {
#         "checkout": {
#             "theme": {
#                 "hide_topbar": True
#             }
#         }
#     }
# })
#
# print(p)
# h = {'accept_partial': True, 'amount': 1000, 'amount_paid': 0, 'cancelled_at': 0, 'created_at': 1659776249,
#      'currency': 'INR',
#      'customer': {'contact': '+918938095294', 'email': 'yashrasniya3@gmail.com', 'name': 'Gaurav Kumar'},
#      'description': 'Payment for policy no #23456', 'expire_by': 0, 'expired_at': 0, 'first_min_partial_amount': 100,
#      'id': 'plink_K2I0rUZbeygr4S', 'notes': None, 'notify': {'email': False, 'sms': False}, 'payments': None,
#      'reference_id': '012', 'reminder_enable': True, 'reminders': [], 'short_url': 'https://rzp.io/i/ZpZS1lcI',
#      'status': 'created', 'updated_at': 1659776249, 'upi_link': False, 'user_id': ''}
#
razorpay_payment_id='pay_K2IgJvvcvK3YmO&' \
                    'razorpay_payment_link_id=plink_K2IfTzaPgsKI1k&' \
                    'razorpay_payment_link_reference_id=0142' \
                    '&razorpay_payment_link_status=paid&' \
                    'razorpay_signature=24a194564adaf98df5edb9caa8408f064bb59c35945c5457a49bb21903a5e3fd'

import razorpay
client = razorpay.Client(auth=("rzp_test_vlK7qms1BtJdXt", "GmrIdfs0XYoLWtXsY2E7D5pk"))

o=client.utility.verify_payment_link_signature({
   'payment_link_id': 'plink_K2IfTzaPgsKI1k',
   'payment_link_reference_id': '0142',
   'payment_link_status':'paid',
   'razorpay_payment_id': 'pay_K2IgJvvcvK3YmO',
   'razorpay_signature': '24a194564adaf98df5edb9caa8408f064bb59c35945c5457a49bb21903a5e3fd'
   })


print(o)

