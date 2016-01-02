
from datetime import datetime
import tornado.escape
import tornado.ioloop
import tornado.web

import __disease__
from disease import cardio

# test: http://localhost:8888/coronaryheartdiseaserisk/gender/1/age/60/dbp/150/smoker/1/tcl/100/hdl/50/diabetes/1

class GetCoronaryHeartDiseaseRisk(tornado.web.RequestHandler):
    def get(self,gender,age,dbp,smoker,tcl,hdl,diabetes):
        info = dict(
            gender=int(gender),age=int(age),dbp=int(dbp),smoker=int(smoker),
            tcl=int(tcl),hdl=int(hdl),diabetes=int(diabetes),
        )        
        response = { 
            'risk': cardio.anderson_chd(**info).predict(),
            'name': cardio.anderson_chd.name,
            'description': cardio.anderson_chd.description,
            'reference': cardio.anderson_chd.reference,
            'execution_date': datetime.now().isoformat()}
        self.write(response)
        
application = tornado.web.Application([
    (r"/coronaryheartdiseaserisk/gender/([0-1]+)/age/([0-9]+)/dbp/([0-9]+)/smoker/([0-9]+)/tcl/([0-9]+)/hdl/([0-9]+)/diabetes/([0-9]+)", GetCoronaryHeartDiseaseRisk),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()