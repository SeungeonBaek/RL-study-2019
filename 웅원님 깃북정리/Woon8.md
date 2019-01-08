/*이웅원님 Git*/

# Q-Learning

## Importance Sampling

  지금까지 Monte-Carlo Control과 Temporal-Difference Control을 살펴보았습니다. 사실은 두 방법 모두 on-policy reinforcement learning입니다. 여기서 새로운 개념을 하나 알고 갈 필요가 있습니다.

## 1. On-Policy vs Off-Policy

  다시 Sarsa의 알고리즘을 살펴보겠습니다. 아래와 같이 Sarsa에서는

  - Choose A  from S  using Policy derived from Q
  - Choose A' from S' using Policy derived from Q

  action을 선택하는 것이 두 부분이 맞습니다. 보면 둘 다 공통적으로 "using Policy derived from Q"가 사용된다는 것을 알 수 있습니다.

    > An on-policy TD control algorithm
      Initialize Q(s,a), s ∈ S, 𝑎 ∈ 𝐴, arbitrarily, and Q(terminal-state,∙) = 0
      Repeat (for each episode):
        Initialize S
        Choose A from S using policy derived from Q(e.g. ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
        Repeat (for each step of episode):
          Take action A, observe R, S'
          Choose A' from S' using policy derived from Q(e.g. ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
          Q(S,A) <- Q(S,A) + 𝛼 * (R + 𝛾 * Q(S',A') - Q(S,A))
          S <- S'; A <- A';
      until S is terminal

  이 말은 즉 현재 policy로 움직이면서 그 policy를 평가한다는 것입니다. 위 알고리즘에서 보면 에이전트가 실제로 움직인 Q function으로 현재의 Q function을 update합니다. 따라서 현재 policy위에서 control(prediction + policy improvement)을 하기 때문에 on-policy라고 생각해도 좋습니다.

  하지만 on-policy에는 한계가 존재합니다. 바로 탐험의 문제입니다. 현재 알고있는 정보에 대해 greedy로 policy를 정해버리면 optimal에 가지 못 할 확률이 커지기 때문에 에이전트는 항상 탐험이 필요합니다.

  따라서 on-policy처럼 움직이는 policy와 학습하는 policy가 같은 것이 아니고 이 두개의 policy를 분리시킨 것이 off-policy입니다. Silver는 수업에서 Off-policy를 다음과 같이 정의합니다.

    > Off-policy definition
      Evaluate target policy 𝜋(a|s) to compute v_𝜋(s) or q_𝜋(s,a)
      While following behaviour policy 𝜇(a|s)
        {S_1, A_1, R_2, ... , S_T} ~ 𝜇
      Why is this important?
        Learn from observing humans or other agents
        Re-use experience generated from old policies 𝜋_1, 𝜋_2, ..., 𝜋_(t-1)
        Learn about optimal policy while following exploratory policy
        Learn about multiple policies while following one policy
