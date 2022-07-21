from flask import Flask,render_template
import pandas as pd
app=Flask(__name__)
import sqlite3


def serialize_data(columns,data):
    data_list=[]
    for one_data in data:
        conv=zip(columns,one_data)
        data_list.append(dict(conv))
    return data_list

@app.route('/meter')
@app.route('/meter/<name>',)
def hello_world(name=None):
    if name is None:
        db=sqlite3.connect('sample_meter.db')
        data_from_db=db.execute("select * from meters")
        columns = [x[0] for x in data_from_db.description]
        data_json={"columns":columns,'data':data_from_db.fetchall()}
        return render_template('page_one.html',data=data_json)
    elif name is not None:
        db=sqlite3.connect('sample_meter.db')
        data_from_db=db.execute("select * from meter_data where meter_data.meter_id=?", [name])
        columns = [x[0] for x in data_from_db.description]
        data=data_from_db.fetchall()
        serial_data=serialize_data(columns,data)
        df=pd.DataFrame(serial_data)
        df.sort_values(by='timestamp',inplace=True)
        data_in_json=df.to_dict('records')
        data={"columns":columns,"data":data_in_json}
        return render_template('page_two.html',data=data)