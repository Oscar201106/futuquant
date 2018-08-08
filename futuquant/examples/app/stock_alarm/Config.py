class Config:
    def __init__(self):
        # wechat
        self.appid = ''       # AppID
        self.secrect = ''      # Secret

        # test_user_list
        self.test_user_list = {
                          'oaeaj02DzklyZHavotk2X3mt6JuA'  # test openid
                          }

        # test_user_nickname
        self.test_user_nickname = {'lpt'}

        # wechat token
        self.token = ''  # token

        # parameter: 越价率
        self.premium_rate = 0.005
        self.warning_threshold = 1000000
        self.large_threshold = 5000000
        self.warning_limit = 5

        # template_id
        self.template_id = ""

        # mysql
        self.host = '127.0.0.1'
        self.port = 3306
        self.user = 'root'
        self.passwd = ''
        self.database = 'stock_alarm'