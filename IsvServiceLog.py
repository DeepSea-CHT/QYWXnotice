class IsvServiceLog:
    def __init__(self, data):
        self.id = data.get('id')
        self.errorStackTrace = data.get('errorStackTrace')
        self.serviceName = data.get('serviceName')
        self.errorTime = data.get('errorTime')
        self.errorClass = data.get('errorClass')
        self.errorMessage = data.get('errorMessage')
        self.traceId = data.get('traceId')
        self.pushFlag = data.get('pushFlag')
        self.qywxGroupName = data.get('qywxGroupName')
        self.applicationName = data.get('applicationName')
        self.errorCount = data.get('errorCount')
        self.type = data.get('type')
        self.title = data.get('title')
        self.message = data.get('message')


    def __error__(self):
        return f"服务告警信息\n" \
               f"服务名称:{self.serviceName}, \n" \
               f"集成应用名称:{self.applicationName}, \n" \
               f"errorTime:{self.errorTime}, \n" \
               f"errorClass:{self.errorClass}, \n" \
               f"errorCount:{self.errorCount}, \n" \
               f"errorMessage:{self.errorMessage}, \n" \
               f"errorStackTrace:{self.errorStackTrace}, \n" \
               f"traceId:{self.traceId}  \n" \
               f"请及时处理！查询日志地址: xxx"

    def __notice__(self):
        return f"通知信息\n" \
               f"title：{self.title}, \n" \
               f"message：" \
               f"{self.message} \n" \
               f"请关注通知信息！"