from InfinatoDB import db


def set(collection: str, doc_id: str, data: dict):
    return db.collection(collection).document(doc_id).set(data)


def add(collection: str, data: dict):
    return db.collection(collection).add(data)


def rem(collection: str, doc_id: str):
    return db.collection(collection).document(doc_id).delete()


def get(collection: str, doc_id: str = None):
    if doc_id:
        return db.collection(collection).document(doc_id).get().to_dict()
    else:
        ref = db.collection(collection).stream()
        docs = {}
        for doc in ref:
            docs[doc.id] = doc.to_dict()
        return docs
