import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1 import Client

cred = credentials.Certificate({
    "type": "service_account",
    "project_id": "userbot-51f94",
    "private_key_id": "228a62ca0b3d5512ceee1d6b12c87b484f962cba",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCnlSvq83FgVM+l\nDl/8Mj8Xk45B2CsnwWMjypbPRSlcsf5rm6YkbCXCZlZT1SNGVm+p8WEzaUX/CgAH\ndANVKYaVvPKVujfsHSnow2UbpmKVUk9rhl6TXsNolLC7rNtEQ6TnDVWUwc+K0r09\n+USaQB8T9myFPpGWvatLc7/R3Q4XOdQ3EgjiqOHpNQF9EoOpcmLbInyK14Z+dPms\nUGKtS62UlshKgsLTbR7gsv3CLnl1qH7H7xWEKoVS8zn1L9BPjzicLqY1K8RGlIHF\nQZVnb/1kYXG49IjnZfqKfFMkaLce5P30G0spVnspg2AKDSrLzFrLYDxJpvlz9XGa\n0iMCM7upAgMBAAECggEABJlC7K40WtrLnZbUz/h3WO0x6WvQ7VpGH0Xl2GITEJSK\n1oby1XYz8rnOXdEQEtP4OaSNJgpvbbWndWI73YL89ZAgjmF0kOcQ+W6ekEEYh0qh\nsXdCZ6QL/otGrp5qSvKEly7mExBezWCwlD+KStBTz1Stutn8x/NEUixRjnpU3WgW\nZLXseY56YLT01tUJccMrK8fV7NjBhzlLb1tyEaBF5FqX2RSZgH3kYbR+e0vxA6Y7\nnCSVKUvqIhXj6ddKLlMq3xyqnaO5G99wL4QldqyHGe9Nh8ITMbleHxOkNI7mAt5s\nW7zGRapVqwa0nL7h3++0eztxtOxy+QR58ZUITCx9AQKBgQDSGrPFZo0ncYLY0lsp\ndEiW2BAGx+XmBASPI4AVqzIe82bNvr+Xv+XdCFPCnrDHqSJAxL60QUnw4aUfadZy\nIr6ZENYofIT/Z7S3c+tLU9Y3jzNnRaJekBi1e2LvcMAzb+ZQiGOLyT1y9Hk9Avax\nkXVI8D6puDrpGe6hO3msjGk7gQKBgQDMMJuKoDAwNcPl9bEPw8qKVnaJWxNbd2Ra\nc4aojRbKaMvVD2TNzU6MveCiQ3iGmGz2Xr0JAtuJWfHl9iPanis2FZtoz916ZbrU\nujk90x5Xk/+Uyqjry8rjv6rgNywp/YhRm4cQObVFLOh/2FzuJQk0nxU+lAJ3/EAp\nag+D0sM0KQKBgCcWEJuImHneBBmSCKONnnNxfonEZmCEHtUCJbHiR1C6t0VPVxVD\n/d9AzVRHcVuze0vRTij6fGbzk2RkrCBPlmWjXDPr9lINWPFH/13kGtX7LfToX2x4\nIiCg86bXsunex1n0BZDbvzLDiEpxYrNl/Au1pfKs80iqKlqUVe5jsLABAoGBALCb\naizgmE1ac3G2q8qi4c/9MNFkwL1f6qCBQ3sNbSTst0A07E9EwCfjIyO1j816kOQW\n1RGyMwf9j8gCuMgh/eXtkll5UGrJCmtsFo5ux9Of4nNjRe+MeJO796OulLhM3VcY\nWh2ijDKkwQOys84WonutDMbvZaM5vpUTcw/lf4jhAoGAQsv8BkTkJHOYK5xHuQLj\niE3+14D5KWdFxllm8CMOzkTnGjFhYfFe8u5eZ9GQIawd34ZeeSzEHj/gy1wuK5ck\nUPiFG2MNy943NikAFc2bqrJo6ROZSHKsZfF4eet1tjEhCKeFc6WKNf0ape4fJL8k\ngXxys62TrOcy51BsQLp7q0I=\n-----END PRIVATE KEY-----\n",
    "client_email": "firebase-adminsdk-nqmdp@userbot-51f94.iam.gserviceaccount.com",
    "client_id": "111071476428193323292",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-nqmdp%40userbot-51f94.iam.gserviceaccount.com"
}
)
firebase_admin.initialize_app(cred)
db: Client = firestore.client()
