def test_unregister_from_activity_succeeds(client):
    # Arrange
    endpoint = "/activities/Chess Club/signup"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.delete(endpoint, params={"email": existing_email})
    activities_response = client.get("/activities")
    activities = activities_response.json()

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == "Unregistered michael@mergington.edu from Chess Club"
    assert existing_email not in activities["Chess Club"]["participants"]


def test_unregister_for_unknown_activity_returns_404(client):
    # Arrange
    endpoint = "/activities/Unknown Club/signup"
    email = "student@mergington.edu"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_non_member_returns_404(client):
    # Arrange
    endpoint = "/activities/Chess Club/signup"
    email = "notregistered@mergington.edu"

    # Act
    response = client.delete(endpoint, params={"email": email})

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student is not registered for this activity"
