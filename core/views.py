from flask import Blueprint, url_for, request, render_template

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