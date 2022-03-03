# 最简单的Hello World， 会给收到的每一条信息回复 Hello World

import werobot

robot = werobot.WeRoBot(token='token')

@robot.handler
def hello(message):
    return 'Hello World!'

# 让服务器监听在 0.0.0.0:80
robot.config['HOST'] = '0.0.0.0'
robot.config['PORT'] = 80
robot.run()