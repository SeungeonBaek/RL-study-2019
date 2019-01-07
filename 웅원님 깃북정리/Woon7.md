/*이웅원님 Git*/

# Temporal Difference Learning

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

# TD Prediction

## 1. Tmeporal Difference

  이전 Chapter에서 배웠던 Monte-Carlo Control은 Model-Free Control입니다. Model-Free라는 점에 강화학습이지만 단점이 있습니다. 바로 online으로 바로바로 학습할 수가 없고 꼭 끝나는 episode여야 한다는 단점이 있습니다.
  끝나지 않더라도 eipsode가 길 경우에는(예를 들어 atari 게임이 아니라 starcraft같은 에김) 학습하기 어려운 단점이 있습니다. 따라서 자연스럽게도 꼭 episode가 끝나지 않더라도 DP처럼 time step마다 학습할 수 있지 않나?라는 생각을 하게 됩니다. 이게 바로 Temporal Difference이며 Sutton교수님 책에서는 아래와 같이 소개하고 있습니다.

    > Temporal Difference method
      If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning.
      TD learning is a combination of Monte-Carlo ideas and dynamic programming (DP) ideas.
      Like Monte-Carlo methods, TD methods can learn directly from raw experience without a model of the environment's dynamics.
      Like DP, TD methods update estimates based in part on other learned estimates, without wating for a final outcome (they bootstrap)

  Temporal difference(TD)는 MC와 DP를 섞은 것으로써 MC처럼 raw experience로부터 학습할 수 있지만 DP처럼 time step마다 학습할 수 있는 방법입니다. 마지막에 "bootstrap"이라고 하는데 이 말은 무엇을 뜻할까요?

  대학생활을 예로 들어보겠습니다. MC는 대학교에 들어와서 졸업을 한 다음에 그 동안을 돌아보며 "이건 더 했어야 했고 술은 덜 마셔야했다"라고 생각하며 다시 대학교를 들어가서 대학생활을 하면서 졸업할 때까지 똑같이 살다가 다시 졸업하고 자신을 돌아보는 반면에 TD같은 경우는 같은 대학교를 다니고 있는 2학년 선배가 1학년을 이끌어주는 것과 같습니다.

  사실은 둘 다 졸업을 해보지 않은 상태에서 (잘 모르는 상황에서)이끌어 주는 것이지만 대학교를 다니면서 바로 바로 자신을 고쳐나가기 때문에 어쩌면 더 옳은 방법일지도 모릅니다.

  TD는 따라서 현재의 value function을 계산하는데 앞선(앞선이라고 표현하기에는 조금 애매한 부분이 있습니다.) 주변 state들의 value function을 사용합니다. 이 것은 이전에 배웠던 Bellman equation이며, 따라서 Bellman equation자체가 Bootstrap하는 것이라고 볼 수 있습니다.

***

## 2. TD(0)

  Temporal Difference(TD)는 Monte-Carlo + DP라고 말했었습니다. 이전에 봤던 Monte-Carlo prediction에서 incremental mean을 보면 아래와 같이 return을 사용해서 update합니다. TD에서는 이 G_t를 R_(t+1) + 𝛾 * V_(t+1)(s)로 바꿔서 아래와 같은 식이 됩니다.
  Temporal Difference learning 방법에도 여러가지가 있는데 그 중에서 가장 간단한 방법은 TD(0)이고 방금 말한 방법이 바로 TD(0)입니다.
  R_(t+1) + 𝛾 * V_(t+1)(s)를 TD target이라고 부르고 그 target과 현재의 value function과의 차이를 TD error라고 부릅니다.

    > Temporal Differenc TD(0)
      Goal : leaern v_𝜋 online from experience under policy 𝜋
      Incremental every-visit Monte-Carlo
        Update value V(S_t) toward actual return G_t
          V(S_t) <- V(S_t) + 𝛼 * (G_t - V(S_t))

      Simplest temporal-difference learning algorithm : __TD(0)__ !
        Update value V(S_t) toward estimated return R_(t+1) + 𝛾 * V_(t+1)(s)
          V(S_t) <- V(S_t) + 𝛼 * (R_(t+1) + 𝛾 * V_(t+1)(s) - V(S_t))

      R_(t+1) + 𝛾 * V_(t+1)(s) is called the TD target
      𝛿_t = R_(t+1) + 𝛾 * V_(t+1)(s) - V(S_t) is called the TD error

      => V_(S_t) = V(S_t) + 𝛼 * 𝛿_t

  TD(0)의 알고리즘을 살펴보고 backup diagram을 보면 아래와 같습니다.

    > TD(0) algorithm
      Input : the policy 𝜋 to be evaluted
      Initialize V(s) arbitrarily (e.g., V(s) = 0, ∀s ∈ S+)
      Repeat (for each episode):
        A <- action given by 𝜋 for S
        Take action A; observe reward, R, and next state, S'
        V(S) <- V(S) + alpha[R + 𝛾 * V(S') - V(S)]
        S <- S'
      until S is terminal

***

## 3. Monte-Carlo method vs Temporal Difference method

  MC의 경우에는 다 도착한 다음에 각각의 state에서 예측했던 value function과 실제로 받은 returen을 비교해서 update하게 됩니다. 하지만 TD에서는 한 step 진행을 하면 아직 도착을 하지 않아서 얼마나 걸릴지는 정확히 모르지만 한 step 동안 지났던 시간을 토대로 value function을 update합니다. 따라서 실제로 도착을 하지 않아도, final outcome을 모르더라도 학습할 수 있는 것이 TD의 장점이며 매 step마다 학습할 수 있다는 것도 장점입니다.

    > MC vs TD
      TD can learn before knowing the final outcome
        TD can learn online after every step
        MC must wait until end of episode before return is knwon

      TD can learn without the final outcome
        TD can learn from incomplete sequences
        MC can only learn from complete sequences
        TD works in continuing (non-terminating) environments
        MC only works for episodic (terminating) environments

  - Bias / Variation Trade-Off

  또 한 가지 중요한 차이점은 바로 bias와 variance입니다.
  bias : 데이터가 실제 값으로부터 전체적으로 많이 벗어나게 되면 bias가 높다 혹은 biased됬다고 표현합니다.
  variance : 실제 값과 상관없이, 전체적으로 데이터가 많이 퍼져있는 경우 variance가 높다고 합니다.

  둘 다 낮으면 좋겠지만 보통은 이 둘이 Trade-off 관계에 있어서 하나가 낮아지면 하나가 높아지는 관계에 있습니다. TD는 bias가 높고 MC는 variance가 높습니다. 둘 다 학습에 방해가 되는 요소입니다.

  TD는 한 episode안에서 계속 업데이트를 하는데 보통은 그 전의 상태가 그 후의 상태에 영향을 많이 주기 때문에 학습이 한 쪽으로 치우쳐지게 됩니다. 계속 같은 분야 사람들과 이야기를 하면 생각의 폭이 좁아지는 것과 비슷한 것을 생각하면 될 것 같습니다. 생각이 한 쪽으로 치우쳐질 수 있다는 것이지요 그렇기 때문에 여러사람들의 의견을 들어보는 것이 좋습니다.

  하지만 너무 여러사람의 의견을 듣다보면 이도 저도 아니게 되서 결정을 못하게 되곤 합니다. 이러한 실제 경험들이 사실 bias/variance trade-off와 관련이 되어 있습니다. MC가 variance가 높은 이유는 앞에서도 설명했었지만 에피소드마다 학습하기 때문에 처음에 어떻게 했느냐에 따라 전혀 다른 experience를 가질 수가 있기 때문입니다.

    > TD methods
      TD target R_(t+1) + 𝛾 * V_(t+1)(s) is biased estimate of v_𝜋(S_t)
      TD target is much lower variance than the return :
        Return depends on many random actions, transitions, rewards
        TD target depends on one random action, transition, reward

  앞으로도 Bias와 Variance는 머리속에 기억해두어야 할 필요가 있는 것이, 강화학습을 발전시키려는 노력들이 알고리즘의 근본적인 부분을 수정하는 것에도 있지만, 그 알고리즘의 bias와 variance를 낮추려는 것에 집중되는 경향이 있기 때문입니다.

  ***

# TD Control

## 1. Sansa

  TD(0)의 알고리즘은 다음과 같습니다.

    > TD(0) algorithm
      Input : the policy 𝜋 to be evaluted
      Initialize V(s) arbitrarily (e.g., V(s) = 0, ∀s ∈ S+)
      Repeat (for each episode):
        A <- action given by 𝜋 for S
        Take action A; observe reward, R, and next state, S'
        V(S) <- V(S) + alpha[R + 𝛾 * V(S') - V(S)]
        S <- S'
      until S is terminal

  하지만 model-free control이 되기 위해서는 action-value function을 사용해야 한다고 말했었습니다. 따라서 위의 TD(0)의 식에서 value function을 action-value function으로 바꾸어주면 Sarsa가 됩니다. Sarsa는 현재 state-action pair에서 다음 state와 다음 action까지를 보고 update하기 때문에 붙은 이름입니다. TD(0)를 이해했다면 크게 어려운 점이 없는 부분입니다.

    > Sarsa
      Q(S,A) <- Q(S,A) + 𝛼 * (R + 𝛾 * Q(S',A') - Q(S,A))

  Sarsa는 따라서 TD(0)을 가지고 action-value function으로 바꾸고 ϵ-greedy policy improvement를 한 것입니다.

    > On-Policy Control With Sarsa
      Every time-step:
        Policy evalutation Sarsa, Q ≈ q_𝜋
        Policy improvement ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 policy improvement

  Sarsa의 algorithm을 보면 다음과 같습니다. on-policy TD control algorithm으로써 매 time-setp마다 현재의 Q value를 imediate reward와 다음 action의 Q value를 가지고 update합니다. policy는 따로 정의되지는 않고 이 Q value를 보고 ϵ−𝑔𝑟𝑒𝑒𝑑𝑦하게 움직이는 것 자체가 policy입니다.

    > Sarsa algorithm
      Initialize Q(s,a), ∀s ∈ S, a ∈ A(s), arbitrarily, and Q(terminal-state,∙) = 0
      Repeat (for each episode):
        Initialize S
        Choose A from S using policy derived from Q (e.g., ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
          Take action A, observe R, S'
          Choose A' from S' using policy derived from Q (e.g., ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
          Q(S,A) <- Q(S,A) + 𝛼 * [R + 𝛾 * Q(S',A') - Q(S,A)]
          S <- S'; A <- A';
        until S is terminal
