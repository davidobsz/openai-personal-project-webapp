from flask import Flask, render_template, request, session, url_for, redirect
import openai
import os
openai.organization = "org-3IYbWVJSBg74DJ3vPwBXCqqS"
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.Model.retrieve("text-davinci-003")
app = Flask(__name__)


# curl https://api.openai.com/v1/completions -H "Content-Type: application/json" -H "Authorization: Bearer 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" -d '{"model": "text-davinci-003", "prompt": "Say this is a test", "temperature": 0, "max_tokens": 7}'

@app.route('/', methods=(["GET", "POST"]))
def index():

    # if request method from home page is post i.e user pressed submit button.
    if request.method == "POST":
        prompt = request.form["prompt"]

        # generate the response
        response = openai.Image.create(
            prompt=f"{prompt}",
            n=1,
            size="256x256"
        )

        # trim response to show URL only
        image_url = response['data'][0]['url']

        # redirect to /picture where image is shown on screen
        return redirect(url_for("picture", image_url=image_url))

    # if no post just return home page
    return render_template("index.html")



@app.route('/picture', methods=(["GET", "POST"]))
def picture():
    # get image
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
