import requests

# Replace with your API endpoint URL
base_url = 'http://127.0.0.1:5000/'

def test_add_person():
    url = f'{base_url}/insert'
    data = {
        'name': 'Mark Essien',
        'email': 'mark@example.com',
        'phone': '1234567890'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Person added successfully')
    else:
        print('Failed to add person')



def test_update_person():
    person_id = 7  # Replace with the ID of the person you want to update
    url = f'{base_url}/update'
    data = {
        'id': 3,
        'name': 'Updated Name',
        'email': 'updated@example.com',
        'phone': '9876543210'
    }

    response = requests.post(url, data=data)

    if response.status_code == 200:
        print('Person details updated successfully')
    else:
        print('Failed to update person details')

def test_delete_person():
    person_id = 5  # Replace with the ID of the person you want to delete
    url = f'{base_url}/delete/{person_id}'

    response = requests.get(url)

    if response.status_code == 200:
        print('Person deleted successfully')
    else:
        print('Failed to delete person')

if __name__ == '__main__':
    test_add_person()
    test_update_person()
    test_delete_person()
