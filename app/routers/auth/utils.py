import bcrypt

def hash_password(password: str) -> str:
    try:
        if not password:
            raise ValueError("Password cannot be empty")
        # bcrypt only supports bytes
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hashed.decode('utf-8')  # store as string in DB
    except Exception as e:
        print(f"[HASH ERROR] Failed to hash password: {e}")
        raise e  # re-raise the exception for upstream handling


def verify_password(plain: str, hashed: str) -> bool:
    try:
        if not plain or not hashed:
            raise ValueError("Plain password or hashed password is empty")
        return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))
    except Exception as e:
        print(f"[VERIFY ERROR] Failed to verify password: {e}")
        return False  # safely return False if verification fails
