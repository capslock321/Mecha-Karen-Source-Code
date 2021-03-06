"""
Copyright ©️: 2020 Seniatical / _-*™#7519
License: Apache 2.0

A permissive license whose main conditions require preservation of copyright and license notices.
Contributors provide an express grant of patent rights.

Licensed works, modifications, and larger works may be distributed under different terms and without source code.

FULL LICENSE CAN BE FOUND AT:
    https://www.apache.org/licenses/LICENSE-2.0.html

Any violation to the license, will result in moderate action
You are legally required to mention (original author, license, source and any changes made)
"""

user_data = '''
SELECT 
    (Strikes, Logged_In, Registered_At, Messages, Bot, Commands, Email, Password, Servers, Premium, LastUpdate, Admin, SupportBoosts)
FROM 
    "users" 
WHERE 
    UserID = ? AND GuildID = ? AND name LIKE %GuildID%
'''

warns = '''
SELECT
    *
FROM
    "warns"
WHERE
    UserID = ? AND GuildID = ? AND name LIKE %warn% AND CASE = ?
'''

starboard = '''
SELECT
    *
FROM
    "starboard"
WHERE
    GuildID = ?
'''

add_to_db = '''
INSERT INTO Users
    (Strikes, Logged_In, Registered_At, Messages, Bot, Commands, Email, Password, Servers, Premium, LastUpdate, Admin, SupportBoosts)
VALUES
    (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''
