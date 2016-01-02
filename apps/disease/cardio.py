import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# helper methods:
class dict2class(object):
    def __init__(self, d):
        self.__dict__ = d

# Simple model for prediction of coronary heart disease (CHD)
# implemented based on
# Anderson KM et al, Cardiovascular disease risk profiles , 1991, American Heart Journal
# http://www.sciencedirect.com/\science/article/pii/000287039190861B
# note: tables 1 and 'Results, predicted probability'.
#
# inputs: gender, boolean, male = 1, female=0
#         age, float
#         dbp, float, diastolic blood pressure
#         smoker, smoker or quit within one year=1, otherwise 0.
#         tcl, total cholesterol (mg/dl)
#         hdl, high-density lipoprotein cholesterol (mg/dl)
#         diabetes, diabetes=1,otherwise 0.
#         ecg_lvh, ecg left ventricular hypertrophy, definite =1, otherwise 0.
# 
class anderson_chd():
    name = 'Coronary Heart Disease Risk'
    reference = 'Anderson KM et al, Cardiovascular disease risk profiles , 1991, American Heart Journal'
    description = '10-year predicted probability for cornonary heart disease.'
    
    def __init__(self,gender=1,age=30,dbp=80,
                 smoker=0,tcl=230,hdl=48,
                 diabetes=0,ecg_lvh=0):
                 
        b = dict2class(dict(theta_0=0.9145,
                      theta_1=-0.2784,
                      beta_0=15.5305,
                      female=28.4441,
                      log_age=-1.4792,
                      # log_age_sq=np.nan,
                      log_age_female=-14.4588,
                      log_age_sq_female=1.8515,
                      log_dbp=-0.9119,
                      cig=-0.2767,
                      log_tcl_hdl=-0.7181,
                      diab=-0.1759,
                      diab_female=-0.1999,
                      ecg_lvh=-0.5865,
                      ecg_lvh_male=np.nan))
                      
        if gender == 1:
            male = 1
            female = 0
        else:
            male = 0
            female = 1
            
        mu = b.beta_0+ \
             b.female*female + \
             b.log_age*np.log(age) + \
             b.log_age_female*np.log(age)*female + \
             b.log_age_sq_female*(np.log(age)**2)*female + \
             b.log_dbp*np.log(dbp) + \
             b.cig*smoker + \
             b.log_tcl_hdl*np.log(tcl/hdl) + \
             b.diab*diabetes +\
             b.diab_female*diabetes*female

        sig =np.exp(b.theta_0+b.theta_1*mu)
        u = (np.log(10)-mu)/sig
        self.prob = 1-np.exp(-np.exp(u))
    def predict(self):
        # todo: move calc of pob to method predict.
        return self.prob

def test_anderson_chd():
    info=dict(gender=0,age=55,dbp=135,smoker=1,
                     tcl=230,hdl=48,
                     diabetes=1,ecg_lvh=0)
    out = anderson_chd(**info).predict()  
    assert('%1.2f'%out == '0.22')
    print('10-year predicted probability for coronary heart disease: %1.2f' % out)
    
def gen_data(n=20):
    data = []
    info={}
    for age in np.arange(n):
        info['gender']=np.round(np.random.rand())
        info['age'] = 10+np.random.rand()*70
        info['dbp'] = 90+np.random.rand()*10
        info['smoker'] = 1
        smoker = anderson_chd(**info).predict()
        info['smoker'] = 0
        non_smoker = anderson_chd(**info).predict()
        data.append([info['age'],smoker,non_smoker])
    return np.array(data), ['smoker','non-smoker']
    
if __name__ == '__main__':
    test_anderson_chd()