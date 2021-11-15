import hashlib

def calculate_md5(fpath, chunk_size=1024 * 1024):
    md5 = hashlib.md5()
    with open(fpath, 'rb') as f:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            md5.update(chunk)
    return md5.hexdigest()

if __name__ =='__main__':
    data_basedir = 'data/MaskedFaceNet/'
    train_list = [
        ['data_batch_1', '0776d4245a4a93bf15225d562ea234c7'],
        ['data_batch_2', '91379bdf014d7b916126b6874bec417a'],
        ['data_batch_3', '8d5323e4bd205066a4d9a5030e83e54a'],
        ['data_batch_4', 'b14aa06c3ca3c9e16d9a1743fc788b3d'],
    ]
    test_list = [
        ['test_batch', '331dbc95243fa768facb1dfbab5c48ef'],
    ]
    for item in train_list:
        path = data_basedir + item[0]
        print(path)
        print(calculate_md5(path))
    for item in test_list:
        path = data_basedir + item[0]
        print(path)
        print(calculate_md5(path))
    path = data_basedir + 'batches.meta'
    print(path)
    print(calculate_md5(path))

