import boto3
import csv #to work with csv file
from PIL import Image,ImageDraw,ImageFont
import io

with open('object-Rekognition_accessKeys.csv','r') as file:
    next(file)#move to each row
    reader=csv.reader(file)

    for line in reader:
        access_key_id=line[0]
        secreat_acess_key=line[1]

client=boto3.client('rekognition', region_name='us-east-1',aws_access_key_id=access_key_id,aws_secret_access_key=secreat_acess_key)

photo='image2.jpg'

with  open(photo,'rb') as image_file:
    source_bytes=image_file.read()#read the image 


#detect_object is used to detect the object as a label in the image in json format
detect_objects=client.detect_labels(Image={'Bytes': source_bytes})
print(detect_objects)#provide json output all the info in the image

image=Image.open(io.BytesIO(source_bytes))
draw=ImageDraw.Draw(image)

for label in detect_objects['Labels']:
    print(label["Name"])#printing the name attributes of each label name attributes index
    print("Confidence is:",label["Confidence"])


    for instances in label['Instances']:
        if "BoundingBox" in instances:
            #taking coordinate to make boxes 
            box=instances["BoundingBox"]
            left=image.width*box['Left']
            top=image.width*box['Top']
            width=image.width*box['Width']
            height=image.width*box['Height']

        # coordinates_points=(
        #     (left,top),
        #     (left+width,top),
        #     (left+width,top+height),
        #     (left,top+height),
        #     (left,top)

        # )
        # draw.polygon(coordinates_points, outline="#eb3434", width=5)

        # draw.line(coordinates_points,width=5,fill="#eb3434")
        # shape=[{left-2,top-35},{width+2+left,top}]
        # draw.rectangle(shape,fill="#eb3434")

        rectangle = [
                (left, top),
                (left + width, top + height)
            ]
        draw.rectangle(rectangle, outline="#eb3434", width=1, fill=None)

        #for font use font=ImageFont.truetype("arial.ttf",30)
        draw.text((left+100,top-20),label['Name'],fill="#eb3434")   
        
image.show()
