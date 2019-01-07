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
