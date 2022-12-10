from flask import Flask, render_template, request, session, url_for, redirect
import openai
import os

openai.organization = "org-3IYbWVJSBg74DJ3vPwBXCqqS"

"""
To use this application you will have to follow the steps below.

1. have followed the steps https://beta.openai.com/docs/api-reference/introduction
- git clone https://github.com/openai/openai-quickstart-node.git
- cd openai-quickstart-node
- cp .env.example .env
- copy YOUR secret key and set it as the OPENAI_API_KEY in the newly created .env file.
CAN CREATE SECRET KEY AT https://beta.openai.com/docs/quickstart/build-your-application
- python -m venv venv
- .venv/bin/activate   <- not required if does not work.
- pip install -r requirements.txt <- this will install the dependencies   <- IMPORTANT.


2. change 
"openai.api_key = os.getenv("OPENAI_API_KEY")"
to 
openai.api_key = "YOUR API KEY"

3. Ready to start type "flask run" in terminal.
"""
# openai.api_key = "YOUR API KEY"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")
app = Flask(__name__)

url = ""
# flask route  "/" with 2 https methods GET and POST
@app.route('/', methods=(["GET", "POST"]))
def index():
    # if request method from home page is post - user pressed submit button.
    if request.method == "POST":
        try:
            prompt = request.form["prompt"]

            # generate the response based on prompt
            response = openai.Image.create(
                prompt=f"{prompt}",
                n=1,
                size="512x512"
            )
            global url
            # trim response to show URL only
            image_url = response['data'][0]['url']

            url = image_url

            # redirect to /picture where image is shown on screen
            return render_template("index.html", image_url=url, prompt=prompt) #redirect(url_for("picture", image_url=image_url))
        except:
            return "error.html"

    # if no post just return home page
    return render_template("index.html", image_url=url)


@app.route('/picture', methods=(["GET", "POST"]))
def picture():
    # get image from post request
    img = request.args.get("image_url")

    # send image which is received in html body
    return render_template("picture.html", image_url=img)


# @app.route('/edit', methods=(["GET", "POST"]))
# def edit():
#     response = openai.Image.create_edit(
#         image=open("image_edit_original.png", "rb"),
#         mask=open("mask.png", "rb"),
#         prompt="add a wooden house",
#         n=1,
#         size="1024x1024"
#     )
#     image_url = response['data'][0]['url']
#     return image_url

if __name__ == '__main__':
    app.run()
