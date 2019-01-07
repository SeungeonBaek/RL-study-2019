/*이웅원님 Git*/

# Temporal Difference Learning

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

# TD Prediction

## 1. Tmeporal Difference

  이전 Chapter에서 배웠던 Monte-Carlo Control은 Model-Free Control입니다. Model-Free라는 점에 강화학습이지만 단점이 있습니다. 바로 online으로 바로바로 학습할 수가 없고 꼭 끝나는 episode여야 한다는 단점이 있습니다.
  끝나지 않더라도 eipsode가 길 경우에는(예를 들어 atari 게임이 아니라 starcraft같은 에김) 학습하기 어려운 단점이 있습니다. 따라서 자연스럽게도 꼭 episode가 끝나지 않더라도 DP철머 time step마다 학습할 수 있지 않나?라는 생각을 하게 됩니다. 이게 바로 Temporal Difference이며 Sutton교수님 책에서는 아래와 같이 소개하고 있습니다.

    > Temporal Difference method
      If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning. TD learning is a combination of Monte-Carlo ideas and dynamic programming (DP) ideas. Like Monte-Carlo methods. TD methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based in part 
