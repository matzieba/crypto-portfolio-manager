from rest_framework import status


def test_user_me(db, auth_client, user):

    response = auth_client(user).get(
        f"/users/me",
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    assert response.data.get('id') == user.id
