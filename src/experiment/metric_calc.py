import torch
from custom_rank_metrics import drawn_ROC_list


def reset_metrics(metrics):
    [metric.reset() for metric in metrics.values()]


# numerical labels: 0, 1, 2, 3, ...
def update_metrics(metrics, logits, numerical_labels):
    numerical_labels = numerical_labels.to(torch.int64)
    [metric.update(logits, numerical_labels) for metric in metrics.values()]


def compute_metrics(metrics):
    return {name: metric.compute() for name, metric in metrics.items()}


def create_metric_dictionary(metrics, class_names):
    metric_dict = dict()
    for name, metric in metrics.items():
        if name in drawn_ROC_list or name == "confusion_matrix":
            continue

        value = metric.tolist()
        if isinstance(value, list):  # one number result for each class
            metric_dict[name] = {class_names[i]: value[i] for i in range(len(value))}
        else:  # one number result for all classes
            metric_dict[name] = value

    return metric_dict