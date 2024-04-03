import base64
import json


def main():
    jwt = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJzbWFydHBvcyIsImdydCI6WyJwb3M6c3RhdHVzIiwicG9zOmNvbmZpZ3VyYXRpb24iLCJtYnVzOnBvcy5wYXltZW50LnB1c2giLCJwb3M6ZmluYWxpemUtb3JkZXIiLCJvcmRlcnM6Y3JlYXRlIl0sIm1pZCI6MTAwMTAwMSwiaWF0IjoxNzEwNTE0MjMxLCJqdGkiOiI3OTk0NiIsInRpZCI6IjAwMDAwME5uIiwic2lkIjo5MTI3OX0.QI1iPp9T1Uuh8QnhblLfT-3_gX0EqakNBT4pKMrorG4"

    parts = jwt.split(".")
    if len(parts) != 3:
        print("Invalid JWT format")
        return

    header = decode_base64(parts[0])
    payload = decode_base64(parts[1])
    tid = parse_tid(payload)

    print("Header:", header)
    print("Payload:", payload)
    print("Tenant ID:", tid)


def decode_base64(encoded_string):
    decoded_bytes = base64.urlsafe_b64decode(encoded_string + "==")
    return decoded_bytes.decode("utf-8")


def parse_tid(payload):
    payload_dict = json.loads(payload)
    tid = payload_dict.get("tid")
    return tid


if __name__ == "__main__":
    main()
