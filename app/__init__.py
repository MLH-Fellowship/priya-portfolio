import os
import datetime
from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from dotenv import load_dotenv
from peewee import *
from markdown import markdown
from playhouse.shortcuts import model_to_dict


load_dotenv()
app = Flask(__name__, template_folder="../templates", static_folder="../static")
app.jinja_env.filters['markdown'] = markdown


if os.getenv("TESTING") == "true":
    mydb = SqliteDatabase('file:memory?mode=memory&cache=shared', uri=True)
else:
    mydb = MySQLDatabase(
        os.getenv("MYSQL_DATABASE"),
        user=os.getenv("MYSQL_USER"),
        password=os.getenv("MYSQL_PASSWORD"),
        host=os.getenv("MYSQL_HOST"),
        port=3306
    )

print(mydb)

class TimelinePost(Model):
    name = CharField()
    email = CharField()
    content = TextField()
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = mydb

mydb.connect()
mydb.create_tables([TimelinePost])
mydb.commit()


NAMES = "Priya Hariharan"
URL = os.getenv("URL")

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title=NAMES, url=URL)


@app.route("/project")
def project():
    project_data = [
        {
            "id": 1,
            "title": "University of Washington Major Finder",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image_url": "https://1000logos.net/wp-content/uploads/2022/07/University-of-Washington-Logo.jpg",
            "website_url": "https://info340-groupab5.web.app/home"
        },
        {
            "id": 2,
            "title": "Analysis of Vogue Models",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image_url": "https://vogueprod.blob.core.windows.net/vogueoutput20080701thumbnails/Spreads/0x600/70.jpg",
            "website_url": "https://example.com/vogue"
        },
        {
            "id": 3,
            "title": "MindMeet",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image_url": "{{ url_for('static', filename='img/mindmeet.png') }}",
            "website_url": "https://example.com/mindmeet"
        },
        {
            "id": 4,
            "title": "Sustainify",
            "description": "Some quick example text to build on the card title and make up the bulk of the card's content.",
            "image_url": "{{ url_for('static', filename='img/sustainify.png') }}",
            "website_url": "https://example.com/sustainify"
        },
    ]
    return render_template("project.html", projects=project_data)

@app.route("/project-details/<int:project_id>")
def project_details(project_id):
    project_details = {
        1: {
            "title": "Design Process",
            "description": "After creating our idea, we made a prototype using Figma in order to visualize what our final product was going to look like. We wanted our color scheme to match the University of Washington colors, meaning there would be a lot of purple, gold, and white involved in the application. Our initial draft was only created on a phone screen as we felt this was most convenient for users, but our final website was adapted to fit all screens.",
            "image_urls": [
                "img/major1.png",
                "img/major2.png",
                "img/major3.png",
                "img/major3.png",
                "img/major4.png",
                "img/major5.png",
            ],
            "figma_urls" : [
                "img/figma6.png",
                "img/figma2.png",
                "img/figma3.png",
                "img/figma4.png",
                "img/figma5.png",
                "img/figma1.png",

            ],
            "fd_title": "First Draft:",
            "fd_description": "For the first draft of our website, we utilized BootStrap in order to have an even layout for all our pages. All the pages were static and we used cards to organize images and text. For the major page, I implemented two cards for each of the majors we were including as well as a search bar at the top with an optional filter feature. This was removed in the final draft as we decided to simplify our website so users could just search by major rather than alternative options.",
            "fd_urls" : [
                "img/major6.png",
                "img/major8.png",
                "img/major9.png",
                "img/major7.png",
            ],
            "code_title": "Coding Snippets:",
            "code_description": "The coding process involved using HTML, CSS, JavaScript, ReactJS, and Firebase. My responsibilities were to code a functional research bar in the major finding page as well as most of the components on the homepage. For the first task, I created a .json file that contained a list of the majors was then used in a List component to filter through the input in the search bar and compare it to the data to see if there was a match. For the homepage, I created the cards by downloading images and adding the appropriate descriptions before using the card classes through BootStrap as a means of organizing the content.",
            "github_description": "This link has all the code for the website: ",
            "code_link": "https://github.com/phariharan818/uw-major-finder",
            "website_url": "https://info340-groupab5.web.app/home",
            "code_urls" : [
                "img/majorcode1.png",
                "img/majorcode2.png",
                "img/majorcode3.png",
            ],
        },
        2: {
        "title": "Graphs",
        "description": "Our results show how models in the modeling industry can be exploited or denied based on their skin tone. The implications of this is that certain groups of people might find themselves more certain in their ability to succeed in this industry and some may not based on their skin color. However, the analysis we created is strictly looking at Vogue USA data, so it must be viewed from this viewpoint because the reality is that not everyone has the chance to become a Vogue model. People looking at our analysis have to keep this in mind in order to make decisions based on the results.\n\n These graphs show that there is a range of lightness values for models that had 1-3 covers, but after that the value is mostly higher. It's evident that there is a preference for a certain skin tone as indicated by the lightness values. The number doesn’t go down past 0.6 once a model hits five covers, which implies that the models that have the most covers have lighter skin. There is a point that has a very low lightness value but has been on the Vogue cover for 4 times, but it looks more like an outlier than an honest attempt for Vogue to include more darker skin models since there is still an accumulation of points with higher lightness value across the number of covers in Figure 2. Not only that, when considering the models that have 5 or more Vogue covers, the lightness value lies just in between 0.6 and 0.7, indicating that there is preference for that specific lightness value.",
        "image_urls": [
            "img/chart1.png",
            "img/chart2.png",
            "img/chart3.png",
            "img/chart4.png",
        ],
        "fd_title": "Research Questions:",
        "fd_description": "**Question 1: Is colorism present in the modeling industry? Does Vogue prefer lighter skin color models compared to darker skin-colored models on their magazine covers?**\n\n &ensp;&ensp;&ensp;-To some extent, we believe that colorism is still present in the modeling industry seeing as there is a trend for Vogue using lighter-skinned models.\n\n**Question 2: How has time changed the preference for skin color in the modeling industry? What is the preference for the skin color of the Vogue magazine models over time? When did this change begin happening?** \n\n &ensp;&ensp;-Our graph depicts more lighter-colored models being used overall, especially in the years 2004 and 2013.\n\n**Question 3: Is the modeling industry diverse, or do they just seem that way?**\n\n &ensp;&ensp;-Many organizations have issues with using diversity as a tool for their own success. If the modeling industry is the same way, that could give us a lot of insight into what their true motivations are and whether it is ethical or not. By knowing whether diversity is used instrumentally, we can see how people of color are impacted.",
        "code_title": "Coding Snippets:",
        "code_description": "To begin, we had to clean our data to ensure that both the datasets we were using could be merged so that a comparison could be made. Once this was done, we isolated the different values within the dataset, such as the lightness values and the number of covers. Another factor that went into our analysis was plotting by year and month, which meant we needed to create a separate method that held these values.",
        "github_description": "This link has all the code for the graphs: ",
        "code_link": "https://github.com/phariharan818/CSE163FinalProject",
        "website_url": "https://github.com/phariharan818/CSE163FinalProject",
        "code_urls" : [
            "img/vogue1.png",
            "img/vogue2.png",
            "img/vogue3.png",
            "img/vogue4.png",
        ],
        },
        3: { 
            "title": "Design Process",
            "description": "Our design process began with making user personas on Miro as well as storyboards that illustrated scenarios our users may find themselves in. With the user personas, we included a background that would give more context as to who the users of our application would be. This then allowed us to create storyboards that included specific features that we wanted in our app.",
            "image_urls": [
                "img/mm1.png",
                "img/mm2.png",
                "img/mm3.png",
                "img/mm4.png",
                "img/mm5.png",
                "img/mm6.png",
                "img/mm7.png",
                "img/mm8.png",
                "img/mm9.png",
                "img/mm10.png",
                "img/mm11.png",
                "img/mm12.png",
            ],
            "figma_urls" : [
                "img/persona1.png",
                "img/persona2.png",
                "img/persona3.png",
                "img/persona4.png",

            ],
            "fd_title": "User Flow Diagram:",
            "fd_description": "Once we had a basic idea of what we wanted to do, we created a user flow diagram that included all the key features that we wanted for both individuals seeking therapy as well as group therapists. This diagram also allowed us to make basic sketches of how we wanted our application to look like, which allowed us to then move forward in creating our low-fidelity prototype.",
            "fd_urls" : [
                "img/persona5.png",
                "img/persona6.png",                
            ],
            "code_title": "Low and Medium Fidelity Prototypes:",
            "code_description": "After these sketches and diagrams, we created the first versions of our application. For the low-fidelity prototype, we didn’t use our color scheme as we focused on creating basic features to see how it looked visually. Our main focus with these prototypes was to visualize the most important parts of the application, such as the group pairing process as well as the sessions recommendation system.",
            "github_description": "This link includes the whole prototype: ",
            "code_link": "https://www.figma.com/proto/F7yqMn6vOQFVpCBIqKKQXZ/360-Final-Copy?node-id=1-4259&page-id=0%3A1&scaling=min-zoom&starting-point-node-id=1%3A4259",
            "website_url": "https://www.figma.com/proto/F7yqMn6vOQFVpCBIqKKQXZ/360-Final-Copy?node-id=1-4259&page-id=0%3A1&scaling=min-zoom&starting-point-node-id=1%3A4259",
            "code_urls" : [
                "img/proto1.png",
                "img/proto2.png",
                "img/proto3.png",
            ],
        },
        4: {
            "title": "Design Process",
            "description": "Due to the 24 hour time constraint of this hackathon, we needed to create something that was feasible within the time limit. We created a visuals on Figma, including a color palette we wanted to implement as well as what our pages would potentially look like. Some of the ideas we got for our design came from templates we found on websites like SquareSpace as well as UI-UX websites we found online.",
            "image_urls": [
                "img/sustainify1.png",
                "img/sustainify2.png",
                "img/sustainify3.png",
                "img/sustainify4.png",
                "img/sustainify5.png",
                "img/sustainify6.png",
                
            ],
            "figma_urls" : [
                "img/design1.png",
                "img/design2.png",
                "img/design3.png",
                "img/design4.png",
            ],
            "fd_title": "Ideology:",
            "fd_description": "As mentioned before, this website was targeted towards college students and younger individuals in order to promote cost-effective methods of being sustainable. The most important feature of this website was the explore page, where users could filter through different plants based on price and click on individual plants to see their maintainability. This was implemented in order to help users pick plants based on their schedule as we felt that this small step in helping the environment was a bigger step towards solving the problem of climate change.",
            "fd_urls" : [
                "img/sustainify_vid.gif",
            ],
            "code_title": "Coding Snippets:",
            "code_description": "Using CSS, HTML, JavaScript, and ReactJS, I was able to format all the pages so they were visually appealing and had the effects that we wanted to implement. For the homepage, I used disappearing text with different hooks that added and then removed the animate class so that the visibility of the text components changed as you scroll. This effect was also applied to the recycle, transportation, and why me pages. For the functional search bar, we implemented this by parsing through a .json file regardless of the letter casing inputted. Finally, the filter feature was created by making an array in JavaScript, which was then passed through a function which was then used as a prop.",
            "github_description": "This link has all the code for the website: ",
            "code_link": "https://github.com/phariharan818/hackathon-1",
            "website_url": "https://sustainify.netlify.app/",
            "code_urls" : [
                "img/scode1.png",
                "img/scode2.png",
                "img/scode3.png",
                "img/scode4.png",
                "img/scode5.png",
                "img/scode6.png",
            ],
        },
    }

    project = project_details.get(project_id)

    if project:
        return render_template("project-details.html", project=project, project_id=project_id)
    else:
        return "Project not found", 404

@app.route("/map")
def map():
    return render_template("map.html", title=NAMES, url=URL)


@app.route("/work")
def work():
    return render_template("work.html", title=NAMES, url=URL)


@app.route("/hobbies")
def hobbies():
    return render_template("hobbies.html", title=NAMES, url=URL)

@app.route("/contact", methods=["GET"])
def show_contact_form():
    return render_template("contact.html", title="Contact Me")

# @app.route("/contact", methods=["POST"])
# def send_contact_message():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     message = request.form.get("message")

#     return "Message sent successfully!"

@app.route("/contact", methods=["POST"])
def send_contact_message():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        recipient_email = request.form.get("recipient_email")

        msg = EmailMessage()
        msg.set_content(f"From: {name}\nEmail: {email}\n\n{message}")
        msg["Subject"] = "Contact Form Submission"
        msg["From"] = os.getenv("EMAIL_ADDRESS")
        msg["To"] = recipient_email

        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()
                server.login(os.getenv("EMAIL_ADDRESS"), os.getenv("EMAIL_PASSWORD"))
                server.send_message(msg)
            return redirect(url_for("success"))
        except Exception as e:
            print("Error sending email:", e)
            return redirect(url_for("error"))

    return redirect(url_for("error"))


@app.route("/<path:path>")
def catch_all(path):
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.run(debug=True)
