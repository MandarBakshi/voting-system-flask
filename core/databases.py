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