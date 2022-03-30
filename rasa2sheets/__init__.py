import pandas as pd
import os.path
import yaml

    
def export(file):
    # intent
        if file == 'intent' or file == 'intents':
            with open('data/nlu/nlu.yml') as file:
                file = yaml.load(file, Loader=yaml.FullLoader)
                myvar = pd.DataFrame(index=[i['intent'] for i in file['nlu']],columns=["example_{}".format(x) for x in range(10)])       


                for doc in file['nlu']:
                    count=0
                    for i in doc['examples'].split("\n"):
                        myvar.at[doc['intent'],"example_{}".format(count)]=i
                        count+=1

            myvar.to_csv('spreadsheets/intents.csv', encoding='utf-8')

        ######################################## FAQ
        elif file == 'faq':
            with open('data/nlu/faq.yml') as file:
                file = yaml.load(file, Loader=yaml.FullLoader)
                myvar = pd.DataFrame(index=[i['intent'] for i in file['nlu']], columns=["example_{}".format(x) for x in range(10)])

                for doc in file['nlu']:
                    count = 0
                    for i in doc['examples'].split("\n"):
                        myvar.at[doc['intent'],"example_{}".format(count)]=i
                        count+=1
                myvar.to_csv('spreadsheets/faq.csv', encoding='utf-8')

            with open('data/responses.yml') as file:
                with open('data/responses.yml') as file:
                    file = yaml.load(file, Loader=yaml.FullLoader)
                    myvar = pd.DataFrame(index=[x for x in file['responses'].keys() if len(x.split('/'))>1],columns=["response_{}".format(x) for x in range(10)])

                for x,y in file['responses'].items():

                    if len(x.split('/'))>1:
                        count=0
                        for i in y:
                            myvar.at[x,"response_{}".format(count)]=list(i.values())[0]
                            count+=1
                
                

                myvar.to_csv('spreadsheets/faq_responses.csv', encoding='utf-8')

        ############################# FORMS
        elif file == 'form' or file == 'forms':
            with open('domain.yml') as file:
                file = yaml.load(file, Loader=yaml.FullLoader)

                myvar = pd.DataFrame(index=file['forms'].keys(),columns=["slot_{}".format(x) for x in range(10)])

                for x,y in file['forms'].items():
                    for i in y.values():
                        count=0
                        for j in i:
                            myvar.at[x,"slot_{}".format(count)]=j
                            count+=1

            myvar.to_csv('spreadsheets/forms.csv', encoding='utf-8')

        ########################### RESPONSES
        elif file == 'response' or file == 'responses':
            with open('data/responses.yml') as file:
                file = yaml.load(file, Loader=yaml.FullLoader)

            myvar1 = pd.DataFrame(index=[x for x in file['responses'].keys() if len(x.split('/'))<2],columns=["response_{}".format(x) for x in range(10)])
        
            for x,y in file['responses'].items():

                if len(x.split('/'))<2:
                    count=0
                    for i in y:
                        myvar1.at[x,"response_{}".format(count)]=list(i.values())[0]
                        count+=1
            
            myvar2 = pd.DataFrame(index=[x for x in file['responses'].keys() if len(x.split('/'))>1],columns=["response_{}".format(x) for x in range(10)])
        
            for x,y in file['responses'].items():

                if len(x.split('/'))>1:
                    count=0
                    for i in y:
                        myvar2.at[x,"response_{}".format(count)]=list(i.values())[0]
                        count+=1
                    
                    
        
        myvar1.to_csv('spreadsheets/responses.csv', encoding='utf-8')
        myvar2.to_csv('spreadsheets/faq_responses.csv', encoding='utf-8')


def insert(file):

        # intent
        if file == 'intent' or file == 'intents':
            with open('data/nlu/nlu.yml') as f:
                intent_yml = yaml.load(f, Loader=yaml.FullLoader)
            df = pd.read_csv('spreadsheets/intents.csv')
            files=[]
            for index, row in df.iterrows():
                obj={
                    'intent':'',
                    'examples':[]       
                }
                for i in range(len(df.columns)-1):
                    if pd.isna(row[i])==False:
                        if i==0:
                            obj['intent']=row[i]
                        else:
                            obj['examples'].append(row[i])
                files.append(obj)

            intent_yml['nlu'] = files
            with open('data/nlu/nlu.yml', 'w') as fintent:
                yaml.dump(intent_yml, fintent, default_flow_style=False)


        # faq                 
        elif file == 'faq':
            with open('data/nlu/faq.yml') as f:
                faq_yml = yaml.load(f, Loader=yaml.FullLoader)

            df = pd.read_csv('spreadsheets/faq.csv')
            files=[]
            for index, row in df.iterrows():
                obj={
                    'intent':'',
                    'examples':[]       
                }
                for i in range(len(df.columns)-1):
                    if pd.isna(row[i])==False:
                        if i==0:
                            obj['intent']=row[i]
                        else:
                            obj['examples'].append(row[i])
                files.append(obj)

            faq_yml['nlu'] = files

            with open('data/nlu/faq.yml', 'w') as fintent:
                yaml.dump(faq_yml, fintent, default_flow_style=False)
            
            with open('data/responses.yml') as f:
                responses_yml = yaml.load(f, Loader=yaml.FullLoader)


            df_responses = pd.read_csv('spreadsheets/responses.csv')

            obj={}
            for index, row in df_responses.iterrows():
                slots=[]
                for i in range(len(df_responses.columns)-1):
                    if pd.isna(row[i])==False and i!=0:
                        slots.append({'text':row[i]})
                            
                obj[row[0]]=slots

        
            df_responses = pd.read_csv('spreadsheets/faq_responses.csv')

            for index, row in df_responses.iterrows():
                slots=[]
                for i in range(len(df_responses.columns)-1):
                    if pd.isna(row[i])==False and i!=0:
                        slots.append({'text':row[i]})
                            
                obj[row[0]]=slots
            responses_yml['responses'] = obj
            with open('fresponse.yml', 'w') as fintent:
                yaml.dump(responses_yml, fintent, default_flow_style=False)



        # form
        elif file == 'form' or file == 'forms':

            with open('domain.yml') as f:
                form_yml = yaml.load(f, Loader=yaml.FullLoader)

            df_forms = pd.read_csv("spreadsheets/forms.csv")
            obj={}
            for index, row in df_forms.iterrows():
                slots=[]
                for i in range(len(df_forms.columns)-1):
                    if pd.isna(row[i])==False:
                        if i==0:
                            pass
                        else:
                            slots.append(row[i])
                            
                obj[row[0]]={'required_slots':slots}
            
            form_yml['form'] = obj
            with open('domain.yml', 'w') as fintent:
                yaml.dump(form_yml, fintent, default_flow_style=False)

        elif file == 'domain':
            return 'domain'
        elif file == 'entities' or file == 'entitie':
            return ' entities'
        
        # response
        elif file == 'response' or file == 'responses':
            with open('data/responses.yml') as f:
                responses_yml = yaml.load(f, Loader=yaml.FullLoader)
            df_responses = pd.read_csv('spreadsheets/responses.csv')

            obj={}
            for index, row in df_responses.iterrows():
                slots=[]
                for i in range(len(df_responses.columns)-1):
                    if pd.isna(row[i])==False:
                        if i==0:
                            pass
                        else:
                            slots.append({'text':row[i]})
                            
                obj[row[0]]=slots

            if os.path.exists('spreadsheets/faq_responses.csv'):
                df_responses = pd.read_csv('spreadsheets/faq_responses.csv')

                for index, row in df_responses.iterrows():
                    slots=[]
                    for i in range(len(df_responses.columns)-1):
                        if pd.isna(row[i])==False:
                            if i==0:
                                pass
                            else:
                                slots.append({'text':row[i]})
                            
                obj[row[0]]=slots

            responses_yml['responses'] = obj
            with open('test_response.yml', 'w') as fintent:
                yaml.dump(responses_yml, fintent, default_flow_style=False)