from InfinatoDB import db


def add(chat_id: int, set_name: str, item):
    doc = db.collection("TAGLIST").document(str(chat_id))
    if doc.get().to_dict() is None:
        doc.set(
            {
                set_name: {item}
            }
        )
    else:
        doc_data = doc.get().to_dict()
        if set_name in doc_data.keys():
            doc_data[set_name] = set(doc_data[set_name])
            doc_data[set_name].add(item)
        else:
            doc_data[set_name] = {item}
        doc.set(doc_data)


def rem(chat_id: int, set_name: str, item):
    doc = db.collection("TAGLIST").document(str(chat_id))
    if doc.get().to_dict() is None:
        doc.set(
            {
                set_name: {}
            }
        )
    else:
        doc_data = doc.get().to_dict()
        if set_name in doc_data.keys():
            doc_data[set_name] = set(doc_data[set_name])
            if item in doc_data[set_name]:
                doc_data[set_name].remove(item)
        else:
            doc_data[set_name] = {}
        doc.set(doc_data)


def sets(chat_id: int):
    doc = db.collection("TAGLIST").document(str(chat_id))
    if doc.get().to_dict() is None:
        doc.set({})
        return dict()
    else:
        return doc.get().to_dict()
