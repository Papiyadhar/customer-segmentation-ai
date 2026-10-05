from sklearn.cluster import KMeans


def create_segments(features, number_of_clusters=4):

    model = KMeans(
        n_clusters=number_of_clusters,
        random_state=42,
        n_init=10
    )

    model.fit(features)

    labels = model.labels_

    return model, labels