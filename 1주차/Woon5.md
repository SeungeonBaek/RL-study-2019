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


## 1.Policy iteration

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

  Policy evaluation은 perediction 문제를 푸는 것으로서 현재 주어진 policy에 대한 true value function을 구하는 것이고, Bellman equation을 사용 한다.

  현재 policy를 가지고 true value function을 구하는 것은 one-step backup으로 구합니다.

    > Problem : evaluate a given policy 𝜋
      - Solution : iterative application of Bellman expectation backup
      - v_1 -> v_2 -> ... -> v_𝜋
      - Using synchronous backup
        At each iteration k+1
        For all states
        Update v_k+1(s) from v_k(s')
        where s' is a successor state of s

  이전의 Bellman equation과 다른 점은, value function에 k라는 iteration 숫자가 붙은 것입니다.

  𝑣_(𝑘+1)(𝑠) = {𝑎 ∈ 𝐴} ∑〖𝜋(𝑎│𝑠) ∗ (𝑅(𝑠,𝑎) + 𝛾 ∗ {𝑠 ∈ 𝑆} Σ P(ss′,a) ∗ v_k(s′)〗

  현재 상태의 value function을 update하는데 reward와 next state들의 value function을 사용하는 것입니다. 전체 MDP의 모든 state에 대해서 동시에 한 번씩 Bellman equation을 계산해서 update 함으로서 k가 하나씩 올라가게 됩니다. 차례차례 state별로 구하는 것이 아니고, 한 번에 계산해서 한 번에 value function을 update합니다.

  - Policy improvement

  해당 policy에 대한 참 값을 얻었으면, 이제 policy를 더 나은 policy로 update 해 주어야 합니다. 그래야 점점 optimal policy에 가까워질 것입니다.
  그러한 과정을 policy improvement라고 합니다. improve하는 방법으로는 greedy improvement가 있습니다. 다음 state중에서 가장 높은 value function을 가진 state로 가는 것입니다. 즉, max를 취하는 것입니다. (argmax)

    > Improve the policy by acting greedily with respect to v_𝜋
      𝜋' = greedy(v_𝜋)

  위와 같이 evaluation을 통해 구한 value function을 토대로 여러 번 improve를 하게되면 optimal policy를 구할 수 있습니다. 이러한 반복되는 과정을 Policy iteration이라고 합니다.

***

## 2.Value iteration

  Value iteration이 Policy iteration과 다른 점은 Bellman Expectation equation이 아니고, Bellman Optimality equation을 사용한다는 것입니다. Bellman Optimality equation은 optimal value function들 사이의 관계 식입니다.

  Value iteration의 구현은 단순히 이 관계식을 itrative하게 변환시켜주면 됩니다.

  Policy itration의 경우에는 evaluation할 때 수많은 계산을 해줘야 하는 단점이 있었는데, 그 evaluation을 단 한 번만 하는 것이 value iteration입니다. 따라서 현재 value function을 계산하고 update할 때 max를 취함으로서 greedy하게 improve하는 효과를 줍니다. 따라서 한 번의 evaluation + improvement = value iteration이 됩니다.

    > 𝑣_(𝑘+1)(𝑠) = {𝑎 ∈ 𝐴} max⁡〖( 𝑅(𝑠,𝑎) + 𝛾 ∗ {s ∈ S} Σ (𝑃(𝑠𝑠′,𝑎) ∗ 𝑣_𝑘(𝑠′)〗

## 3. Sample Backup

  처음에 언급했다 시피 DP는 MDP 에 대한 정보를 다 가지고 있어야 optimal policy를 구할 수 있습니다. 또한 DP는 full-width backup(한 번 update할 때 가능한 모든 successor state의 value function을 통해 update하는 방법)을 사용하고 있기 때문에 단 한번의 backup을 하는 데도 많은 계산을 해야합니다.

  또한 state 숫자가 늘어날수록 계산량이 기하급수적으로 증가하기 때문에, MDP가 상당히 크거나 MDP에 대해서 다 알지 못할 때에는 DP를 적용시킬 수 없습니다.

  이때 등장하는 개념이 Sample backup입니다. 즉, 모든 가능한 successor state와 action을 고려하는 것이 아니고, Sampling을 통해서 한 길만 가보고 그 정보를 토대로 value function을 업데이트 한다는 것입니다.

  이렇게 할 경우, 계산이 효율적이라는 장점도 있지만, "Model-free"가 가능하다는 특징이 있습니다. 즉, DP의 방법대로 optimal 한 해를 찾으려면 매 iteration마다 Reward function과 state transition matrix를 알아야 하는데 sample backup의 경우에는 아래 그림과 같이 <S, A, R, S'>을 training set으로 실제 나온 reward와
