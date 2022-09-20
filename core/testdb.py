import sqlite3

dbURL = r'core/db_voting_1.db'

def fGetPostsAndOptions(postID):
    connection = sqlite3.connect(dbURL)
    cur = connection.cursor()

    queryPost = f"SELECT * FROM posts where post_id = {postID}"
    cur.execute(queryPost)
    postsData = cur.fetchone()

    queryOptions = f"select * from options where post_id = {postID}"
    cur.execute(queryOptions)
    optionsData = cur.fetchall()

    if len(postsData) == 0:
        return None
    
    print("posts data")
    print(postsData)
    print("\noptions data", optionsData)
    return "success"


# working perfectly
def fUpdateOptions(postID, HTMLvalue):
    try:
        connection = sqlite3.connect(dbURL)
        cur = connection.cursor()

        query = f"select * from options where post_id = {postID}"
        cur.execute(query)
        optionsData = cur.fetchall()
        optionID = optionsData[HTMLvalue][0]
        print("option_id option = ",optionID)
        print("corresponding value = ", optionsData[HTMLvalue][3])

        queryUpdate = f"""update options set vote_count = vote_count + 1 where option_id = {optionID}"""
        cur.execute(queryUpdate)
        connection.commit()
        return "success"
    except sqlite3.Error as err:
        print(err)
        return "failure"

fGetPostsAndOptions(1)


fUpdateOptions(3,3)