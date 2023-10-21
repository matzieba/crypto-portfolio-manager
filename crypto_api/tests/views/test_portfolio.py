from rest_framework import status


def test_get_my_portfolio(db, auth_client, user, portfolio):

    response = auth_client(user).get(
        f"/portfolio/",
        format="json",
    )

    assert response.status_code == status.HTTP_200_OK
    for portfolio in response.data:
        assert portfolio['user'] == user.pk
