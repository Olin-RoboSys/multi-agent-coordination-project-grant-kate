def transform_path(path):
    new_path = []
    for point in path:
        new_path.append((round((point[0] - 9) * .1, 1), round((point[1] - 9) * .1, 1)))
    
    return new_path

