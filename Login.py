import requests
import json
import  random
head ={
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
DATA={
    'userName': '',
    'password': ''
}

Cookies = {
   'acw_tc':'',
   'auth':'',
   'token':''
}

FORM_DATA={
    'courseOpenId':'',
    'userId':'',
    'moduleId':'',
    'topicId':'',
    'cellId':'',
    'videoTimeTotalLong':'',
    'auvideoLength': '',
    'page':'',
    'workExamId':'',
    'workExamType':'1',
    'agreeHomeWork':'',
    'uniqueId':'',
    'questionId':'',
    'studentWorkId':'',
    'online':'1',
    'answer':'',
    'paperStructUnique':'',
    'useTime':'100'



}

MODULELIST=[]
TOPICLIST=[]
CELLLIST=[]
RESID=[]
class requests_url(object):
    def __init__(self):
        self.DATA = DATA

    def login(self,uName,pw):
        self.DATA['userName']=uName
        self.DATA['password']=pw

        login_txt= requests.post('http://mooc.icve.com.cn/portal/LoginMooc/loignZHZJByUserName',data=DATA,headers = head)
        login_token = json.loads(login_txt.text)['token']
        login_cookie = login_txt.cookies.values()
        FORM_DATA['userId']=json.loads(login_txt.text)['userId']

        cookie_token_json = login_txt.cookies.values()
        # print(cookie_token_json)
        Cookies['acw_tc'] = cookie_token_json[0]
        Cookies['auth'] = cookie_token_json[1]
        Cookies['token'] = json.loads(login_txt.text)['token']
        self.head = head
        return head
    def start(self,courseOpenId):
        FORM_DATA['courseOpenId'] = courseOpenId
        # print(FORM_DATA)
        getProcessList =requests.post('http://mooc.icve.com.cn/study/learn/getProcessList',data=FORM_DATA,cookies=Cookies,headers = head)
        for module in json.loads(getProcessList.text)['proces']['moduleList']:
            MODULELIST.append(module['id'])
        for module in MODULELIST:
            FORM_DATA['moduleId'] = module
            getTopicList = requests.post('http://mooc.icve.com.cn/study/learn/getTopicByModuleId',data=FORM_DATA,cookies = Cookies,headers = head)
            TOPICLIST = []
            for  topic in  json.loads(getTopicList.text)['topicList']:
                TOPICLIST.append(topic['id'])

            for topic in TOPICLIST:
                FORM_DATA['topicId']= topic
                getCell = requests.post('http://mooc.icve.com.cn/study/learn/getCellByTopicId',data=FORM_DATA,cookies = Cookies,headers = head)
                CELLLIST=[]
                for cell in json.loads(getCell.text)['cellList']:
                    #isStudyFinish
                    if cell['isStudyFinish'] == "True":
                        break
                    if cell['categoryName'] == '文档':
                        FORM_DATA['cellId'] = cell['Id']
                        FORM_DATA['videoTimeTotalLong'] = '0'
                        doc_isStudy = requests.post('http://mooc.icve.com.cn/study/learn/statStuProcessCellLogAndTimeLong',data=FORM_DATA,cookies = Cookies,headers = head)
                        print('doc:',doc_isStudy.text)

                    if  cell['categoryName'] =='ppt':
                        FORM_DATA['cellId']=cell['Id']
                        FORM_DATA['videoTimeTotalLong']= '0'
                        ppt_issucess = requests.post('http://mooc.icve.com.cn/study/learn/statStuProcessCellLogAndTimeLong',data=FORM_DATA,cookies = Cookies,headers = head)
                        print('ppt',json.loads(ppt_issucess.text)['isStudy'])

                    if cell['categoryName']=='视频':
                        FORM_DATA['cellId'] = cell['Id']
                        FORM_DATA['videoTimeTotalLong']=FORM_DATA['auvideoLength'] = random.randint(800,2000)
                        video_isStudy = requests.post('http://mooc.icve.com.cn/study/learn/statStuProcessCellLogAndTimeLong',data=FORM_DATA,cookies = Cookies,headers = head)
                        print('video:',json.loads(video_isStudy.text)['isStudy'])

                    if cell['categoryName']=='作业'or cell['categoryName']=='测验' :
                        FORM_DATA['workExamId'] = cell['resId']
                        FORM_DATA['workExamType'] = '0'
                        FORM_DATA['useTime']  = random.randint(100,300)
                        WorkExamData_uniqueId = requests.post('http://mooc.icve.com.cn/study/workExam/addStudentWorkExamRecord',data=FORM_DATA,cookies = Cookies,headers = head)
                        FORM_DATA['uniqueId'] =json.loads(WorkExamData_uniqueId.text)['uniqueId']

                        workExam = requests.post('http://mooc.icve.com.cn/study/workExam/workExamPreview',data=FORM_DATA, cookies=Cookies, headers=head)
                        for question in  json.loads(workExam.text)['paperData']['questions']:
                            FORM_DATA['questionId'] = question['questionId']
                            for ans in question['answerList']:
                                if ans['IsAnswer'] == 'True':
                                    FORM_DATA['answer'] = ans['SortOrder']
                                    online = requests.post('http://mooc.icve.com.cn/study/workExam/onlineHomeworkAnswer',data=FORM_DATA,cookies = Cookies,headers = head)
                                    # print(online.text)
                                    SaveDraft = requests.post('http://mooc.icve.com.cn/study/workExam/onlineWorkExamSaveDraft',data=FORM_DATA,cookies = Cookies,headers = head)
                                    # print(SaveDraft.text)
                            workExamSave = requests.post('http://mooc.icve.com.cn/study/workExam/workExamSave',data=FORM_DATA, cookies=Cookies, headers=head)
                            print('作业:',json.loads(workExamSave.text)['msg'])

                    for childNode in cell['childNodeList']:

                        if  childNode['categoryName'] =='ppt':
                            FORM_DATA['cellId']=childNode['Id']
                            FORM_DATA['videoTimeTotalLong']= '0'
                            ppt_issucess = requests.post('http://mooc.icve.com.cn/study/learn/statStuProcessCellLogAndTimeLong',data=FORM_DATA,cookies = Cookies,headers = head)
                            print('ppt',json.loads(ppt_issucess.text)['isStudy'])
                        if childNode['categoryName']=='视频':
                            FORM_DATA['cellId'] = childNode['Id']
                            FORM_DATA['videoTimeTotalLong']=FORM_DATA['auvideoLength'] = random.randint(800,2000)
                            video_isStudy = requests.post('http://mooc.icve.com.cn/study/learn/statStuProcessCellLogAndTimeLong',data=FORM_DATA,cookies = Cookies,headers = head)
                            print('video:',json.loads(video_isStudy.text)['isStudy'])

                        if childNode['categoryName'] == '测验':
                            FORM_DATA['workExamId']=childNode['resId']
                            FORM_DATA['agreeHomeWork'] = 'agree'
                            FORM_DATA['useTime'] = random.randint(100,300)
                            uniqueId = requests.post('http://mooc.icve.com.cn/study/workExam/addStudentWorkExamRecord',data=FORM_DATA,cookies = Cookies,headers = head)
                            FORM_DATA['uniqueId'] = json.loads(uniqueId.text)['uniqueId']
                            workExam = requests.post('http://mooc.icve.com.cn/study/workExam/workExamPreview',data=FORM_DATA,cookies = Cookies,headers = head)
                            for question in json.loads(workExam.text)['paperData']['questions']:
                                FORM_DATA['questionId']=question['questionId']
                                for ans in question['answerList']:
                                    if ans['IsAnswer'] == 'True':
                                        FORM_DATA['answer'] = ans['SortOrder']
                                        onlineHomeworkAnswer = requests.post('http://mooc.icve.com.cn/study/workExam/onlineHomeworkAnswer',data=FORM_DATA,cookies = Cookies,headers = head)
                                        # print(onlineHomeworkAnswer.text)
                                        SaveDraft = requests.post('http://mooc.icve.com.cn/study/workExam/onlineWorkExamSaveDraft',data=FORM_DATA,cookies = Cookies,headers = head)
                                        # print(SaveDraft.text)
                                workExamSave = requests.post('http://mooc.icve.com.cn/study/workExam/workExamSave',data=FORM_DATA,cookies = Cookies,headers = head)
                                print('测验:',json.loads(workExamSave.text)['msg'])
                        pass






requests_interface = requests_url()


