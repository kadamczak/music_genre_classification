import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src/experiment')))
from src.experiment.metrics.probabilistic.mse import MSE
from src.experiment.helpers.task_type import TaskType

from helpers.metric_test_base import MetricTestBase
import numpy as np
from helpers.sample_data import (
    multiclass_imbalanced_1,
    multiclass_balanced_2,
    multiclass_balanced_3,
    multiclass_balanced_4,
    multiclass_balanced_5,
    binary_imbalanced_6,
    binary_balanced_7,
    binary_8,
    binary_9,
    binary_10,
    binary_11,
    binary_12,
    binary_13,
    multilabel_14
)



class TestMSE(MetricTestBase):
    def setUp(self):
        self.metric_name = "mse"
        self.multiclass_metric_calculator = MSE(num_classes=3, task_type=TaskType.MULTICLASS)
        self.binary_metric_calculator = MSE(num_classes=2, task_type=TaskType.BINARY)
        self.multilabel_metric_calculator = MSE(num_classes=3, task_type=TaskType.MULTILABEL)
        
    def test_Compute_ShouldCalculate_WhenMulticlassimbalanced(self):
        self.expected_matches_result(self.multiclass_metric_calculator, multiclass_imbalanced_1)
          
    def test_Compute_ShouldCalculate_WhenMulticlassBalanced(self):
        self.expected_matches_result(self.multiclass_metric_calculator, multiclass_balanced_2)
        
    def test_Compute_ShouldCalculate_WhenMulticlassBalanced_When0TrueSamplesInClass(self):
        self.expected_matches_result(self.multiclass_metric_calculator, multiclass_balanced_3)
        
    def test_Compute_ShouldCalculate_WhenMulticlassBalanced_When0PredictionsInClass(self):
        self.expected_matches_result(self.multiclass_metric_calculator, multiclass_balanced_4)
        
    def test_Compute_ShouldCalculate_WhenMulticlassBalanced_When0TrueSamplesAndPredictionsInClass(self):
        self.expected_matches_result(self.multiclass_metric_calculator, multiclass_balanced_5)
        
    def test_Compute_ShouldCalculate_WhenBinaryimbalanced(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_imbalanced_6)

    def test_Compute_ShouldCalculate_WhenBinaryBalanced(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_balanced_7)

    def test_Compute_ShouldCalculate_WhenBinary_When0TrueSamplesInPositiveClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_8)
        
    def test_Compute_ShouldCalculate_WhenBinary_When0TrueSamplesInNegativeClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_9)

    def test_Compute_ShouldCalculate_WhenBinary_When0PredictionsInPositiveClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_10)

    def test_Compute_ShouldCalculate_WhenBinary_When0PredictionsInNegativeClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_11)
        
    def test_Compute_ShouldCalculate_WhenBinary_When0TrueSamplesAndPredictionsInPositiveClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_12)
        
    def test_Compute_ShouldCalculate_WhenBinary_When0TrueSamplesAndPredictionsInNegativeClass(self):
        self.expected_matches_result(self.binary_metric_calculator, binary_13)
        
    def test_Compute_ShouldCalculate_WhenMultilabel1(self):
        self.expected_matches_result(self.multilabel_metric_calculator, multilabel_14)
