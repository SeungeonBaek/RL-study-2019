/*이웅원님 Git*/

# Monte-Carlo Methods

  - 5~7장은 Dyanmic programming, Monte Carlo methods, Temporal-difference methods에 대해서 다루고 있습니다.

## 1. Model-free

  이전 Chapter에서 Dynamic programming에 대해서 배워보았습니다.
  Dynamic programming은 Bellman equation을 통해서 optimal한 해를 찾아내는 방법으로서, MDP에 대한 모든 정보를 가진 상태에서 문제를 풀어나가는 방법을 이야기합니다.

  특히 Environment의 model인 "Reward function"과 "State transition probability"를 알아야하기 때문에 Model-based한 방법이라고 할 수 있습니다.

  이러한 방법에는 아래과 같은 문제점이 존재합니다.

  (1) Full-width Backup => Expensive computation
  (2) Full knowledge about environment


  이러한 방식으로는 바둑같은 경우의 수가 많은 문제를 풀 수가 없고 실제 새상에 적용시킬 수가 없습니다.
  사실 위와 같이 학문적으로 접근하지 않더라도 이러한 방법이 사람이 배우는 방법과는 많이 다르다는 것을 알 수 있습니다.

  이전에도 언급했었지만 사람은 모든 것을 다 안 후에 움직이지 않습니다. 만져보면서, 밟아보면서 조금씩 배워나갑니다.

  이전에도 말했듯이 Trial and error를 통해서 학습하는 것이 강화학습의 큰 특징입니다. 따라서 DP처럼 full-width backup을 하는 것이 아니라, 실제로 경험한 정보들로서 update하는 sample backup을 하게 됩니다.

  이렇게 실제로 경험한 정보들을 사용함으로써 처음부터 environment에 대해서 모든 것을 알 필요가 없습니다. environment의 model을 모르고 학습하기 때문에 __Model-free__ 라는 말이 붙게 됩니다.

    > In subsequent lectures we will consider sample backups
      Using sample rewards and sample transitions <S, A, R, S'>
      Instead of reward function R and transition dynamics P
      Advantages :
        Model-free : no advance knowledge of MDP required
        Breaks the curse of dimensionality through sampling
        Cost of backup is constant, independent of n = |S|


  현재의 policy를 바탕으로 움직여 보면서, sampling을 통해 value function을 update하는 것을 "model-free prediction"이라고 하고, policy를 update까지 하게 된다면 "model-free control"이라고 합니다.

  이렇게 Sampling을 통해서 학습하는 model-free 방법에는 다음의 두 가지 방법이 있습니다.

  (1) Monte-Carlo
  (2) Temporal difference

  Monte-Carlo는 episode마다 update하는 방법이고 Temporal Difference는 time step마다 update하는 방법입니다. 이번 Chapter에서는 Monte-Carlo Learning을 살펴보도록 하겠습니다.

## 2. Monte-Carlo

  Monte-Carlo라는 말에 대해 Sutton교수는 다음과 같이 말합니다.

    > Monte-Carlo
      The term "Monte-Carlo" is often used more broadly for any estimation method whose operation


***
