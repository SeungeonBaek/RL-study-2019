출처 : https://dnddnjs.gitbooks.io/rl/content/value_function_approximation.html
/*이웅원님 Git*/

# Off-Policy Control

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

  Off-Policy 또한 MC와 TD로 갈립니다. Off-Policy MC는 아래와 같습니다. 에피소드가 끝나고 return을 계산할 때 아래와 같이 식을 변형시켜줍니다. 각 스텝에 reward를 받게 된 것은 𝜇라는 policy를 따라서 얻었던 것이므로 매 step마다 𝜋/𝜇를 해주어야 합니다. 따라서 Monte-Carlo에 Off-policy를 적용시키는 것은 그리 좋은 아이디어가 아닙니다.

    > Importance Sampling for Off-Policy Monte-Carlo method
      Use returns generated from 𝜇 to evaluate 𝜋
      Weight return G_t according to similarity between policies
      Multiply importance sampling corrections along whole episode
                    𝜋(A_t|S_t) * 𝜋(A_(t+1)|S_(t+1)) ... 𝜋(A_T|S_T)
       G^(𝜋/𝜇)_t = ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ * G_t
                    𝜇(A_t|S_t) * 𝜇(A_(t+1)|S_(t+1)) ... 𝜇(A_T|S_T)

      Update value towards corrected return
        V(S_t) <- V(S_t) + 𝛼 * (G^(𝜋/𝜇)_t - V(S_t))

  Off-Policy TD에서는 MC 때와는 달리 Importance Sampling을 1-step만 진행하면 됩니다.
  MC때와 비교하면 Variance가 낮아지기는 했지만 여전히 원래 TD에 비하면 Importance sampling때문에 높은 variance를 가지고 있습니다. Off-policy learning을 할 떄 Importance sampling말고 다른 방법을 생각할 필요가 있습니다. 바로 여기서, 유명한 Q learning 알고리즘이 나오게 됩니다.

    > Importance Sampling for Off-Policy Temporal Difference method
      Use TD targets generated from 𝜇 to evaluate 𝜋
      Weight TD target R + 𝛾 * V(S') by importance sampling
      Only need a single importance sampling correction
                                ( (𝜋(A_t|S_t)                                       )
        V(S_t) <- V(S_t) +  𝛼 * ( ㅡㅡㅡㅡㅡㅡ * (R_(t+1) + 𝛾 * V(S_(t+1) - V(S_t)) ))
                                ( 𝜇(A_t|S_t))                                       )

***

## Q Lenarning

## 1. Q-Learning

  Off-Policy Learning 알고리즘 중에서 Off-policy MC와 Off-policy TD가 있지만 Importance sampling문제 때문에 새로운 방법이 필요하다고 말했었습니다. Off-Policy learning을 하는데 가장 좋은 알고리즘은 Q Learning입니다. 방법은 다음과 같습니다.

  현재 state S에서 action을 선택하는 것은 behaviour policy를 따라서 선택합니다. TD에서 update할 때는 one-step을 bootstrap하는데 이 때 다음 state의 action을 선택하는 데는 behaviour policy와는 다른 policy(alternative policy)를 사용하면 Importance Sampling이 필요하지 않습니다.

  이전의 Off-Policy에서는 Value function을 사용했었는데 여기서는 action-value function을 사용함으로써 다음 action까지 선택을 해야하는데 그 때 다른 policy를 사용한다는 것입니다.
    > Q-Learning
      We now consider off-policy learning of action-values Q(s,a)
      No importance sampling is required
      Next action is chosen using behaviour policy A_(t+1) ~ 𝜇(∙|S_t)
      But we consider alternative successor action A' ~ 𝜋(∙|S_t)
      And update Q(S_t, A_t) towards value of alternative action
        Q(S_t, A_t) <- Q(S_t, A_t) + 𝛼 * (R_(t+1) + 𝛾 * Q(S_(t+1), A') - Q(S_t, A_t))

***

## 2. Off-Policy control with Q-Learning

  이 Q learning 알고리즘 중에서 가장 유명한 것이 아래입니다.
  - Behaviour policy로는 ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 w.r.t. Q(s,a)
  - Target policy(alternative policy)로는 𝑔𝑟𝑒𝑒𝑑𝑦 w.r.t Q(s,a)

  위와 같이 behavior policy와 target policy를 택한 알고리즘입니다. 이전에 Off-policy의 장점이 exploratory policy를 따르면서도 optimal policy를 학습할 수 있다고 했는데 그게 바로 이 알고리즘입니다. greedy한 policy로 학습을 진행하면 수렴을 빨리 하는데 충분히 탐험을 하지 않았기 때문에 local에 빠지기가 쉽습니다.

  그렇기 때문에, 탐험을 위해 ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 policy를 사용하게 되면 수렴속도가 느려져서 학습속도가 느려지게 됩니다. 이를 해결하기 위한 방법이 ϵ(epsilon)을 시간에 따라 decay기키는 방법과 아래와 같이 Q learning을 사용하는 것입니다.

    > Off-Policy Control with Q-Learning
      We now allow both behaviour and target policies to improve
      The target policy 𝜋 is greedy w.r.t. Q(s,a)
        𝜋(S_(t+1)) = {a') argmax{ Q(S_(t+1),a') }

      The behaviour policy mu is e.g. ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 w.r.t Q(s,a)
      The Q-learning target then simplifies:
         R_(t+1) + 𝛾 * Q(S_(t+1), A')
       = R_(t+1) + 𝛾 * Q(S_(t+1), {a'}argmax{ Q(S_(t+1),a') })
       = R_(t+1) + {a'}max {𝛾 * Q(S_(t+1), a')}

  아래 알고리즘은 사실 Bellman Optimality Equation을 사용한 Value iteration을 이용한 것입니다.
  Optimal valuefunction끼리의 관계식을 이용해서 update를 하는 것입니다. 이렇게 update를 할 때 optimal action-value function에 수렴하게 됩니다.

    > Q-Learning control Algorithm
      식      : Q(S,A) <- Q(S,A) + 𝛼 * (R_(t+1) + 𝛾 * {a'}max {Q(S_(t+1), a')} - Q(S,A))
      Theorem : Q-learning control converges to the optimal action-value function, Q(s,a) -> q*(s,a)

      Pseudo code
        Initialize Q(s,a), s S, a A, arbitrarily, and Q(terminal-state,∙) = 0
        Repeat (for each episode):
          Initialize S
          Repeat (for each step of episode):
            Choose A from S using policy derived from Q (e.g., ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
            Take action A, observe R, S'
            Q(S,A) <- Q(S,A) + 𝛼 * [R + 𝛾 * {a} max(Q(S',a)) - Q(S<A)]
            S <- S';
          until S is terminal

***

## 3. Sarsa vs Q-learning

  이렇게 Q-learning에 대해서 살펴봐도 직관적으로 Q-learning이 어떤 방식으로 작동하는지 잘 와닿지 않을 것입니다. Q-learning을 이해하려면 SARSA와 비교해보는 것이 좋습니다. Sutton이 이 두가지를 비교할 수 있는 예제를 제시했습니다. "Cliff Wlking"이라는 예제입니다.

  이 예제에서 목표는 S라는 start state에서 시작해서 Goal까지 가는 optimal path를 찾는 것입니다. 그림에 나와있는 Cliff에 빠져버리면 -100의 reward를 받고 time-step마다 reward를 -1씩 받는 문제라서 절벽에 빠지지 않고 goal까지 가능한 한 빠르게 도착하는 것이 목표입니다.

  눈으로 딱 봐도 그림에 있는 optimal path가 답이라고 생각합니다. SARSA와 Q-learning 모두 다 $$\epsilon$$-greedy한 policy로 움직입니다. 따라서 더러는 Cliff에 빠져버리기도 합니다. 차이는 SARSA는 on-policy라서 그렇게 Cliff에 빠져버리는 결과로 인해 그 주변의 상태들의 value를 낮다고 판단합니다. 하지만 Q-learing의 경우에는 비록 $$\epsilon$$-greedy로 인해 Cliff에 빠져버릴지라도 자신이 직접 체험한 그 결과가 아니라 greedy한 policy로 인한 Q function을 이용해서 업데이트합니다. 따라서 Cliff 근처의 길도 Q-learning은 optimal path라고 판단할 수 있어서 이 문제의 경우 SARSA보다는 Q-learning이 적합하다고 할 수 있습니다.

  SARSA에서 탐험을 위해서 $$\epsilon$$-greedy를 사용했지만 결국은 그로인해서 정작 에이전트가 optimal로 수렴하지 못하는 현상들이 발생한 것입니다. 따라서 Q-learning의 등장 이후로는 많은 문제에서 Q-learning이 더 효율적으로 문제를 풀었기 때문에 강화학습에서 Q-learning은 기본적인 알고리즘으로 자리를 잡게 됩니다.








  asd
