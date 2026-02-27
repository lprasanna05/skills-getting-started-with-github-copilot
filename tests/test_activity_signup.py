def test_signup_for_activity_succeeds(client):
    # Arrange
    endpoint = "/activities/Chess Club/signup"
    email = "newstudent@mergington.edu"

    # Act
    response = client.post(endpoint, params={"email": email})
    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Signed up newstudent@mergington.edu for Chess Club"
    assert email in activities["Chess Club"]["participants"]


def test_signup_for_unknown_activity_returns_404(client):
    # Arrange
    endpoint = "/activities/Unknown Club/signup"
    email = "student@mergington.edu"

    # Act
    response = client.post(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_duplicate_signup_returns_400(client):
    # Arrange
    endpoint = "/activities/Chess Club/signup"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.post(endpoint, params={"email": existing_email})

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up for this activity"
