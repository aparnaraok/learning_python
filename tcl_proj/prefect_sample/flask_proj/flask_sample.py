 
@app.route('/demo_app')
def demo_app():
    query    = request.args.get('query')
    result   = subprocess.check_output('''curl -X POST -H "Content-Type: application/json" -d "{\\"data\\":{\\"ndarray\\":[[\\"'''+query+ '''}\\"]]}}" http://10.71.3.3:32389/seldon233     result   = json.loads(result)''')
    emotion  = 'positive'
    color    = 'bg-green'
    if result['data']['ndarray'][0][0] == 'pos':
        emotion = 'positive'
    else :
        emotion = 'negative'
        color   = 'bg-red'
    return render_template('emotion.html', color = color)
    # return render_template('deploytables.html', statuses=statuses)
    # return  flask.Response(pods, mimetype='text/plain')

@app.route('/demoui', methods=['GET', 'POST'])
def demoui():
    form = DemoForm()
    if form.validate_on_submit():
        #print(request.form.to_dict())
        args = copy.deepcopy(request.form.to_dict())
        del args['csrf_token']
        return redirect(url_for('demo_app',**args))
    return render_template('demo.html', title='nexo', form=form) 
 
