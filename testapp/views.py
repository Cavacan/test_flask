from flask import render_template, request
from random import randint
from testapp import app

@app.route('/')
def index():
    my_dict = {
        "insert_something1" : "views.pyのinsert_something1部分です。",
        "insert_something2" : "views.pyのinsert_something2部分です。",
        "test_titles" : ["title1", "title2", "title3"]
    }
    return render_template('testapp/index.html', my_dict=my_dict)

@app.route('/test')
def other1():
    return render_template('testapp/index2.html')

@app.route('/sampleform', methods=['GET', 'POST'])
def sample_form():
    if request.method == 'GET':
        return render_template('testapp/sampleform.html')
    if request.method == 'POST':
        hands = {
            '0':'グー',
            '1':'チョキ',
            '2':'パー'
        }
        janken_mapping = {
            'draw': 'draw',
            'win' : 'win',
            'lose' : 'lose'
        }

        player_hand_ja = hands[request.form['janken']]
        player_hand = int(request.form['janken'])
        enemy_hand = randint(0, 2)
        enemy_hand_ja = hands[str(enemy_hand)]
        if player_hand == enemy_hand:
            judgement = 'draw'
        elif (player_hand == 0 and enemy_hand == 1) or ( player_hand == 1 and enemy_hand == 2) or ( player_hand == 2 and enemy_hand == 0):
            judgement = 'win'
        else:
            judgement = 'lose'
        print(f'じゃんけん開始: enemy_hand: {enemy_hand}, player_hand: {player_hand}, judgement: {judgement}')
        result = {
            'enemy_hand_ja': enemy_hand_ja,
            'player_hand_ja': player_hand_ja,
            'judgement': janken_mapping[judgement]
        }
        return render_template('testapp/janken_result.html', result=result)



