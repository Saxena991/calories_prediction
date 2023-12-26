from flask import Flask
from flask import request,jsonify
from PIL import Image
import numpy as np
import io
import os
import cv2



app = Flask(__name__)

def color(img_file,B,G,R):

        # Load the image using OpenCV
        img = img_file

        # Iterate through each pixel of the image
        height, width, _ = img.shape
        for y in range(height):
            for x in range(width):
                pixel = img[y, x]
                red_component = pixel[2]

                if 10 <= red_component <= 255:
                        
                    img[y, x] = (B, G, R)  


        cv2.imwrite("printed.jpg", img)
           

@app.route('/',methods=["GET", "POST"])
def api():
    global result
    result = []

    if request.method == "POST":

            
            
        B = request.form.get("B")
        G = request.form.get("G")
        R = request.form.get("R")
        

        

    if request.method == "POST":

        file = request.files.get('image')
        print(file)
        if file is None or file.filename == "" or not file.filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            #return jsonify({"error": "no file"})
            json_error =  {'error':'no file or invalid image file'}
            result.append(json_error)

        else:
            image_bytes = file.read()
            pillow_image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
            image_path = np.asarray(pillow_image)
            image_path1 = cv2.cvtColor(image_path, cv2.COLOR_RGB2BGR)

            #main_functio(image_path1)
            color(image_path1,B,G,R)

            

    else:
        
        json_error =  {'error':'method not allowed'}
        result.append(json_error)

    
    return(jsonify(result))
            
    

if __name__=='__main__':
    app.run('0.0.0.0', port=8802)
