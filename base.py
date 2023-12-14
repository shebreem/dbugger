import requests

def ip_to_location(ip):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip}')
        response.raise_for_status()
    except requests.exceptions.HTTPError as errh:
        return f'HTTP Error: {errh}'
    except requests.exceptions.ConnectionError as errc:
        return f'Error Connecting: {errc}'
    except requests.exceptions.Timeout as errt:
        return f'Timeout Error: {errt}'
    except requests.exceptions.RequestException as err:
        return f'Oops: Something Else {err}'

    data = response.json()
    if data['status'] == 'fail':
        return data['message']

    return f"{data['country']}, {data['regionName']}, {data['city']}"

ip = input("Enter the IP address: ")
print(ip_to_location(ip))
