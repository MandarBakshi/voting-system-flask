import sqlite3

dbURL = r'core/db_voting_1.db'

def fGetPostAndOptions(postID):
    try:
        connection = sqlite3.connect(dbURL)
        cur = connection.cursor()

        queryPosts = f"SELECT * FROM posts WHERE post_id = {postID}"
        cur.execute(queryPosts)
        postsData = cur.fetchone()

        queryOptions = f"SELECT * FROM options WHERE post_id = {postID}"
        cur.execute(queryOptions)
        optionsData = cur.fetchall()

        return {
            "post" : postsData,
            "options" : optionsData
        }
    
    except sqlite3.Error as error:
        print(error)
        return None


def fUpdateOptions(postID, HTMLvalue):
    try:
        tempdata = fGetPostAndOptions(postID)
        optionID = int(tempdata["options"][int(HTMLvalue)][0])
        print("option id - ", optionID, " - ", tempdata.options[int(HTMLvalue)][3])
        queryUpdate = f"""UPDATE options SET vote_count = vote_count + 1 WHERE option_id = {optionID}"""
        
        connection = sqlite3.connect(dbURL)
        cur = connection.cursor()
        cur.execute(queryUpdate)
        return "success"
    
    except sqlite3.Error as err:
        print(err)
        return None



def fGetLoginData(uname, password):
    try:
        connection = sqlite3.connect(dbURL)
        cur = connection.cursor()

        query = f"SELECT * FROM users WHERE username = '{uname}' AND password = '{password}'"

        cur.execute(query)
        tempData = cur.fetchone()
        print(tempData)

        userData = {
            "user_id" : tempData[0],
            "name" : tempData[1],
            "username" : tempData[2],
            "email" : tempData[3],
            "password" : tempData[4],
            "account_created_on" : tempData[5]
        }
        print("JSON userdata = \n",userData)
        return userData
    
    except sqlite3.Error as err:
        print(err)
        return None
    
    finally:
        connection.close()



def fGetPostsDataShort():
    try:
        connection = sqlite3.connect(dbURL)
        cur = connection.cursor()

        query = "SELECT * FROM posts"
        cur.execute(query)

        tempData = cur.fetchall()
        tempdict = {}
        arr = []
        for x in tempData:
            tempdict = {
                "post_id" : x[0],
                "user_id" : x[1],
                "username" : x[2],
                "name" : x[3],
                "post_title" : x[4],
                "post_description" : x[5],
                "total_votes" : x[6],
                "posted_on" : x[7]
            }
            arr.append(tempdict)
        print(arr)
        return arr
    
    except sqlite3.Error as err:
        print(err)
        return None
    
    finally:
        connection.close()