from flask import Flask, render_template, request
import pymssql



conn = pymssql.connect("db-description", "username", "password", "db-name")
cursor = conn.cursor(as_dict=True)


#...

app = Flask(__name__ , template_folder='template')


#...
@app.route('/', methods=['post', 'get'])
def home():
    message = ''
    if request.method == 'POST':
        ID = request.form.get('ID')  # access the data inside 
        fullname = request.form.get('fullname')
        msg = request.form.get('msg')

        
        cursor.execute("INSERT INTO [dbo].[contact] (ID, fullname, msg) VALUES(%s, %s, %s)", (ID , fullname , msg))
        #vall=((login['ID'] ,login['fullname'] ,login['msg']))
        for row in cursor:
            print("SELECT TOP (1000) * FROM [dbo].[contact]")

        conn.commit()

    return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)
