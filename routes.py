# Spencer Lommel
# Aug 26th, 2023
# Initialize routes for API

from flask import jsonify, request
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required, JWTManager


# ========== TEST ROUTES =============
def init_routes(app):
    @app.route('/test')
    def test():
        return jsonify(sucess="Connection received and API working")



    # Protect a route with jwt_required, which will kick out requests
    # without a valid JWT present.
    @app.route("/protected", methods=["GET"])
    @jwt_required()
    def protected():
        # Access the identity of the current user with get_jwt_identity
        current_user = get_jwt_identity()
        return jsonify(logged_in_as=current_user), 200

    # ========== LOGIN & REGISTER ROUTES =============

    @app.post('/login')
    def login():
        username = request.json.get("username", None)
        password = request.json.get("password", None)

        print(username, password)

        if username != "test" or password != "test":
            print("False")
            return jsonify({"msg": "Bad username or password"}), 401


        access_token = create_access_token(identity=username)
        print(f"Logged in {username}")
        return jsonify(token=access_token)

    @app.route('/register')
    def register():
        # DATA REQUIRED
            # Username
            # Email OR Phone Number
            # Password
            # Date of Birth

        pass


    # ========== ADD & CREATE ROUTES =============
    @app.route('/workouts/add', methods=['POST', 'GET'])
    @jwt_required()
    def add_workout():
        current_user = get_jwt_identity()
        # Use current_user to add workout data

        startDateTime = request.json.get("startDateTime")
        print(startDateTime)

    @app.route('/sets/add')
    @jwt_required()
    def add_set():
        current_user = get_jwt_identity()

        # use current_user to get the users current workout to add set to
        # Add set to work out using workout ID
        # Required info:
            # Workout ID (foreign key)
            # Workout Name
            # Reps
            # Weight

        return jsonify(sucess='workout added to database')


    # ========== READ ROUTES =============
    @app.route('/workouts/get')
    @jwt_required()
    def get_workouts():
        return jsonify(sucess='test')

    @app.route('/workouts/get_preview')
    def get_workout_previews():

        # Return
            # Name
            # Time
            # Date
        return jsonify(sucess='test')

