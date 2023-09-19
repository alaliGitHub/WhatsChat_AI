import os
import openai
import json
openai.api_type = os.getenv("OPENAI_API_TYPE")
#openai.api_version = os.getenv("OPENAI_API_VERSION") 
#openai.api_base =  os.getenv("OPENAI_API_BASE")
#openai.api_key = os.getenv("OPENAI_API_KEY")

      
# Global variale for prompt history
 #usermessage = [
    #       {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
    #      {"role": "user", "content": "Who were the founders of Microsoft?"}
    #]
   
prompt=[]
prompt.append( {"role": "system", "content": "Assistant is a large language model trained by OpenAI."})
    

def Azure_ChatCompletion(prompt,headers):
   
    print("*************** request to OpenAI ***************")
    
    openai.api_version = headers["OPENAI_API_VERSION"] 
    openai.api_base =   headers["OPENAI_API_BASE"] 
    openai.api_key =  headers["OPENAI_API_KEY"] 
    deployname = headers["OPENAI_DEPLOYMENT_NAME"]  #"gpt35-turbo-deployment"

    print("Opeanai type = ", openai.api_type)
    response = openai.ChatCompletion.create(
        engine= deployname, # The deployment name you chose when you deployed the GPT-35-Turbo or GPT-4 model.
        messages= prompt
    )
    print("************* response ***************")
    print(response)
    print("************* end of response ***************")
    
    prompt.append(response['choices'][0]['message'])
    
    message = response['choices'][0]['message']['content']
    print(message)
    return message


def Azure_PromptBuilder(usermessage):

   
    userdata = {}
    userdata['role'] = 'user'
    userdata['content'] = usermessage
    
    prompt.append(userdata)
    print("*********prompt BEGIN **** = ")
    print(prompt)
    print("*********prompt END **** = ")

    return prompt