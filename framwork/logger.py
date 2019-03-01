import logging
import os.path
import time

class Logger(object):
    def __init__(self,logger):

        self.logger=logging.getLogger(logger) #创建一个logger
        self.logger.setLevel(logging.DEBUG)#设置最低的日志级别

        #创建一个Handler，用以写入日志信息
        rq=time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
        log_path=os.path.dirname(os.path.abspath("."))+"/logs/" #项目根目录下/Logs保存日志
        log_name=log_path+rq+".log"

        #定义俩种Handler
        fh=logging.FileHandler(log_name)#文件输出日志信息
        fh.setLevel(logging.INFO)
        ch=logging.StreamHandler()#控制台输出日志信息
        ch.setLevel(logging.INFO)

        #定义handler的输出格式
        formatter=logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)

        #给logger添加handler
        self.logger.addHandler(fh)
        self.logger.addHandler(ch)

    def getlog(self):
        return self.logger