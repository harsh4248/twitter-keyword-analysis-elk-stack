indexMapping = {
    "properties":{
        "author": {
            "type":"text"
        },
        "content": {
            "type":"text"
        },
        "date_time": {
            "type":"text"
        },
        "language": {
            "type":"text"
        },
        "number_of_likes": {
            "type":"long"
        },
        "number_of_shares": {
            "type":"long"
        },
        "ContentVector": {
            "type":"dense_vector",
            "dims":768,
            "index":True,
            "similarity":"l2_norm"
        }
    }
}