import flask
import twilio.twiml
import json
import base64
import yaml


app = flask.Flask(__name__)


@app.route('/', methods=['POST'])
@app.route('/<string:state_encoded>', methods=['POST'])
def gather(state_encoded=''):
    state = _decode_state(state_encoded)
    app.logger.debug('State: %s', str(state))
    path = state.get('choices', [])
    tree = _get_tree()
    app.logger.debug('Path: %s', str(path))

    app.logger.debug('Tree: %s', str(tree))
    # traverse tree based on state
    for choice in path:
        options = tree.get('options', [])
        if not isinstance(choice, int):
            continue
        if choice not in range(len(options)):
            return _redirect_to_start()
        tree = options[choice]
    app.logger.debug('Tree: %s', str(tree))

    # traverse tree based on user input
    user_input = _get_user_input()
    app.logger.debug('Input: %s', str(user_input))
    if user_input is not None:
        options = tree.get('options', [])
        if user_input not in range(len(options)):
            return _redirect_to_start()
        tree = options[user_input]
        path.append(user_input)
    app.logger.debug('Tree: %s', str(tree))

    # respond based on whether node is a leaf
    response = twilio.twiml.Response()
    if 'number' in tree:
        response.dial(tree.get('number'))
        return twiml(response)
    elif 'options' in tree:
        state = base64.b64encode(json.dumps({'choices': path}))
        with response.gather(numDigits=1, action='/{}'.format(state), method="POST") as g:
            g.say(_generate_script(tree), loop=3)
        return twiml(response)


# private methods
def _get_user_input():
    try:
        return int(flask.request.form.get('Digits'))
    except TypeError:
        pass
    return None


def _decode_state(state_encoded):
    if state_encoded:
        try:
            return json.loads(base64.b64decode(state_encoded))
        except (ValueError):
            pass
    return {'choices': []}


def _generate_script(tree):
    return ' '.join([
        'To reach {} press {}.'.format(branch.get('name', ''), number) for
        number, branch in enumerate(tree.get('options'))
    ])


def _get_tree():
    with open('/etc/phone-tree/phone-tree.yaml', 'r') as _file:
        return yaml.load(_file)


def _redirect_to_start():
    response = twilio.twiml.Response()
    response.say("Returning to the main menu", voice="alice", language="en-GB")
    response.redirect('/')
    return twiml(response)


def twiml(resp):
    resp = flask.Response(str(resp))
    resp.headers['Content-Type'] = 'text/xml'
    return resp
