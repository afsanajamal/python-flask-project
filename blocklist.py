"""""
blocklist.py

This file just contains the blocklist of JWT tokens. It will be imported by 
app and the logout resource so that the tokens can be added to the blocklist when the user logs out.
"""

BLOCKLIST = set()
