from flask import Blueprint, url_for, request, render_template, session, redirect

views = Blueprint('views', __name__)

@views.route('/')
def fHandleHome():
    from .databases import fGetPostsDataShort
    homeData = fGetPostsDataShort()
    return render_template('home.html', postData = homeData)


@views.route('/posts/post/<id1>/', methods = ["POST", "GET"])
def fHandlePostPage(id1):
    id = int(id1)
    # postID = request.args.get('post')
    if request.method == "POST":
        formdata = request.form.get("option")
        print("\n\nformdata = ", formdata, "\n\n")
        from .databases import fUpdateOptions
        res = fUpdateOptions(id, formdata)
        if res == "success":
            return "success"
        elif res == None:
            return "failure"

    if request.method == "GET":
        from .databases import fGetPostAndOptions
        res = fGetPostAndOptions(id)
        return render_template('postDetails.html', postData = res)



@views.route('/users/user')
def fHandleViewProfilePage():
    userID = request.args.get('uid')
    return f"you are viewing profile of user {userID}"



@views.route('/login/', methods = ['POST', 'GET'])
def fHandleLoginPage():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        from .databases import fGetLoginData
        userData = fGetLoginData(username, password)

        if userData != None:
            session['userdata'] = userData
            session['is_logged_in'] = True
            print("\n\n\nsession data = ", session, "\n\n")
            # return render_template('home.html', userData)
            return redirect(url_for('views.fHandleHome'))
        else:
            return render_template('login.html', error = "Incorrect credentials")
    
    if request.method == "GET":
        return render_template('login.html', error = None)