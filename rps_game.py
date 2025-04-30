from flask import Flask, render_template, request, session, redirect, url_for
import random

# Initialize the Flask app
app = Flask(__name__)
app.secret_key = 'bimbam'

# Choice options
choices = ['Akmuo', 'Šulinys', 'Žirklės']

# reward options
anecdotes = [
    "Anglijoje mirė vyriausybės narys, į tuometinį premjerą Vinstoną Čerčilį kreipėsi tūlas interesantas:"
    "<br>– Sere, ar jūs neprieštarausite, jei aš užimsiu jo vietą?"
    "<br>– Ne, – atsakė Čerčilis, – tačiau jums tai reikėtų suderinti su kapinių sargu.",

    "Važiuoja vilkas ir kiškis traukiniu. Kiškis miega pirmame aukšte, o vilkas – antrame. "
    "<br>Girdi kiškis kažkas bum nukrito ir klausia vilko:"
    "<br>– Ei, kas ten nukrito?"
    "<br>– Mano maikė."
    "<br>– Tai ko taip garsiai?"
    "<br>– Nespėjau nusivilkt.",

    "- Ačiū, teta, už dovaną, - sako Petriukas."
    "<br>- Neverta dėkoti, mano mielasis, - šypsosi teta."
    "<br>- Ir aš taip manau, bet mama liepė..."
]


fun_facts = [
    "1913 metais JAV buvo legalu vaikus siųsti paštu.",
    "Aštunkojai turi 3 širdis",
    "Citrinose yra daugiau cukraus nei braškėse"
]

surprise = [
    "Didžiuojuosi Tavimi",
    "https://www.youtube.com/watch?v=y0sF5xhGreA",
    " :)"
]

# Main game view
@app.route('/')
def home():
    session['user_score'] = 0
    session['computer_score'] = 0
    session['round'] = 1
    return render_template('play.html')

# Each round algorithm
@app.route('/play', methods=['POST'])
def play():
    user_choice = request.form['choice']
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "Lygiosios!"
    elif (user_choice == 'Akmuo' and computer_choice == 'Žirklės') or \
         (user_choice == 'Šulinys' and computer_choice == 'Akmuo') or \
         (user_choice == 'Žirklės' and computer_choice == 'Šulinys'):
        result = "Laimėjai Tu 💗"
        session['user_score'] += 1
    else:
        result = "Aš laimėjau!!😜"
        session['computer_score'] += 1

    session['round'] += 1

    if session['round'] > 10:
        if session['user_score'] > session['computer_score']:
            return redirect(url_for('reward'))
        else:
            return redirect(url_for('game_over'))

    return render_template('play.html', result=result, user_choice=user_choice, computer_choice=computer_choice)

# Outcome if user won the game - reward options
@app.route('/reward')
def reward():
    return render_template('reward.html')

# Show the chosen prize
@app.route('/claim_reward', methods=['POST'])
def claim_reward():
    reward_type = request.form['reward']

    if reward_type == 'anecdotes':
        reward_text = random.choice(anecdotes)
    elif reward_type == 'fun_facts':
        reward_text = random.choice(fun_facts)
    elif reward_type == 'surprise':
        reward_text = random.choice(surprise)
    else:
        reward_text = "Unknown reward!"

    return render_template('result.html', reward_text=reward_text)

# Show when the player lost or if there were draws
@app.route('/game_over')
def game_over():
    return render_template('game_over.html', user_score=session.get('user_score', 0), computer_score=session.get('computer_score', 0))

# Clear session and restart the game
@app.route('/reset')
def reset():
    session.clear()
    return redirect(url_for('home'))

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
