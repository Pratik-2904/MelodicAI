from fastapi import HTTPException, Header
import jwt


def auth_middleware(x_auth_token=Header()):
    try:
        # take token from the request
        if not x_auth_token:
            raise HTTPException(status_code=401, detail="No auth token, access denied!")
        # decode the token
        verified_token = jwt.decode(x_auth_token, "Password_key", ["HS256"])

        if not verified_token:
            raise HTTPException(401, "Token cerification failed, Authorization denied!")
        # extract the id
        uid = verified_token.get("id")
        return {"id": uid, "token": x_auth_token}
        # get info from database
    except jwt.InvalidTokenError:
        raise HTTPException(401, "Token is not valid, authorization failed!")
