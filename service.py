# Score.py file
# Must be included when deploying the model using the Azure ML CLIs
# Requires init and run functions to be defined.
# Run this file "python score.py" to generate a schema for the web service

def init():
    
    import os
    # os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    # os.environ["CUDA_VISIBLE_DEVICES"] = ""
    # os.environ["KERAS_BACKEND"] = "cntk"
    
    from keras.models import load_model
    # load the saved model file
    global model
    model = load_model('model.h5')

def run(doc_base64):
    categories = ['axes', 'boots', 'carabiners', 'crampons', 'gloves',
       'hardshell_jackets', 'harnesses', 'helmets', 'insulated_jackets',
       'pulleys', 'rope', 'tents']
    
    import base64
    import PIL as Image
    import numpy as np
    import json
    
    bts = base64.b64decode(doc_base64)
    with open("tst.jpg", "wb") as f:
        f.write(bts)
    
    im = Image.Image.open("tst.jpg")
    im = np.array(im)
    im = im.reshape((1,) + im.shape)
    
    pred = model.predict(im)
    
    
    # Return the result
    return json.dumps({"pred": "%d" % np.argmax(pred)})

def main():
    # Load the Azure ML libraries to generate a schema
    from azureml.api.schema.dataTypes import DataTypes
    from azureml.api.schema.sampleDefinition import SampleDefinition
    from azureml.api.realtime.services import generate_schema
    
    # Test the init and run functions using test data
    test_doc_text = "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"
    init()
    category = run(test_doc_text)
    print(category)

    # Generate the schema file (schema.json)
    inputs = {"doc_base64": SampleDefinition(DataTypes.STANDARD, test_doc_text)}
    generate_schema(run_func=run, inputs=inputs, filepath='./outputs/schema.json')

if __name__ == "__main__":
    main()