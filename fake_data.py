import random
import datetime
from uuid import uuid4
from models import *

user = User(id=str(uuid4()), username='john', password='123456')
db.session.add(user)
db.session.commit()

user=User.query.first()
tag1=Tag(id=str(uuid4()), name='Python')
tag2 = Tag(id=str(uuid4()), name='Flask')
tag3 = Tag(id=str(uuid4()), name='SQLALchemy')
tag4 = Tag(id=str(uuid4()), name='Migrate')
tag_list = [tag1, tag2, tag3, tag4]

s="EXAMPLE TEXT"

for i in range(100):
    newpost = Post(id=str(uuid4()), title='Post'+str(i))
    newpost.user = user
    newpost.publish_data = datetime.datetime.now()
    newpost.text = s
    newpost.tags = random.sample(tag_list, random.randint(1,3))
    db.session.add(newpost)

db.session.commit()