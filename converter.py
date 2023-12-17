from flask import Flask, request

app = Flask(__name__)

@app.route('/convert', methods=['POST'])
def convert_xlsx_to_json():
    if 'file' not in request.files:
        return 'No file part', 400
    
    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400
    
    if file and file.filename.endswith('.xlsx'):
        import pandas as pd
        # data = pd.read_excel(file)
        # new_data=data.drop(data.index[1],axis=0)
        # new_data.reset_index(drop=True, inplace=True)
        # new_data.columns = new_data.iloc[0]
        # new_data = new_data[1:]
        result = (
            data.groupby('Class')
            .apply(lambda x: x.groupby('Section')
                .apply(lambda y: y.set_index('Admission Number')
                    .drop(['Class', 'Section'], axis=1)
                    .to_dict(orient='index'))
                .to_dict())
            .to_json()
        )
        
        return result, 200
    
    return 'Invalid file format. Please provide an XLSX file.', 400

if __name__ == '__main__':
    app.run(debug=True)