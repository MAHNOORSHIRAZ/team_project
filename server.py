from flask_app import app
from flask_app.controllers import users #controllers go here

if __name__=="__main__":
    app.run(debug=True, host = "localHost", port = 5008)

# debug needs to be set to False when deployed.
# We shared a video showing how the information leaked by this feature and help hackers.
