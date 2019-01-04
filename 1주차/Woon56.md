/*이웅원님 Git*/

- Dynamic programming

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

  위의 세가지 방법은 각각 장점과 단점을 분명히 가지고 있습니다.

  Dynamic programming의 경우, 수학적으로 잘 설계된 모델이긴 하지만, 완전하고 정확한 모델이 필수적이라는 단점이 있습니다.

  Monte Carlo methods의 경우 simple한 컨셉을 지니고 있고, 모델을 필요로 하지는 않지만, step-by-step 학습에는 적절하지 않습니다.

  Temporal-difference methods의 경우, model이 필요하지 않고, fully incremental합니다. 그러나, 복잡하고 분석이 어렵습니다.

  각각의 방법들은 효율과 수렴속도 측면에서 여러가지 차이가 있습니다.

  또한 Dynamic programming을 다음과 같이 정의하고 있습니다.
    > The term dynamic programming (DP) refers to a collection of algorithm that can be used to compute optimal policies given a perfect model of the environment as a Markov decision process (MDP)

1.Policy iteration


==================================================================
