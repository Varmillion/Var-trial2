from datetime import datetime
from flask import make_response, abort

import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='varmillion',
                             db='remote',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

# def get_timestamp():
#     return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

def readAll():
    # Show table values!!
    mysql = connection.cursor()
    query = "SELECT * FROM users"
    mysql.execute(query)
    result = mysql.fetchall()
    connection.commit()
    print(result)
    return result

# def writeAll(user_name, user_email, user_password):
#     # Show table values!!
#     mysql = connection.cursor()
#     query = "INSERT INTO users (username, email, password ) VALUES (%s,%s,%s)"
#     mysql.execute(query, ( user_name, user_email, user_password))
#     result = mysql.fetchall()
#     connection.commit()
#     print(result)
#     return result


def writeAll(user_name, user_email, user_password, user_landOwner):
    # Show table values!!
    mysql = connection.cursor()
    query = "INSERT INTO users (username, email, password, landOwner ) VALUES (%s,%s,%s,%s)"
    mysql.execute(query, ( user_name, user_email, user_password, user_landOwner))
    result = mysql.fetchall()
    connection.commit()
    print(result)
    return result



def readwithId(user_id):
    # Show table values!!
    mysql = connection.cursor()
    query1= "SELECT * FROM users where id={0}".format(user_id)
    mysql.execute(query1)
    result = mysql.fetchall()
    connection.commit()
    print(result)
    return result


def readUser(user_name):
    # Show table values!!
    mysql = connection.cursor()
    query2= "SELECT * FROM users where username='{0}'".format(user_name) 
    mysql.execute(query2)
    result1 = mysql.fetchall()
    connection.commit()
    print(result1)
    return result1

# def readOne(user_name):
#     # Show table values!!
#     mysql = connection.cursor()
#     query2= "SELECT * FROM users where username=%s"
#     # query2= "SELECT * FROM users where username=' "+user_name+" '"
#     mysql.execute(query2,(user_name,))
#     result1 = mysql.fetchall()
#     connection.commit()
#     print(result1)
#     return result1



# def readOne(user_name):
#     # Show table values!!
#     mysql = connection.cursor()
#     query2= "SELECT * FROM users where username=%s",(user_name,)
#     # query2= "SELECT * FROM users where username=' "+user_name+" '"
#     mysql.execute(query2)
#     result1 = mysql.fetchall()
#     connection.commit()
#     print(result1)
#     return result1



def readAllLand():
    # Show table values!!
    mysql = connection.cursor()
    query4 = "SELECT * FROM land"
    mysql.execute(query4)
    result3 = mysql.fetchall()
    connection.commit()
    print(result3)
    return result3

def readPin(land_pin):
    # Show table values!!
    mysql = connection.cursor()
    query3= "SELECT * FROM land where pincode={0}".format(land_pin)
    mysql.execute(query3)
    result2 = mysql.fetchall()
    connection.commit()
    print(result2)
    return result2

# def readLArea(land_area):
#     # Show table values!!
#     mysql = connection.cursor()
#     query= "SELECT * FROM land where areaSize={0}".format(land_area)
#     mysql.execute(query)
#     result = mysql.fetchall()
#     connection.commit()
#     print(result)
#     return result

# def readLandName(land_name):
#     # Show table values!!
#     mysql = connection.cursor()
#     query3= "SELECT * FROM land where name={0}".format(land_name)
#     mysql.execute(query3)
#     result2 = mysql.fetchall()
#     connection.commit()
#     print(result2)
#     return result2



    # ---------------------
    # query1 = "SELECT * FROM users where password = '"+password+"'"
   #  result = query1.fetchall()
   #  print(len(result))
   #  if password in users:

   #     ikuser = users.get(password)
   # else:
   #     abort(
   #         404, "Person with password {password} not found".format(password=password)
   #     )
    
    
    # if lname in PEOPLE:
    #     person = PEOPLE.get(lname)

    # # otherwise, nope, not found
    # else:
    #     abort(
    #         404, "Person with last name {lname} not found".format(lname=lname)
    #     )



# def readOne(userName):
#     """
#     This function responds to a request for /api/people/{lname}
#     with one matching person from people
#     :param lname:   last name of person to find
#     :return:        person matching last name
#     """
#     # Does the person exist in people?
#     if userName in USER:
#         ikuser = USER.get(userName)

#     # otherwise, nope, not found
#     else:
#         abort(
#             404, "Person with user name {userName} not found".format(userName=userName)
#         )

#     return ikuser

# def create(ikuser):

#     userName = ikuser.get("userName", None)
#     lname = ikuser.get("lname", None)
#     fname = ikuser.get("fname", None)

#     if userName not in USER and userName is not None:
#         USER[userName] = {
#             "userName": userName,
#             "lname": lname,
#             "fname": fname,
#             "timestamp": get_timestamp(),
#         }
#         return make_response(
#             "{userName} successfully created".format(userName=userName), 201
#         )
#     else:
#         abort(
#             406,
#             "Peron with last name {userName} already exists".format(userName=userName),
#         )

# def update(userName, ikuser):
#     """
#     This function updates an existing person in the people structure
#     :param lname:   last name of person to update in the people structure
#     :param person:  person to update
#     :return:        updated person structure
#     """
#     # Does the person exist in people?
#     if userName in USER:
#         USER[userName]["fname"] = ikuser.get("fname")
#         USER[userName]["timestamp"] = get_timestamp()

#         return USER[userName]

#     # otherwise, nope, that's an error
#     else:
#         abort(
#             404, "Person with last name {userName} not found".format(userName=userName)
#         )

# def delete(userName):
#     """
#     This function deletes a person from the people structure
#     :param lname:   last name of person to delete
#     :return:        200 on successful delete, 404 if not found
#     """
#     # Does the person to delete exist?
#     if userName in USER:
#         del USER[userName]
#         return make_response(
#             "{userName} successfully deleted".format(userName=userName), 200
#         )

#     # Otherwise, nope, person to delete not found
#     else:
#         abort(
#             404, "Person with last name {userName} not found".format(userName=userName)
#         )








# query2= "SELECT * FROM users where username= {0}".format(user_name)
    # query2= "SELECT * FROM users where username=' "+user_name+" '"
    # query2="SELECT * FROM users WHERE username LIKE %s"
    # mysql.execute(query2,(user_name, ))
    # mysql.execute(query2, ('varaa'))









