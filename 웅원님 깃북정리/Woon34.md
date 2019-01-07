/*이웅원님 Git*/

# Bellman Equation

## 1. Bellman Equation

  Bellman Equation은 Dynamic programming의 기반이 되는 방정식 입니다.

  이전 markdown에 정리해 놓았듯이, MDP에서  Value function에는 state-value function v(s)와 action-value function q(s,a) 두 가지가 있습니다.

  Value function의 정의에서, value function은 다음과 같이 풀어 쓸 수 있습니다.

  - v(s) = E[G_t | S_t = s]

  = E[R_t+1 + 𝛾 * R_t+2 + 𝛾^2 * R_t+3 + ... | S_t = s]

  = E[R_t+1 + 𝛾 * (R_t+2 + 𝛾 * R_t+3 + ...) | S_t = s]

  = E[R_t+1 + 𝛾 * G_t+1 | S_t = s]

    > E[R_t+1 + 𝛾 * v(S_t+1) | S_t = s]

  이 중 가장 중요한 식은 마지막 식으로, 이 식은 현재 state와 다음 state사이의 value function을 관계짓는 식입니다.

  이 식을 Bellman equation이라고 합니다.

  이와 비슷하게 action-value function도 다음과 같이 표현할 수 있습니다.

    > q(s,a) = E[R_t+1 + 𝛾 * q(S_t+1, A_t+1) | S_t = s, A_t = a]

  이렇게 위와같이 expectation을 이용한 표현은 조금 추상적일 수 있으며, 다음과 같이 표현할 수 있습니다.

  현재 state의 value function과 다음 state의 value function의 상관관계 식을 구하려면 그 사이에 있는 state-action pair에 대해서 그 관계를 나눠볼 필요가 있습니다.

  그렇게 되면, v(s)라는 값은 다음과 같이, s에서 선택할 수 있는 모든 a 에 대해 𝜋(𝑎│𝑠) * q(s,a) 합한 것과 같다고 할 수 있습니다.

    > 𝑣_𝜋 (𝑠) = {a∈𝐴} ∑〖𝜋(𝑎│𝑠) * 𝑞_𝜋 (𝑠,𝑎)〗

***

  q(s,a)라는 것은 S_t = s, A_t = a 일때의 G_t인데, 이는 R_t+1 + 𝛾 * R_t+2 + 𝛾^2 * R_t+3 + ... 입니다. 그러므로, 다음과 같은 식을 얻습니다.

    > 𝑞_𝜋 (𝑠,𝑎)=𝑅(𝑠,𝑎) + 𝛾 ∗ {s∈S}∑〖𝑃(𝑠𝑠′,𝑎)∗𝑣_𝜋 (𝑠^′)〗

        > R_t+1 = R(s,a) / 𝛾 * R_t+2 + 𝛾^2 * R_t+3 + ... 𝛾 ∗ {s∈S}∑〖𝑃(𝑠𝑠′,𝑎)∗𝑣_𝜋 (𝑠′)〗

***

  이 두개의 식을 합치면, 다음과 같은 식을 얻을 수 있습니다.

    > 𝑣_𝜋 (𝑠) = {a∈𝐴}∑〖𝜋(𝑎│𝑠)∗(𝑅(𝑠,𝑎)+𝛾∗Σ𝑃(𝑠𝑠′,𝑎)∗𝑣_𝜋 (𝑠^′ ))〗

  실제 강화학습으로는 무엇인가를 학습 시킬 때 reward와 transition probability P는 미리 알 수가 없습니다. 경험을 통해서 알아가야만 하는 것입니다.

  이러한 정보를 다 알면 MDP를 모두 안다고 표현하며, 이러한 정보들이 MDP의 model이 됩니다.

  강화학습의 큰 특징은 바로 MDP의 model을 몰라도 학습할 수 있다는 것입니다.

  따라서, reward function과 state transition probability를 모르고 학습하는 강화학습에서는 Bellman equation으로는 구할 수가 없습니다.

  - Bellman Equation for Q-function

  같은 식을 action value function에 대해서 작성하고 그림을 보면 다음과 같습니다.

    > 𝑞_𝜋(𝑠,𝑎) = 𝑅(𝑠,𝑎) + 𝛾 ∗ {s∈𝑆}∑〖 𝑃(𝑠𝑠^′,𝑎) {a∈𝐴}∑ 𝜋(𝑎′│𝑠′) * 𝑞_𝜋(𝑠′, 𝑎′) 〗

***

  - Optimal value function

  Bellman optimality equation을 보기 전에 optimal value function에 대해서 살펴보도록 하겠습니다.

  강화학습의 목적이 accumulative future reward를 최대로 하는 policy를 찾는 것이었습니다.

  optimal state-value function이란, 현재 state에서 policy에 따라서 앞으로 받을 reward들이 달라지는데, 그 중에서 앞으로 가장 많은 reward를 받을 policy를 다랐을 때의 value function입니다.

  optimal action-value function도 마찬가지로, (s,a)에서 얻을 수 있는 최대의 value function입니다.

  정의 : The optimal state-value function v_*(s) is the maximum value function over  all policies

    > v_*(s) = max_𝜋(v_𝜋(s))

  The optimal action-value function q_*(s) is the maximum action-value function over all policies

    > q_*(s,a) = max_𝜋(q_𝜋(s,a))

    The optimal value function specifies the best possible performance in the MDP

  - An MDP is "solved" when we know the optimal value function

  즉, 현재 environment에서 취할 수 있는 가장 높은 값의 reward 총 합입니다.

  위의 두 식중에서 두번째 식. 즉, optimal action-value function의 값을 안다면 단순히 q 값이 높은 action을 선택해주면 되므로, 이 최적화 문제는 풀렸다라고 볼 수 있습니다.

  강화학습 뿐만 아니라, Dynamic programming 에서도 목표가 되는 optimal policy는 다음과 같습니다.

  optimal policy는 (s,a)에서 action-value function이 가장 높은 action만을 고르기 때문에 deterministic하다고 할 수 있습니다.

  An optimal policy can be found by maximising over q_*(s,a)

    > 𝜋_* (a|s) = 1 (if a = argmax q_*(s,a) ) or 0 (if otherwise)
