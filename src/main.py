import pickle
import os

# __dirname = os.path.dirname(os.path.abspath(__file__))

# model = pickle.load(open(os.path.join(__dirname, 'hateClassify.pkl'), 'rb'))
# vector = pickle.load(open(os.path.join(__dirname, 'vectorized.pkl', 'rb')))

def main(context):    

    return context.res.json(context.req)

    # text = context.req.params.get('text')

    # if text is None:
    #     context.response.send('Error: "text" query parameter is missing.', status_code=400)
    #     return
    

    # res = bool(model.predict(vector.transform([text]))[0]) 

    # context.re

    # return context.res.send("Hello, World!")

