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

  Off-policy는 다음과 같은 장점이 있습니다.
  - 다른 agent나 사람을 관찰하고 그로부터 학습할 수 있다.
  - 이전의 policy들을 재활용하여 학습할 수 있다.
  - 탐험을 계속 하면서도 optimal한 policy를 학습할 수 있다. (Q-learning)
  - 하나의 policy를 따르면서 여러개의 policy를 학습할 수 있다.

## 2. Importance Sampling

  위에서 Off-policy learning이 어떤 것인지 배웠습니다. 하지만 다른 policy로 부터 현재 policy를 학습할 수 있다는 근거가 무엇일까요? "importance sampling"이라는 개념은 원래 통계학에서 사용하던 개념으로 아래와 특정한 분포의 값들을 추정하는 기법중의 하나입니다.

    > Importance sampling
      In statics, importance sampling is a general technique for estimating properties of a particular distribution,
      while only having samples generated from a different distribution than the distribution of interset

  어떤 값을 추정하는데 가장 기본적인 방법은 그냥 random하게 찍어보는 것입니다. 이미 저희가 배웠다시피 이러한 process료 표현하는 말은 "monte-carlo"로서 Monte-Carlo estimation이라고 합니다. 하지만 너무 광범위하게 탐색하기도 하고 어떠한 중요한 부분을 알아서 그 위주로 탐색을 하면 더 빠르고 효율적으로 값을 추정할 수 있고 그러한 아이디어가 바로 "Importance Sampling"입니다.

  importance sampling에 대한 간단한 설명은 다음과 같습니다. p와 q라는 distribution이 있을 때 q라는 distribution에서 실제로 진행을 함에도 불구하고 p로 추정하는 것처럼 할 수 있다는 것입니다. 강화학습에서도 policy가 다르면 state의 distribution은 달라지게 되어 있습니다. 따라서 다른 distribution을 통해 추정할 수 있다는 개념을 그대로 가져와서 다른 policy를 통해서 얻어진 sample을 이용하여 Q 값을 추정할 수 있다는 것입니다. 일종의 trick이라고 할 수 있을 것 같습니다.

  위의 내용을 David Silver교수님은 아래와 같이 설명합니다. f(X)라는 함수를 value function이라고 생각하고 강화학습에서는 이 value function = expected future reward를 계속 추정해 나가는데 P(x)라는 현재 policy로 형성된 distribution으로부터 학습을 하고 있었습니다. 하지만 다른 Q라는 distribution을 따르면서도 똑같이 학습할 수 있는데 단, 아래와 같이 간단히 식을 변형시켜주면 됩니다. Q(x)를 곱해주고 나눠주면 됩니다.

    > Importance Sampling
      Estimate the expectation of a different distribution
        E_(X~P)[f(x)] = Σ P(X) * f(X)
                      = Σ Q(X) * (P(X)/Q(X)) * f(X)
                      = E_(X~Q)[ (P(X)/Q(X)) * f(x)]

  Off-Policy 또한 MC와 TD로 갈립니다. Off-policy MC는 아래와 같습니다. 에피소드가 끝나고 return을 계산할 때 아래와 같이 식을 변형시켜줍니다. 각 스텝에 reward를 받게 된 것은 𝜇라는 policy를 따라서 얻었던 것이므로 매 step마다 𝜋/𝜇를 해주어야 합니다. 따라서 Monte-Carlo에 Off-policy를 적용시키는 것은 그리 좋은 아이디어가 아닙니다.

    > Importance Sampling for Off-Policy Monte-Carlo
      Use returns generated from 𝜇 to evaluate 𝜋
      Weight return G_t according to similarity between policies
      Multiply importance sampling corrections along whole episode
                    𝜋(A_t|S_t) * 𝜋(A_(t+1)|S_(t+1)) ... 𝜋(A_T|S_T)
       G^(𝜋/𝜇)_t = ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ * G_t
                    𝜇(A_t|S_t) * 𝜇(A_(t+1)|S_(t+1)) ... 𝜇(A_T|S_T)

      Update value towards corrected return
        V(S_t) <- V(S_t) + 𝛼 * (G^(𝜋/𝜇)_t - V(S_t))




















  asd
