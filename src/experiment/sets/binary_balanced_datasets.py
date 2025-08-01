from src.experiment.helpers.variables import dataset_root_dir

dataset_names = [
    #"all-in-one_sentiment_balanced",
    #"amazon-reviews-0.25_balanced",
    "ceas_balanced",
    #"colon-0.5_balanced",
    #"fake-news_balanced",
    #"news-sarcasm_balanced",
    # "philippine_balanced",
    # "santander-customer-satisfaction_balanced",
    # "spambase_balanced",
    # "vehicle-sensit_balanced",
]

binary_balanced_datasets = {
    name: {
        "path": dataset_root_dir / "binary" / name,
        "classification_type": "binary",
        "class_balance": "balanced",
        "dataset_name": name,
    }
    for name in dataset_names
}