from flask import Flask, request, redirect, url_for 
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.database import Base

engine=create_engine('sqlite:///database.db',echo=True)
Base.metadata.bind=engine
session = scoped_session(sessionmaker(bind=engine))

from controllers import article
articles = article.Article(session)

@app.teardown_request
def remove_session(ex=None):
    session.remove()
    
@app.route('/')
@app.route('/blog')
def Blog():
    return redirect(url_for('Index'),302)
    
@app.route('/blog/index')
def Index():
    return articles.index();

@app.route('/blog/create',methods=['GET','POST'])
def Create():
    return articles.create(request.method)
    
@app.route('/blog/show/<int:id>')
def Show(id):
    return articles.show(id);    

@app.route('/blog/edit/<int:id>',methods=['GET'])
def Edit(id):
    return articles.edit(id)
    
@app.route('/blog/update',methods=['POST','PUT','PATCH','DELETE'])
def Update():
    return articles.update(request.method)
        
@app.route('/blog/delete/<int:id>')
def Delete(id):
    return articles.delete(request.method)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
