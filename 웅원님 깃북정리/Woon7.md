/*이웅원님 Git*/

# Temporal Difference Learning

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

# TD Prediction

## 1. Tmeporal Difference

  이전 Chapter에서 배웠던 Monte-Carlo Control은 Model-Free Control입니다. Model-Free라는 점에 강화학습이지만 단점이 있습니다. 바로 online으로 바로바로 학습할 수가 없고 꼭 끝나는 episode여야 한다는 단점이 있습니다.
  끝나지 않더라도 eipsode가 길 경우에는(예를 들어 atari 게임이 아니라 starcraft같은 에김) 학습하기 어려운 단점이 있습니다. 따라서 자연스럽게도 꼭 episode가 끝나지 않더라도 DP철머 time step마다 학습할 수 있지 않나?라는 생각을 하게 됩니다. 이게 바로 Temporal Difference이며 Sutton교수님 책에서는 아래와 같이 소개하고 있습니다.

    > Temporal Difference method
      If one had to identify one idea as central and novel to reinforcement learning, it would undoubtedly be temporal-difference (TD) learning.
      TD learning is a combination of Monte-Carlo ideas and dynamic programming (DP) ideas. Like Monte-Carlo methods.
      TD methods can learn directly from raw experience without a model of the environment's dynamics. Like DP, TD methods update estimates based in part 

  Temporal difference(TD)는 MC와 DP를 섞은 것으로써 MC처럼 raw experience로부터 학습할 수 있지만 DP처럼 time step마다 학습할 수 있는 방법입니다. 마지막에 "bootstrap"이라고 하는데 이 말은 무엇을 뜻할까요?

  대학생활을 예로 들어보겠습니다. MC는 대학교에 들어와서 졸업을 한 다음에 그 동안을 돌아보며 "이건 더 했어야 했고 술은 덜 마셔야했다"라고 생각하며 다시 대학교를 들어가서 대학생활을 하면서 졸업할 때까지 똑같이 살다가 다시 졸업하고 자신을 돌아보는 반면에 TD같은 경우는 같은 대학교를 다니고 있는 2학년 선배가 1학년을 이끌어주는 것과 같습니다.

  사실은 둘 다 졸업을 해보지 않은 상태에서 (잘 모르는 상황에서)이끌어 주는 것이지만 대학교를 다니면서 바로 바로 자신을 고쳐나가기 때문에 어쩌면 더 옳은 방법일지도 모
