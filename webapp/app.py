import flask
import twilio.twiml
import json
import base64
import yaml


app = flask.Flask(__name__)


@app.route('/')
@app.route('/<string:state>')
def gather(state=None):
    tree = _get_tree()
    response = twilio.twiml.Response()
    if state is None:
        with response.gather(numDigits=1, action='/', method="POST") as g:
            g.say(_generate_script(tree), loop=3)
        return twiml(response)
    elif state:
        selected_option = flask.request.form['Digits']
        state = json.loads(base64.b64decode(state))
        app.logging.info('State: %s', state)
        path = state.get('choices', [])
        tree = _get_tree()
        options = tree.get('options', [])
        for choice in path:
            if len(options) <= choice:
                # TODO handle error
                break
            tree = options[choice]
            options = tree.get('options', [])
        if len(options) <= selected_option:
            # TODO handle error
            return _redirect_welcome()
        selection = options[selected_option]
        if 'number' in selection:
            response.dial(selection.get('number'))
            return twiml(response)
        elif 'options' in selection:
            path.append(selected_option)
            state = base64.b64encode(json.dumps({'choices': path}))
            with response.gather(numDigits=1, action='/{}'.format(state), method="POST") as g:
                g.say(_generate_script(selection), loop=3)
            return twiml(response)
    return _redirect_welcome()


# private methods

def _generate_script(tree):
    return ' '.join([
        'To reach {} press {}.'.format(branch.get('name', ''), number) for
        number, branch in enumerate(tree.get('options'))
    ])


def _get_tree():
    with open('/etc/phone-tree/phone-tree.yaml', 'r') as _file:
        return yaml.load(_file)


def _redirect_welcome():
    response = twilio.twiml.Response()
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect('/')
    return twiml(response)


def twiml(resp):
    resp = flask.Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp
