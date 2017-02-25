from flask import Flask, render_template, request, redirect, url_for
import sqlite3
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getEmojiByID/<id>', methods=['GET'])
def get_emoji_by_id(id):
	db = connect_db() 
	curr = db.execute("SELECT emoji_name FROM categories WHERE id=?", id)
	curr = curr.fetchall()
	return curr[0]

@app.route('/getEmojiByCategory/<category>', methods=['GET'])
def get_emoji_by_category(category):
	db = connect_db() 
	curr = db.execute("SELECT * FROM categories WHERE category=(?)", (category,))
	curr = curr.fetchall()
	return curr[0][1]

if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)
