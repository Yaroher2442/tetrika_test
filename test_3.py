import requests

r = requests.post('http://127.0.0.1:5000/get_appearance', json={
    'lesson': [3200, 6800],
    'pupil': [3340, 3389, 3390, 3395, 3396, 6472],
    'tutor': [3290, 3430, 3443, 6473]
})
print(r.status_code)
print(r.json())
