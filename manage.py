from flask_script import Manager, Server, Shell
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import models
from flask_migrate import Migrate, MigrateCommand
from config import Devconfig

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object(Devconfig)


#Init manager object via app object
manager = Manager(app)
migrate = Migrate(app, models.db)

def make_shell_context():
    '''
    Create a python Cli.
    '''
    return dict(app=app, db=models.db, User=models.User, \
    Post=models.Post, Comment=models.Comment, Tag=models.Tag)

#Create a new commands:Server
#This command will be run the Flask development_env server
manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

def sidebar_data():
    """Set the sidebar function."""
    #Get post of recent
    recent = models.Post.query.order_by(Post.publish_data.desc()).limit(5).all()

    top_tags = db.session.query(
        Tag, func.count(posts_tags.c.post_id).label('total')
    ).join(
        posts_tags
    ).group_by(Tag).order_by('total DESC').limit(5).all()
    return recent, top_tags

@app.route('/')
@app.route('/<int:page>')
def home(page=1):
    """View function for home page"""
    posts = models.Post.query.order_by(Post.publish_data.desc()).paginate(page, 10)
    recent, top_tags = sidebar_data()
    return render_template('home.html', posts=posts, recent=recent, top_tags=top_tags)


@app.route('/post/<string:post_id>')
def post(post_id):
    """View function for post page"""
    post = models.Post.query.get_or_404(post_id)
    tags = post.tags
    comments = post.comments.order_by(Comment.date.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template(
        'post.html',
        tags=tags,
        comments=comments,
        recent=recent,
        top_tags=top_tags
    )


@app.route('/tag/<string:tag_name>')
def tag(tag_name):
    """View function for tag page"""
    tag = models.Tag.query.filter_by(name=tag_name).first_or_404()
    posts = tag.posts.order_by(Post.publish_data.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template(
        'tag.html',
        posts=posts,
        recent=recent,
        top_tags=top_tags
    )


if __name__ == '__main__':
    manager.run()