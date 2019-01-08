출처 : https://dnddnjs.gitbooks.io/rl/content/value_function_approximation.html
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

***

# Eligibility Traces

## 1. n-step TD

  TD learning은 Monte-Carlo learning에 비해서 매 time-step마다 학습을 할 수 있다는 장점이 있었습니다. 다시 한 번 TD Control인 Sarsa를 봐보겠습니다. 아래의 update식을 보면 결국 update 한 번 할 때 R 하나의 정보밖에 알 수 없어서 학습하는데 오래 걸리기도 하고 bias가 높기 때문에 사실은 TD와 MC 이 둘의 장점을 다 살릴 수 있다면 좋습니다.

  따라서 update를 할 때 one step만 보고 update를 하는 것이 아니고 n-step을 움직인 다음에 update를 하자라고 생각하게 됩니다. 만약 지금이 t라고 하면 t+n이 되면 그 때까지 모았던 reward들로써 n-step return을 계산하고 그 사이의 방문했던 state들의 value function을 update하는 것입니다. 그것이 바로 n-step TD입니다. 몇 개의 time-step마다 update를 할 것인지는 자신이 결정하면 됩니다.

  이 n-step이 terminal state까지 간다면 그게 바로 Monte-Carlo method가 됩니다. 따라서 둘의 장점을 다 취하기 위해서 그 사이의 적당한 n-step을 선택해주는 것이 좋습니다.

    > n-Step Return
      Consider the following n-step returens for n = 1, 2, ..., ∞;
        n = 1 (TD) G^1_t = R_(t+1) + 𝛾 ∗ V(S_(t+1))
        n = 2      G^2_t = R_(t+1) + 𝛾 ∗ R_(t+2) + 𝛾^2 ∗ V(S_(t+2))
          .
          .
          .
        n = ∞ (MC) G^∞_t = R_(t+1) + 𝛾 ∗ R_(t+2) + 𝛾^2 ∗ R_(t+3) + ... + 𝛾^(T-1)) ∗ R_T

      Define the n-step return
        G^n_t = R_(t+1) + 𝛾 ∗ R_(t+2) + ... + 𝛾^(n-1) ∗ R_(t+n) + 𝛾^(n) ∗ V(S_(t+n))

      n-step temporal-difference learning
        V(S_t) <- V(S_t) + 𝛼 * (G^n_t - V(S_t))

  하지만 어떤 n이 적당한 n이라는 것을 알 수있는지와 그 기준이 무엇인지에 대한 문제가 남습니다.

***

## 2. Forward-View of TD(𝜆)

  예제 설명은 스킵하겠습니다.

  어떠한 문제에 n-step TD prediction을 적용시켜볼 경우에 n으로 적당한 숫자가 얼마인지 판별하기 쉽지 않습니다.
  사실 𝛼의 값에 따라서 어떤 n-step이 학습에 좋은지는 달라지기 때문에 사실은 여러 n-step을 합할 수만 있다면 각 n-step에서의 장점을 다 취할 수 있을 것입니다.

  따라서 이 모든 n-step return을 모두 더해서 사용하는 방법이 있습니다. 하지만 단순히 더해서 평균을 구하는 방식이 아니라, 아래와 같이 𝜆라는 weight을 사용해서 geometrically weighted sum을 이용하게 되면 모든 n-step을 다 포함하면서도 weight들의 합이 1이 됩니다. 이것을 통해서 구한 𝜆-return을 원래 MC의 return 자리에 넣어주게 되면, forward-view TD(𝜆)가 됩니다.

      > 𝜆-return
        The 𝜆-return G^𝜆_t combines all n-step returns G^𝜆_t
        Using weight (1-𝜆) * 𝜆^(n-1)

          G^𝜆_t = (1-𝜆) {n = 1 -> ∞} Σ 𝜆^(n-1) * G^n_t

        Forward-view TD(𝜆)

          V(S_t) <- V(S_t) + 𝛼 * (G^𝜆_t - V(S_t))

  다시 정리를 해보자면 TD는 time-step마다 학습할 수 있는 장점은 있었지만 또한 bias가 높고 학습정보가 별로 없기 때문에 TD와 MC의 장점을 둘 다 살리기 위한 방법으로 n-step TD가 있었습니다. 하지만 각 n-step이 상황마다 다른 장점이 있어서 이 모든 장점을 포함하기 위해서 𝜆라는 wiehgt을 도입해서 𝜆-return을 계산해서 사용하는 것이 forward-view TD(𝜆)입니다.

  하지만 이 방법에도 단점이 있습니다. 바로 MC와 똑같이 episode가 끝나야 update를 할 수 있다는 것입니다. (모든 n-step을 포함하기 때문)

      > Forward-view TD(𝜆)
        Update value function towards the 𝜆-return
        Forward-view looks into the future to compute G^𝜆_t
        Like MC, can only be computed from complete episodes

***

## 3. Backward-View of TD(𝜆)

  따라서 본래 TD의 장점이었던 time-step마다 update할 수 있다는 장점이 사라졌습니다. MC의 장점은 살리면서도 바로 바로 update할 수 있는 방법이 없을까요? 여기서 바로 eligibility trace라는 개념이 나옵니다. 아래 그림과 같이 과거에 있었던 일들 중에서 현재 내가 받은 reward에 기여한 것이 무엇일까? 라는 credit assignment문제에서 "얼마나 최근에 일어났던 일이었나?"와 "얼마나 자주 발생했었나?"라는 것을 기준으로 과거의 일들을 기억해놓고 현재 받은 reward를 과거의 state들로 분배해주게 됩니다.

      > Eligibility Traces

        그림 : 벨 벨 벨 전구 쇼크 가 그려져있음.

        Credit assignment problem : did bell or light cause shock?
        Frequency heuristic : assign credit to most frequent states
        Recency heuristic   : assign credit to most recent states
        Eligibility traces combine both heuristics

          E_0(s) = 0
          E_t(s) = 𝛾 * 𝜆 * E_(t-1)(s) + I(S_t = s)

  즉, TD(0)처럼 현재 update할 𝛿를 계산하면 현재의 value function만 update하는 것이 아니라 과거에 지나왔던 모든 state에 eligibility trace를 기억해두었다가 그 만큼 자신을 update하게 됩니다.

  따라서 아래 그림과 같이 현재의 경험을 통해 한 번에 과거의 모든 state들의 value function을 update하게 되는 것입니다. 현재의 경험이 과거의 value function에 얼마나 영향을 주고 싶은가는 𝜆를 통해서 조절할 수 있습니다.

  이러한 update방식을 backward-view TD(𝜆)라고 합니다.

      > Backward-view TD(𝜆)
        Keep an eligibility trace for every state s
        Update value V(s) for every state s
        In proportion to TD-error 𝛿_t and eligibility trace E_t(s)
          𝛿_t = R_(t+1) + 𝛾 * V(S_(t+1)) - V(S_t)
          V(s) <- V(s) + 𝛼 * 𝛿_t * E_t(s)

***

## 4. Sarsa(𝜆)

  위에서는 TD prediction만 다루었습니다. 여기서는 TD Control에 대해서 다루도록 하겠습니다. Sarsa에도 n-step Sarsa가 있고 forward-view Sarsa(𝜆)가 있고, backward-view Sarsa(𝜆)가 있습니다. 각각은 다음과 같습니다. 설명은 생략하겠습니다.

    > n-step Sarsa
    Consider the following n-step returens for n = 1, 2, ..., ∞;
      n = 1 (Sarsa) q^1_t = R_(t+1) + 𝛾 ∗ q(S_(t+1))
      n = 2         q^2_t = R_(t+1) + 𝛾 ∗ R_(t+2) + 𝛾^2 ∗ q(S_(t+2))
        .
        .
        .
      n = ∞ (MC)    q^∞_t = R_(t+1) + 𝛾 ∗ R_(t+2) + 𝛾^2 ∗ R_(t+3) + ... + 𝛾^(T-1)) ∗ R_T

    Define the n-step Q-return
      q^n_t = R_(t+1) + 𝛾 ∗ R_(t+2) + ... + 𝛾^(n-1) ∗ R_(t+n) + 𝛾^n ∗ Q(S_(t+n))

    n-step Sarsa updates Q(s,a) towards the n-step Q-return
      Q(S_t,A_t) <- Q(S_t,A_t) + 𝛼 * (q^n_t - Q(S_t,A_t))

***

## 5. Forward View Sarsa(𝜆)

  The q^𝜆 return combines all n-step Q-returns q^𝜆_t
  Using weight (1-𝜆) * 𝜆^(n-1)
    q^𝜆_t = (1-𝜆) {n = 1 -> ∞} Σ (𝜆^(n-1) * q^n_t)

  Forward-view Sarsa(𝜆)
    Q(S_t,A_t) <- Q(S_t,A_t) + 𝛼 * (q^𝜆_t - Q(S_t,A_t))

***

## 5. Backward View Sarsa(𝜆)

  Just like TD(𝜆), we use eligibility traces in an online algorithm
  But Sarsa(𝜆) has one eligibility trace for each stata-action pair
    E_0(s,a) = 0
    E_t(s,a) = 𝛾 * E_(t-1)(s,a) + I(S_t = s, A_t = a)

  Q(s,a) is updated for every state s and action a
  In proportion to TD-error 𝛿_t and eligibility trace E_t(s,a)
    𝛿_t = R_(t+1) + 𝛾 * Q(S_(t+1),A_(t+1)) - Q(S_t,A_t)
    Q(s,a) <- Q(s,a) + 𝛼 * 𝛿_t * E_t(s,a)

  backward-view Sarsa(𝜆) algorithm의 qseudo code는 다음과 같습니다.

      > Backward-veiw Sarsa(𝜆) algorithm
        Initialize Q(s,a) arbitrarily, for all {s ∈ S ,𝑎 ∈ 𝐴}
        Repeat (for each episode) :
          E(s,a) = 0, for all {s ∈ S ,𝑎 ∈ 𝐴}
          Initilaze S, A
          Repeat(for each step of episode) :
            Take action A, observe R, S'
            Choose A' from S' using policy derived from Q (e.g. ϵ−𝑔𝑟𝑒𝑒𝑑𝑦)
            𝛿 <- R + 𝛾 * Q(S',A') - Q(S,A)
            E(S,A) <- E(S,A) + 1
            For all {s ∈ S ,𝑎 ∈ 𝐴}:
              Q(s,a) <- Q(s,a) +  * 𝛿_t * E_t(s,a)
              E(s,a) <- 𝛾 * 𝜆 * E(s,a)
            S <- S'; A <- A'
        until S is terminal
