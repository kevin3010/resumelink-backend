# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_list_of_jobs():
    response = client.get("/list-of-jobs")
    assert response.status_code == 200
    assert response.json() == {
        'jobs': [
            {
                'CompanyName': 'Scotiabank', 
                'Date': '29/05/2024', 
                'Location': 'Toronto, Ontario, Canada', 
                'Position': 'Software Engineer [Scotiabank]', 
                'JobURL': 'https://www.linkedin.com/jobs/view/3933412770/?alternateChannel=search&refId=o0AbxSfASVj4oVig2XFSbg%3D%3D&trackingId=MumxlQCiD5YPk6Usx9fP1w%3D%3D&trk=d_flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3B4JWZY3UZQj2sCOW8bk5rJw%3D%3D'
            }, 
            {
                'CompanyName': 'The Home Depot Canada', 
                'Date': '29/05/2024', 
                'Location': 'Toronto, Ontario, Canada', 
                'Position': 'Junior Backend / Fullstack Developer (Askuity Division)', 
                'JobURL': 'https://www.linkedin.com/jobs/view/3920564788/?alternateChannel=search&refId=o0AbxSfASVj4oVig2XFSbg%3D%3D&trackingId=cq%2Fb6xV8aOOiKFRuyh49mQ%3D%3D&trk=d_flagship3_search_srp_jobs&lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_jobs%3B4JWZY3UZQj2sCOW8bk5rJw%3D%3D'
            }
        ]
    }
