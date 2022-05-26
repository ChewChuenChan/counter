Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import base64
base64.urlsafe_b64decode('eyJjb3VudCI6NCwiY291bnRfcGx1cyI6MCwic3VtIjo0fQ===')
b'{"count":4,"count_plus":0,"sum":4}'
base64.urlsafe_b64decode('eyJjb3VudCI6MCwiY291bnRfcGx1cyI6MCwic3VtIjowfQ===')
b'{"count":0,"count_plus":0,"sum":0}'
