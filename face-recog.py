import face_recognition
from PIL import Image, ImageDraw, ImageFont
image_of_person = face_recognition.load_image_file('mark-zuckerberg-mwc-2015-internet-org-facebook.webp')
person_face_encoding = face_recognition.face_encodings(image_of_person)[0]

known_face_encodings = [person_face_encoding]
known_face_names = ["Rahul"]

test_image = face_recognition.load_image_file('Mark-Zuckerberg.jpg')

face_locations = face_recognition.face_locations(test_image)
face_encodings = face_recognition.face_encodings(test_image, face_locations)

pil_image = Image.fromarray(test_image)
draw = ImageDraw.Draw(pil_image)

for (t, r, b, l), face_encoding in zip(face_locations, face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
    name = "Unknown Person"
    print(matches)

    if True in matches:
        first_match_index = matches.index(True)
        name = known_face_names[first_match_index]
    print(name)
     
    '''draw.rectangle(((l, t), (r, b)), outline=(0, 255, 0))
    text_width, text_height = draw.textlength(name)
    draw.rectangle(((l, b - text_height - 90), (r, b)), fill=(0, 0, 0), outline=(0, 255, 0))
    draw.text((l+6, b-text_height-75), name, fill=(0, 255, 0))'''

del draw

pil_image.show()