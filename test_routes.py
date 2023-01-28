import pytest

# @pytest.mark.skip
def test_delete_one_favorite(client, favorites):
    #ACT
    response =  client.delete('/favorites/1')
    response_body = response.get_json

    #ASSERT
    assert response.status_code == 200
    assert 'message' in response_body
    assert response_body == { f'message': 'Favorites #1 was deleted.'}

@pytest.mark.skip
def test_delete_once_favorite_not_found(client):
    #ACT
    response =  client.delete('/favorites/222')
    response_body = response.get_json

    #ASSERT
    assert response.status_code == 404
    assert response_body == { f'message': 'Favorites #222 was not found.'}

@pytest.mark.skip
#def_test_create_account():
#ACT
#ASSERT
#assert response.status_code == 200

@pytest.mark.skip
#def_test_create_account_must_have_name():

@pytest.mark.skip
#def_test_create_account_must_have_email_addresse():

@pytest.mark.skip
def test_delete_account(client, one_account):
    #ACT
    response =  client.delete('/account/1')
    response_body = response.get_json

    #ASSERT
    assert response.status_code == 200
    assert 'message' in response_body
    assert response_body == { f'message': 'Account #1 was deleted.'}

@pytest.mark.skip
def test_delete_account_not_found(client):
    #ACT
    response =  client.delete('/account/32')
    response_body = response.get_json

    #ASSERT
    assert response.status_code == 404
    assert response_body == { f'message': 'Account #32 was not found.'}

# @pytest.mark.skip
# def test_read_all_favorites(client):

# @pytest.mark.skip
# def test_read_all_favorites(client):