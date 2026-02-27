def test_root_redirects_to_static_index(client):
    # Arrange
    endpoint = "/"

    # Act
    response = client.get(endpoint, follow_redirects=False)

    # Assert
    assert response.status_code in {302, 307}
    assert response.headers["location"] == "/static/index.html"


def test_get_activities_returns_activity_map(client):
    # Arrange
    endpoint = "/activities"

    # Act
    response = client.get(endpoint)
    payload = response.json()
    sample_activity = payload["Chess Club"]

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "description" in sample_activity
    assert "schedule" in sample_activity
    assert "max_participants" in sample_activity
    assert "participants" in sample_activity
