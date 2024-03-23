from flask import Flask, render_template,url_for, request, redirect,session,flash,jsonify,send_from_directory
import traceback
from flask_pymongo import PyMongo
import bcrypt
import os
from PIL import Image, ImageFont, ImageDraw
import json
import csv

# database connection code
app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/TourismDatabase"
db = PyMongo(app).db
# database connection code en


@app.route('/signUp', methods=['GET','POST'])
def signUp():
    if request.method == 'POST':
        register = db.register
        existing_user = register.find_one({"email":request.form["email"]})
        password = request.form.get("password")
        c_password = request.form.get("cpassword")
        if existing_user is None:  
            if password == c_password:
                hashpass = bcrypt.hashpw(request.form["password"].encode("utf-8"), bcrypt.gensalt())
                db.register.insert_one({"name":request.form["name"],"email":request.form["email"], "password":hashpass,"confirm_pass":request.form["cpassword"]})
                session["email"] = request.form.get("email")
                return render_template('success.html') 
            else:
                flash("your password and confirm password does not matched !!!")
        else:
            return render_template('error.html')
    return render_template('signUp.html')


@app.route('/login', methods=['POST','GET'])
def login():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),login_user['password'])==login_user['password']:
            session["email"] = request.form.get("email")
            return render_template('index.html',user=login_user)
        else:
            return render_template('loginerror.html')
    else:
        flash("Enter email or username...")
    session.pop('email',None)
    return render_template('login.html')


@app.route('/submit', methods=['POST','GET'])
def submit(): 
    if request.method == "POST":
        name = request.form.get("personName")
        place = request.form.get("placeName")
        description = request.form.get("description")
        review = db.review
        db.review.insert_one({"name":request.form["personName"],"place":request.form["placeName"],"description":request.form["description"]})
        return render_template('aboutUs.html',name=name, place=place,description=description)
    
    return render_template("aboutUs.html")




@app.route("/daExp")
def daexplore():
    return render_template("daexplore.html")

@app.route("/juhuExp")
def juhuexplore():
    return render_template("juhuexplore.html")

@app.route("/mukteshwarExp")
def mukteshwarexplore():
    return render_template("mukteshwarexplore.html")

@app.route("/iskonExp")
def iskonexplore():
    return render_template("iskonexplore.html")

@app.route("/babulExp")
def babulhome():
    return render_template("babulhome.html")


@app.route("/ITparkExp")
def ITparkhome():
    return render_template("ITparkhome.html")

@app.route("/lokhandExp")
def lokhandwalaexplore():
    return render_template("lokhandwalaexplore.html")

@app.route("/cavesExp")
def caves():
    return render_template("caves.html")


@app.route("/warliExp")
def warlihome():
    return render_template("warlihome.html")

@app.route("/siddhiExp")
def siddhiexplore():
    return render_template("siddhi.html")

@app.route("/mahaExp")
def mahalaxmiexplore():
    return render_template("mahalaxmi.html")

@app.route("/maryExp")
def maryexplore():
    return render_template("mary.html")



@app.route("/lonawalaExp")
def lonawalahome():
    return render_template("lonawalahome.html")

@app.route("/pavanaExp")
def pavanaexplore():
    return render_template("pavana.html")

@app.route("/lohagadExp")
def lohagadexplore():
    return render_template("lohagad.html")

@app.route("/korigadExp")
def korigadexplore():
    return render_template("korigad.html")




@app.route("/jivdanimataExp")
def jivdanihome():
    return render_template("jivdanihome.html")

@app.route("/takmakExp")
def takmakexplore():
    return render_template("takmak.html")

@app.route("/rajodiExp")
def rajodiexplore():
    return render_template("rajodi.html")







@app.route("/kanheriExp")
def kanheriexplore():
    return render_template("kanheriexplore.html")

@app.route("/pagodaExp")
def pagodaexplore():
    return render_template("pagodaexplore.html")

@app.route("/elephantaExp")
def elephantaexplore():
    return render_template("elephantaexplore.html")


@app.route("/tajExpp")
def tajhome():
    return render_template("tajhome.html")

@app.route("/juhuExpp")
def juhuhome():
    return render_template("juhuhome.html")




@app.route("/national")
def nationalhome():
    return render_template("nationalhome.html")

@app.route("/iskon")
def iskonhome():
    return render_template("iskonhome.html")

@app.route("/gateway")
def gateway():
    return render_template("gateway.html")

@app.route("/csmtExp")
def explore():
    return render_template("csmtexplore.html")

@app.route("/tajExp")
def tajexplore():
    return render_template("tajexp.html")

@app.route("/marinExp")
def marineexplore():
    return render_template("marineexp.html")


# seeall wale links
@app.route("/hangingExp")
def hangingexplore():
    return render_template("hangingexplore.html")




@app.route("/kokanExp")
def kokanexplore():
    return render_template("kokanplaces.html")

@app.route("/sinExp")
def sindhudurgexplore():
    return render_template("sindhudurgplaces.html")

@app.route("/ratExp")
def ratnagiriexplore():
    return render_template("ratnagiriplaces.html")

@app.route("/palgharExp")
def palgharexplore():
    return render_template("palgharplaces.html")

@app.route("/tajExp")
def tajjexplore():
    return render_template("tajplaces.html")

@app.route("/thaneExp")
def thaneexplore():
    return render_template("thaneplaces.html")

@app.route("/raigadExp")
def raigadexplore():
    return render_template("raigadplaces.html")



@app.route("/westernmaharashtraExp")
def westmahaexplore():
    return render_template("WesternMaharashtra.html")

@app.route("/puneExp")
def puneexplore():
    return render_template("puneplaces.html")

@app.route("/sataraExp")
def sataraexplore():
    return render_template("sataraplaces.html")

@app.route("/sangliExp")
def sangliexplore():
    return render_template("sangliplaces.html")

@app.route("/kolhapurExp")
def kolhapurexplore():
    return render_template("kolhapurplaces.html")

@app.route("/solapurExp")
def solapurexplore():
    return render_template("solapurplaces.html")




@app.route("/vidarbhaExp")
def vidarbhaexplore():
    return render_template("vidarbhaplaces.html")

@app.route("/nagpurExp")
def nagpurexplore():
    return render_template("nagpurplaces.html")

@app.route("/chandrapurExp")
def chandrapurexplore():
    return render_template("chandrapurplaces.html")

@app.route("/gadchiroliExp")
def gadchiroliexplore():
    return render_template("gadchiroliplaces.html")

@app.route("/gondiaExp")
def gondiaexplore():
    return render_template("gondiaplaces.html")

@app.route("/wardhaExp")
def wardhaexplore():
    return render_template("wardhaplaces.html")



@app.route("/northmaharashtraExp")
def northmaharashtraexplore():
    return render_template("northmaharashtra.html")

@app.route("/dhuleExp")
def dhuleexplore():
    return render_template("dhuleplaces.html")

@app.route("/jalgaonExp")
def jalgaonexplore():
    return render_template("jalgaonplaces.html")

@app.route("/nashikExp")
def nashikexplore():
    return render_template("nashikplaces.html")

@app.route("/nandurbarExp")
def nandurbarexplore():
    return render_template("nandurbarplaces.html")



@app.route("/marathwadaExp")
def marathwadaexplore():
    return render_template("marathwadaplaces.html")

@app.route("/aurangabadExp")
def aurangabadexplore():
    return render_template("aurangabadplaces.html")

@app.route("/laturExp")
def laturexplore():
    return render_template("laturplaces.html")

@app.route("/beedExp")
def beedexplore():
    return render_template("beedplaces.html")

@app.route("/hingoliExp")
def hingoliexplore():
    return render_template("hingoliplaces.html")

@app.route("/wardhaExp")
def nandedexplore():
    return render_template("nandedplaces.html")



@app.route("/vidarbha2Exp")
def vidarbha2explore():
    return render_template("vidarbha2places.html")

@app.route("/amravatiExp")
def amravatiexplore():
    return render_template("amravatiplaces.html")

@app.route("/yawatmalExp")
def yawatmalexplore():
    return render_template("yawatmalplaces.html")

@app.route("/washimExp")
def washimexplore():
    return render_template("washimplaces.html")


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/destination")
def destination():
    return render_template("destination.html")

@app.route("/experience")
def experience():
    return render_template("experience.html")



@app.route("/submitbtn")
def submitbtn():
    return render_template("submit.html")

@app.route("/logout")
def logout():
    return render_template("index.html")


@app.route("/seeAll")
def seeAll():
    return render_template("seeAll.html")


@app.route("/aboutUs")
def aboutUs():
    return render_template("aboutUs.html")

@app.route("/privacy")
def privacy():
    return render_template("privacypolicy.html")


@app.route("/forgot" , methods=["POST", "GET"])
def forgot():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})
    new_password = request.form.get("new password")
    confirm_password = request.form.get("confirm password")
    if request.method == "POST":
        if login_user:
            forgot = db.forgot
            if new_password == confirm_password:
                db.forgot.insert_one({"new password":request.form["new password"],"confirm password":request.form["confirm password"]})
                return render_template('forgotSuccess.html')
    
    return render_template("forgotpwd.html")



@app.route("/cancel", methods=["POST", "GET"])
def cancellation():
    register = db.register
    bookings = db.bookings
    email = request.form.get("email")
    session["email"] = email
    login_user = register.find_one({"email": request.form.get("email")})
    book_data = bookings.find_one({"email": session.get('email')})
    if request.method == "POST":
        if login_user:
            cancel = db.cancel
            db.cancel.insert_one({"Name":request.form["fullname"],"Email":request.form["email"],"contact":request.form["phone"],
            "country":"India","city":request.form["city"],"status":"cancelled"})
            session["email"] = request.form.get("email")
            return render_template('cancelsuccess.html')
        else:
            flash("Enter correct email...")
    return render_template("cancellation.html", user_book_data = book_data)


@app.route("/booking", methods=["POST", "GET"])
def bookings():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})
    if request.method == "POST":
        if login_user:
            bookings = db.bookings
            db.bookings.insert_one({"Name":request.form["fullname"],"Email":request.form["email"],"contact":request.form["phone"],
            "adult":request.form["adult"],"child":request.form["child"],"infant":request.form["infant"],"checkin":request.form["checkin"],
            "checkout":request.form["checkout"],"destination":request.form["select"],"country":"India","state":"Maharshtra","city":request.form["select_city"],
            "status":"booked","hotel":request.form["data"]})
            session["email"] = request.form.get("email")
            return render_template('Payment.html')
        else:
            flash("you entered wrong email, Error !!!")
    return render_template("bookingform.html")


@app.route("/train_booking", methods=["POST", "GET"])
def train_bookings():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})
    if request.method == "POST":
        if login_user:
            train_bookings = db.train_bookings
            db.train_bookings.insert_one({
            "Date":request.form["date"],"destination":request.form["select_to"],
            "from":request.form["select_from"],"data":request.form["data"],"email":request.form["email"]})
            session["email"] = request.form.get("email")
            return render_template('Payment.html')
        else:
            flash("you entered wrong email, Error !!!")
    return render_template("trans_lear_more.html")


@app.route("/bus_booking", methods=["POST", "GET"])
def bus_bookings():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})
    if request.method == "POST":
        if login_user:
            bus_bookings = db.bus_bookings
            db.bus_bookings.insert_one({
            "Date":request.form["date"],"destination":request.form["select_to"],
            "from":request.form["select_from"],"data":request.form["data"],"email":request.form["email"]})
            session["email"] = request.form.get("email")
            return render_template('Payment.html')
        else:
            flash("you entered wrong email, Error !!!")
    return render_template("road_trip_lear_more.html")




@app.route("/contactUs", methods=["POST", "GET"])
def contactUs():
    register = db.register
    login_user = register.find_one({"email": request.form.get("email")})
    if request.method == "POST":
        contacts = db.contacts
        db.contacts.insert_one({"Name":request.form["name"],"Email":request.form["email"],"contact":request.form["phone"]})
        session["email"] = request.form.get("email")
        return render_template('contactsuccess.html')
    return render_template("contactUs.html",user=login_user)


@app.route("/Destinations")
def Destinations():
    return render_template("Destinations.html")


@app.route("/Gallery")
def Gallery():
    return render_template("Gallery.html")


@app.route("/spring")
def spring():
    return render_template("spring.html")


@app.route("/summer")
def summer():
    return render_template("summer.html")

@app.route("/winter")
def winter():
    return render_template("winter.html")


@app.route("/autumn")
def autumn():
    return render_template("autumn.html")


@app.route("/learn_more")
def learn_more():
    return render_template("learn_more.html")


@app.route("/trans_learn_more")
def trans_learn_more():
    return render_template("trans_lear_more.html")


@app.route("/road_trip_learn_more")
def road_trip_learn_more():
    return render_template("road_trip_lear_more.html")


@app.route("/mumbai_best_learn_more")
def mumbai_best_learn_more():
    return render_template("mumbai_best_lear_more.html")


@app.route("/gift", methods=['POST','GET'])
def gift():
    if request.method == "POST":
        gifts = db.gifts
        db.gifts.insert_one({"from_name":request.form["from_name"],"to_name":request.form["to_name"],"gift_name":request.form["gift_name"]
        ,"Email":request.form["email"],"contact":request.form["phone"]})
        return render_template('giftsuccess.html')
    
    return render_template("gift_voucher.html")


@app.route("/Payment" , methods=['POST','GET'])
def Payment():
    if request.method == "POST": 
        register = db.register
        login_user = register.find_one({"email": request.form.get("email")})
        if login_user:
            payments = db.payment
            db.payments.insert_one({"card holder name":request.form["name"],"card Number":request.form["number"],"email":request.form["email"],
            "year":request.form["year"],"cvv":request.form["cvv"]})
            return render_template('paysuccess.html')
        else:
            return render_template("error.html")
    
    return render_template("Payment.html")

# @app.route('/upload', methods=['POST'])
# def upload_file():
#     if 'file' not in request.files:
#         return redirect(request.url)

#     file = request.files['file']

#     if file.filename == '':
#         return redirect(request.url)

#     if file:
#         # Save the uploaded file
#         uploaded_filepath = os.path.join('C:/Users/91937/OneDrive/Pictures', file.filename)
#         file.save(uploaded_filepath)

#         # Apply watermark
#         result_path = apply_watermark(uploaded_filepath)

#         return render_template('Gallery.html', result_image = result_path)

# def apply_watermark(image_path):
#     im = Image.open(image_path)
#     width, height = im.size
#     drawing = ImageDraw.Draw(im)

#     font = ImageFont.truetype("arial.ttf", 50)
#     fill_color = (203, 201, 201)
#     watermark_text = "tourism.com"
#     x = width / 2 - 50
#     y = height / 2 - 50
#     position = (x, y)
#     drawing.text(xy=position, text=watermark_text, font=font, fill=fill_color)
#     result_path = os.path.join('C:/Users/91937/OneDrive/Pictures','watermark_' + os.path.basename(image_path))
#     im.save(result_path)
#     return result_path




@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'})

    file = request.files['file']

    if file.filename == '':
        return jsonify({'error': 'No file selected'})

    if file:
        uploads_folder = os.path.join(app.root_path, 'uploads')
        # os.makedirs(uploads_folder, exist_ok=True)

        uploaded_filepath = os.path.join(uploads_folder, file.filename)
        file.save(uploaded_filepath)

        result_path = apply_watermark(uploaded_filepath)
        result_filename = os.path.basename(result_path)

        return jsonify({'result_image': f'/uploads/{result_filename}'})



# @app.route('/api/search', methods=['GET'])
# def search():
#     query = request.args.get('query')
#     # Perform any necessary processing with the query
#     # For example, you could log the query
#     print(f'Search query: {query}')
#     with open('andheri.txt', 'r', newline='') as file:
#         # Create a CSV reader object
#         csv_reader = csv.reader(file)

#         # Skip the header
#         next(csv_reader)

#         # Create a list to store the data
#         data = []

#         # Iterate over each row in the CSV file
        # for row in csv_reader:
        #     # Extract the values
        #     source_address = row[0]
        #     destination_address = row[1]
        #     temperature = row[2]
        #     weather = row[3]
        #     food = row[4]
        #     clothes = row[5]
        #     transportation = row[6]
        #     imglink = row[7]

        #     # Create a dictionary for each row of data
        #     row_data = {
        #         'source_address': source_address,
        #         'destination_address': destination_address,
        #         'temperature': temperature,
        #         'weather': weather,
        #         'food': food,
        #         'clothes': clothes,
        #         'transportation': transportation,
        #         'imglink': imglink
        #     }

        #     # Append the row data to the list
        #     data.append(row_data)

#     # Return the data as JSON
#     return json.dumps(data)




@app.route('/api/search', methods=['GET'])
def search():
    query = request.args.get('query')
    # Convert the query to lowercase
    query = query.lower()
    # Perform any necessary processing with the query
    # For example, you could log the query
    print(f'Search query: {query}')
    
    # Construct the file path based on the lowercase query
    file_path = f'{query}.txt'
    
    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, 'r', newline='') as file:
            # Create a CSV reader object
            csv_reader = csv.reader(file)

            # Skip the header
            next(csv_reader)

            # Create a list to store the data
            data = []

            # Iterate over each row in the CSV file
            for row in csv_reader:
                # Check if the row has at least 8 elements
                if len(row) >= 8:
                    # Extract the values
                    source_address = row[0]
                    destination_address = row[1]
                    temperature = row[2]
                    weather = row[3]
                    food = row[4]
                    clothes = row[5]
                    transportation = row[6]
                    imglink = row[7]

                    # Create a dictionary for each row of data
                    row_data = {
                        'source_address': source_address,
                        'destination_address': destination_address,
                        'temperature': temperature,
                        'weather': weather,
                        'food': food,
                        'clothes': clothes,
                        'transportation': transportation,
                        'imglink': imglink
                    }

                    # Append the row data to the list
                    data.append(row_data)
                else:
                    print(f'Row does not have enough elements: {row}')

        # Return the data as JSON
        return json.dumps(data)
    else:
        return 'File not found'









@app.route('/uploads/<filename>')
def get_uploaded_file(filename):
    try:
        return send_from_directory('uploads', filename)
    except Exception as e:
        traceback.print_exc()  # Print the traceback to the console
        return jsonify({'error': 'Internal Server Error'}), 500

def apply_watermark(image_path):
    im = Image.open(image_path)
    width, height = im.size
    drawing = ImageDraw.Draw(im)

    font = ImageFont.truetype("arial.ttf", 50)
    fill_color = (255, 255, 255)
    watermark_text = "Dzire Tourism.com"
    x = width/2-120
    y = height/2-100
    position = (x, y)
    drawing.text(xy=position, text=watermark_text, font=font, fill=fill_color,fontWeight = 500)

    result_path = os.path.join(app.root_path, 'uploads', 'watermark_' + os.path.basename(image_path))
    im.save(result_path)
    return result_path

if __name__ == '__main__':
    app.secret_key = 'secretivekeyagain'
app.run(debug=True, port=5001)


