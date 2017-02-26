from flask import Flask, render_template, request, redirect, url_for, jsonify, json
import random
import sqlite3
app = Flask(__name__)

def connect_db():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
	emojis = json.loads(get_random_emojis())
	return render_template('index.html', emojis = emojis)

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
	category = name
	db = connect_db() 
	curr = db.cursor()
	curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name = (?)", (name,))
	curr = curr.fetchall()
	return jsonify(curr)

@app.route('/getEmoji/<term>', methods=['GET'])
def get_emoji(term):
	db = connect_db() 
	curr = db.cursor()
	curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name = (?) OR category = (?)", (term, term,))
	curr = curr.fetchall()
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

@app.route('/getEmojiContains/<term>', methods=['GET'])
def get_emoji_contains(term):
	print(term)
	thing = term
	print(thing)
	db = connect_db() 
	curr = db.cursor()
	if term == 'face':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%face%'")
	elif term == 'medal':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%medal%'")
	elif term == 'sign':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%sign%'")	
	elif term == 'baby':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%baby%'")		
	elif term == 'arrow':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%arrow%'")
	elif term == 'hand':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%hand%'")	
	elif term == 'black':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%black'")
	elif term == 'white':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%white%'")	
	elif term == 'blonde':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%blonde'")
	elif term == 'hair':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%hair%'") 	
	elif term == 'fish':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%fish%'") 	
	elif term == 'boy':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%boy%'")	
	elif term == 'girl':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%girl'") 	
	elif term == 'dark':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%dark%'") 	
	elif term == 'light':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%light%'") 	
	elif term == 'medium':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%medium%'")
	elif term == 'cat':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%cat%'") 
	elif term == 'heart':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%heart%'")
	elif term == 'kiss':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%kiss%'")
	elif term == 'button':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%button%'") 	
	elif term == 'man':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%man%'")
	elif term == 'woman':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%woman%'")
	elif term == 'person':
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%person%'")
	elif term == ('smile') :
		curr = curr.execute("SELECT emoji_name FROM categories WHERE emoji_name LIKE '%smile' OR emoji_name LIKE '%smiling'")
	curr = curr.fetchall()
	return jsonify(curr)

if __name__ == '__main__':
	app.debug = True
	app.run(port = 8000)

