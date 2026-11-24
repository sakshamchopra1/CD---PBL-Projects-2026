"""
Stream Analytics & Generator Sample.
Tests typing, generators, mathematical transforms, and object orientation.
"""
from typing import List, Dict, Any
import math


class StreamAnalyticsPipeline:
    def __init__(self, window_size: int = 10, alpha: float = 0.2):
        self.window_size = window_size
        self.alpha = alpha

    def exponential_moving_average(self, values: List[float]) -> List[float]:
        if not values:
            return []
        ema = [values[0]]
        for i in range(1, len(values)):
            new_val = self.alpha * values[i] + (1.0 - self.alpha) * ema[-1]
            ema.append(round(new_val, 4))
        return ema

    def stream_windows(self, items: List[Any], step: int = 1):
        idx = 0
        total = len(items)
        while idx + self.window_size <= total:
            yield items[idx:idx + self.window_size]
            idx += step
