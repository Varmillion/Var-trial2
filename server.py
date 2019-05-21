from flask import render_template
import connexion

# application/ web page instance
webApp = connexion.App(__name__,specification_dir = "./")

webApp.add_api('swagger.yaml')

@webApp.route('/')
def home():
	return render_template('wahjiwah.html')

if __name__ == '__main__':
    webApp.run(debug='true') 



    # host='0.0.0.0',port=5000, 