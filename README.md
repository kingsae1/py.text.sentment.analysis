# Python을 이용한 텍스트 감정 분석
## 데이터 처리 Flow
데이터를 처리하기 위해 아래와 같은 Flow를 이용하여 학습한다
   1. 데이터 수집
   2. 데이터 확인 및 탐색
   3. 데이터 전처리 / 정제
   4. 데이터 모델링 / 학습
   5. 데이터 평가
   6. 배포

배포 후 다시 1.데이터 수집부터 시작하여 연속적인 데이터들에 대해서 학습된다

```python
import pandas as pd
import numpy as np
from math import log
```
