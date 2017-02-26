from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import random
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
	curr = db.cursor()
	curr = db.execute("SELECT emoji_name FROM categories WHERE id=(?)", (id,))
	curr = curr.fetchall()
	return jsonify(curr)

@app.route('/getRandomEmojis/', methods=['GET'])
def get_random_emojis():
	emoji_list = []
	db = connect_db() 
	curr = db.cursor()
	for i in range(0,10): 
		curr = db.execute("SELECT emoji_name FROM categories WHERE id=(?)", (random.randint(0,2351),))
		curr = curr.fetchall()
		emoji_list.append(curr[0][0])
	return json.dumps(emoji_list)

@app.route('/getEmojiByName/<name>', methods=['GET'])
def get_emoji_by_name(name):
	db = connect_db() 
	curr = db.cursor()
	curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name=(?)", (name,))
	curr = curr.fetchone()
	return jsonify(curr)



@app.route('/getEmojiByCategory/<category>', methods=['GET'])
def get_emoji_by_category(category):
	db = connect_db() 
	curr = db.cursor()
	curr = db.execute("SELECT emoji_name FROM categories WHERE category=(?)", (category,))
	emoji_list = []
	for emoji in curr:
		emoji_list.append(emoji[0])
		print type(emoji[0])
	return json.dumps(emoji_list)



if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)

