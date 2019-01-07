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

***

## 2. Monte-Carlo

  Monte-Carlo라는 말에 대해 Sutton교수는 다음과 같이 말합니다.

    > Monte-Carlo
      The term "Monte-Carlo" is often used more broadly for any estimation method whose operation

  Monte-Carlo 단어 자체는 무엇인가를 random하게 측정하는 것을 뜻하는 말이라고 합니다. 강화학습에서는 "averaging complete returns"하는 방법을 의미한다고 합니다. 이것은 무엇을 의미하는지 알아보겠습니다.

  Monte-Carlo와 Temporal Difference로 갈리는 것은 value function을 estimation하는 방법에 따라서 입니다. value function이라는 것은 expected accumulative futre reward로서 지금 이 state에서 시작해서 미래까지 받을 기대되는 reward의 총합입니다. 이것을 DP가 아니라면 어떻게 측정할 수 있을까요?

  가장 기본적인 생각은 episode를 끝까지 가본 후에 받은 reward들로 각 state의 value function들을 거꾸로 계산해보는 것입니다. 따라서 MC(Monte-Carlo)는 끝나지 않는 episode에서는 사용할 수 없는 방법입니다. initial state S1에서부터 시작해서 terminal state St까지 현재 policy를 따라서 움직이게 된다면 한 time step마다 reward를 받게 될 텐데, 그 reward들을 기억해 두었다가 St가 되면 뒤돌아보면서 각 state의 value fucntion을 계산하게 됩니다. 아래 recall that the return이라고 되어있는데 제가 말한 것과 같은 말입니다. 순간 순간 받았던 reward들을 시간 순서대로 discount시켜서 sample return을 구할 수 있습니다.

    > Monte-Carlo
      Goal: learn v_𝜋 from episodes of experience under policy 𝜋
        S_1, A_1, R_2, ... , S_k ~ 𝜋
      Recall that the return is the total discounted reward:
        G_t = R_(t+1) + 𝛾 * R_(t+2) + ... + 𝛾^(T-1) * R_(T)
      Recall that the value function is the expected return:
        v_𝜋(s) = E_𝜋[G_t | S_t = s]
      Monte-Carlo policy evaluation uses empirical mean return instead of expected return

***

## 3. First-Visit MC vs Every-Visit MC

  위에서는 한 에피소드가 끝나면 어떻게 하는 지에 대해서 말했습니다. 하지만 multiple episodes를 진행할 경우에는 한 episode마다 얻었던 return을 어떻게 계산해야할까요? MC에서는 단순히 평균을 취해줍니다. 한 episode에서 어떤 state에 대해 return을 계산해놨는데 다른 episode에서도 그 state를 지나가서 다시 새로운 return을 얻었을 경우에 그 두개의 return을 평균을 취해주는 것이고 그 return들이 쌓이면 쌓일수록 true value function에 가까워지게 됩니다.

  한 가지 고민해야할 점이 있습니다. 만약에 한 episode내에서 어떠한 state를 두 번 방문하다면 어떻게 해야할가요? 이 때 어떻게 하냐에 따라서 두 가지로 나뉘게 됩니다.

  - First-visit Monte-Carlo Policy evaluation
  - Every-visit Monte-Carlo Policy evaluation

  말 그대로 First-visit은 처음 방문한 state만 인정하는 것이고(두 번째 그 state 방문에 대해서는 return을 계산하지 않는) every-visit은 방문할 때마다 따로 따로 return을 계산하는 방법입니다. 두 방법은 모두 무한대로 갔을 때 true value function으로 수렴합니다. 하지만 First-visit이 좀 더 널리 오랫동안 연구되어 왔으므로 여기서는 First-visit MC에 대해서 다루도록 하겠습니다. 아래는 First-Visit Monet-Carlo Policy Evalutation에 대한 Silver교수님 수업의 자료입니다.

  > First-visit Monte-Carlo Policy evaluation
    To evaluate state s
    The first time-step t that state s is visit in an episode,
    Increment counter N(s) <- N(s) + 1
    Increment total return S(s) <- S(s) + G_t
    Value is estimated by mean return V(s) = S(s)/N(s)
    By law of large numbers, V(s) -> v_𝜋(s) as N(s) -> ∞

***

## 4. Incermental Mean

  위의 평균을 취하는 식을 좀 더 발전시켜보면 다음과 같습니다. 저희가 학습하는 방법은 여러개를 모아놓고 한 번에 평균을 취하는 것이 아니고, 하나 하나 더해가며 평균을 계산해얗 ㅏ기 때문에 아래와 같은 incremental meatn의 식으로 표현할 수 있습니다.
    The mean 𝜇_1, 𝜇_2, ... of a sequence x_1, x_2 ... can be computed incremntally,

      > 𝜇_k = (1/k) * {j = 1 -> k } Σ x_j
            = (1/k) * (x_k + {j = 1 -> k-1 } Σ x_j )
            = (1/k) * (x_k + (k-1) * 𝜇_(k-1))
            = (1/k) * (x_k + k * 𝜇_(k-1) - 𝜇_(k-1))
            = 𝜇_(k-1) + (1/k) * (x_k - 𝜇_(k-1))

  이 Incremental Mean을 위의 First-visit MC에 적용시키면 아래와 같습니다. 같은 식을 다르게 표현한 것입니다. 이 때, 분수로 가있는 N(S_t)가 점점 무한대로 가게되는데, 이를 알파로 고정시켜놓으면 효과적으로 평균을 취할 수 있게 됩니다. 맨 처음 정보들에 대해 가중치를 덜 주는 형태라고 보시면 될 것 같습니다. (Complementary filter에 대해서 알면 이해가 쉬운 부분입니다.) 이와 같이 하는 이유는 강화학습이 stationary problem이 아니기 대문입니다. 매 epixode마다 새로운 policy를 사용하기 때문에 non-stationary problem이므로 update하는 상수를 일정하게 고정하는 것입니다.



***
