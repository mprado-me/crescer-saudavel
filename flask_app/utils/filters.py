from flask_app import app

@app.template_filter('ignore_undefined')
def reverse_filter(data, path):
    for key in path.split('.'):
        if key in data:
            data = data[key]
        else:
            return ''
    return data