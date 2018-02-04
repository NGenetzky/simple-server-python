from flask import Flask
app = Flask(__name__)

SYS_DEVICES_LEDS = '/sys/devices/platform/leds/leds/'


def led_brightness(name, value):
    path = '{0}/{1}/brightness'.format(SYS_DEVICES_LEDS, name)
    with open(path, 'w') as f:
        f.write(value)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/led/led0/<int:brightness>')
def led_led0(brightness):
    led_brightness('led0', brightness)
    return 'led0={0}'.format(brightness)


@app.route('/led/led1/<int:brightness>')
def led_led1(brightness):
    led_brightness('led1', brightness)
    return 'led1={0}'.format(brightness)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
