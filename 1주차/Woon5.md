/*이웅원님 Git*/

# Dynamic programming

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

  위의 세가지 방법은 각각 장점과 단점을 분명히 가지고 있습니다.

  Dynamic programming의 경우, 수학적으로 잘 설계된 모델이긴 하지만, 완전하고 정확한 모델이 필수적이라는 단점이 있습니다.

  Monte Carlo methods의 경우 simple한 컨셉을 지니고 있고, 모델을 필요로 하지는 않지만, step-by-step 학습에는 적절하지 않습니다.

  Temporal-difference methods의 경우, model이 필요하지 않고, fully incremental합니다. 그러나, 복잡하고 분석이 어렵습니다.

  각각의 방법들은 효율과 수렴속도 측면에서 여러가지 차이가 있습니다.

  또한 Dynamic programming을 다음과 같이 정의하고 있습니다.
    > The term dynamic programming (DP) refers to a collection of algorithm that can be used to compute optimal policies given a perfect model of the environment as a Markov decision process (MDP)


1.Policy iteration

  - Planning vs Learning

  Planning과 Learning의 차이를 먼저 알아보도록 하겠습니다.
  Planning이란 environment의 model을 알고서 문제를 푸는 것이고, Learning이란 environment의 model을 모르지만 상호작용을 통해서 문제를 푸는 것을 말합니다.

  Dynamic programming은 planning으로서 Environment의 model(reward, state transition matrix)에 대해서 안다는 전제에서, Bellman equation을 통해 문제를 푸는 방법을 말합니다.


    > Two fundamental problems in sequential decision making
      - Reinforcement Learning
        The environment is initially unknown
        The agent interacts with the environment
        The agent improves its policy
      - Planning
        A model of the environment is known
        The agent performs computations with its model (without any external interaction)
        The agent improves its policy
        a.k.a deliberation, reasoning, introspection, pondering, thought, search

  - Prediction & control

  Dynamic programming은 다음의 두 step (1) Prediction (2) Control 으로 나뉩니다.

  Prediction이란 현재 optimal 하지 않은 어떤 policy에 대해서 value function을 구하는 과정이며, 현재의 value function을 토대로 더 나은 policy를 구하고 이와같은 과정을 반복하여 optimal policy를 구하는 것입니다.

  - Policy evaluation

    > Problem : evaluate a given policy 𝜋
      - Solution : iterative application of Bellman expectation backup
      - v_1 -> v_2 -> ... -> v_𝜋
      - Using synchronous backup,
        At each iteration k+1
        For all states
        Update v_k+1(s) from v_k(s')
        where s' is a successor state of s

  Policy evaluation은 perediction 문제를



***
