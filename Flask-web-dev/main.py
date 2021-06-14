from flask import Flask,render_template,request,url_for,redirect


app=Flask(__name__)

posts={
    0:{
        'id': 0,
        'title': 'Hello world !',
        'content': ' This is my first post'
    }
}

@app.route('/')
def main():
    return posts[0]['title']

@app.route('/post/<int:post_id>')   # /post/0
def post(post_id):
    post=posts.get(post_id)

    if not post:    # if no post is found i.e. None since get returns none.
        return render_template('404.html', message=f'Post with id {post_id} is not found')

    return render_template('post.jinja2',post=post)  #this file should ALWAYS be in Templates directory within the project.
    # return render_template('post_base.html',post=posts.get(post_id)) post is the post variable in html template.


#Jinja2 is the engine that is driving the html templates.  Can also use post.html ; its just that
#flask gives better syntax highlighting in appropriate pycharm version.
# if using community version , .html instead of .jinja2 is better... No other differences.

#404.html and post.html are children of base.jinja2 ( % extends jinja2 % does exactly that )

@app.route('/post/form')
def form():
    return render_template('create.jinja2')


# <form action="/post/create"> will send the data entered after clicking submit into create instead of /form
#http://...../post/create?title=blalal&post=blabla
@app.route('/post/create')
def create():
    title=request.args.get('title')  #can get args title , post etc
    content=request.args.get('content')
    post_id=len(posts)
    posts[post_id]={'id':post_id, 'title': title, 'content':content}

    return redirect(url_for('post', post_id=post_id))     #Go get the information in the url ,
                                                          # save it in database , and redirect to print
                                                          # the entered content in




if __name__ == '__main__':
    app.run(debug=True)

