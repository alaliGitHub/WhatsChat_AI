from flask import Flask, redirect, url_for, request,  render_template

from TestOpenAI import Azure_ChatCompletion, Azure_PromptBuilder

app = Flask(__name__)


@app.route('/dialogue',methods = ['POST'])
def prompt():
   usermessage  = request.get_json()
   print("usermessage = ",usermessage)
   prompt = Azure_PromptBuilder(usermessage['message'])
   completion = Azure_ChatCompletion(prompt,usermessage['headers'])
   apimessageresponse  = {}
   apimessageresponse['answer'] = completion
   return apimessageresponse


@app.route('/')
def hello_world():
    return redirect(url_for('display_message',type = 'system'))

@app.route('/api/docs')
def get_docs():
    print('sending docs')
    return render_template('swaggerui.html')

@app.route('/message/<type>')
def display_message(type):
   if type == 'system':
      message = ' System error. Please contact your administrator'
   else:
      message = "Working in progress ..."
   
   return render_template('Message.html', display = message)


                         
if __name__ == '__main__':
   app.debug = True
   app.run()
   app.run(debug = True)