출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Policy Gradient

## 1. Policy Gradient

  현재 강화학습에서 가장 "hot"하다고 볼 수 있는 방법이 바로 Policy Gradient입니다.

  AlphaGo의 알고리즘도 "Policy Gradient with Monte-Carlo Tree Search"라고 합니다. 또한 실제 로봇이나 헬리콥터, 드론 같은 도메인에 적용하기 적합한 방법이라고 합니다.

  이웅원님의 경우 강화학습에 관심을 가지게 된 계기가 드론의 자율주행이었기 때문에 Policy Gradient는 상당히 흥미롭게 다가왔다고 합니다.

## 2. Value-based RL vs Policy-based RL

  지금까지 저희가 다루어왔던 방법들은 모두 "Value-based" 강화학습입니다. 즉, Q라는 action-value function에 초점을 맞추어서 Q function을 구하고 그것을 토대로 policy를 구하는 방식입니다.

  이전에 DQN 또한 Value-based RL으로써 DNN을 이용하여 Q-function을 approximate하고 policy는 그것을 통해 만들어졌을 뿐이었습니다.

    > Value-based reinforcement learning vs Policy-based reinforcement learning

      In the last lecture we approximated the values or action-value function using parameters 𝜃,
        V_𝜃(s) ≈ V_pi(s)
        Q_𝜃(s,a) ≈ Q_pi(s,a)

      A policy was generated directly from the value function
        e.g. using ϵ−𝑔𝑟𝑒𝑒𝑑𝑦

  그와 달리 Policy-based RL은 Policy 자체를 approximate해서 function approximator에서 나오는 것이 value function이 아니고 policy자체가 나옵니다.

  Policy자체를 parameterize하는 것입니다. 어떻게 보면 evolutionary 알고리즘의 개념에 더 가깝다고 할 수도 있습니다. 하지만 지금까지 저희가 살펴보았듯이 evolutionary 알고리즘과 달리 강화학습은 환경과의 상호작용이 있습니다.
