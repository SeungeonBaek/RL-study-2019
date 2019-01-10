출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Policy Gradient

## Monte-Carlo Policy Gradient : REINFORCE

  앞에서 살펴봤던 Finite difference policy gradient는 numerical한 방법이고 앞으로 살펴볼 Monte-Carlo Policy Gradient와 Actor-Critic은 analytic하게 gradient를 계산하는 방법입니다. analytic하게 gradient를 계산한다는 것은 objective function에 직접 gradient를 취해준다는 것입니다. 이때, policy는 미분 가능하다고 가정합니다.

  이 때 gradient를 계산하는 것을 episode마다 해주면 MC Policy Gradient이고 time-step마다 계산할 수 있으면 Actor-critic입니다. 밑에서 보면 score function이라는 것이 나옵니다. score function이란 무엇일까요?

***

## 1. Score function

  analytic하게 gradient를 계산하기 위해서 Objective function에 직접 gradient를 취하면 다음과 같은 식을 얻습니다. objective function으로 average reward formulation을 사용하였습니다.

  Gradient를 𝜃에 대해서 취하기 때문에 objective function의 식 중에서 policy에만 gradient를 취하면 되서 안쪽으로 들어가게 됩니다.

    J(𝜃)    = E_𝜋𝜃[r] = {s ∈ S} Σ d(s) {a ∈ A} Σ 𝜋_𝜃(s,a) * R^s_a

    ∇𝜃 J(𝜃) = {s ∈ S} Σ d(s) {a ∈ A} Σ 𝜋_𝜃(s,a) * ∇𝜃 log(𝜋_𝜃(s,a) * R^s_a)
            = E_𝜋𝜃 [∇𝜃 log(𝜋_𝜃(s,a) * r)]

  하지만 gradient가 안쪽으로 들어가면서 log가 갑자기 나오는데 그 이유는 다음과 같습니다.

    ∇𝜃 𝜋_𝜃(s,a) = 𝜋_𝜃(s,a) * ( ∇𝜃 𝜋_𝜃(s,a) / 𝜋_𝜃(s,a) )
                = 𝜋_𝜃(s,a) * ∇𝜃 log(𝜋_𝜃(s,a) * R^s_a)

  왜 이렇게 하는 걸까요? 만약에 log의 형태로 바꾸지 않았다고 생각하면 식은 다음과 같이 됩니다.

  $$\sum { s\in S }^{ }{ d(s) } \sum { a\in A }^{ }{ { { \nabla }{ \theta }\pi }{ \theta }(s,a)\quad{ R }_{ s,a }\quad } $$

  이렇게 되면 결국 𝜋_𝜃(s,a)가 사라졌기 때문에 expectation을 취할 수가 없습니다. 결국은 expectation으로 묶어서 그 안을 sampling하게 되어야 강화학습이 될텐데 따라서 expectation을 취하기 위해서 policy를 나눴다가 곱하는 것입니다. 그래서 score function은 아래와 같이 정의가 됩니다.

    > Score function
      We now compute the policy gradient analytically
      Assume policy 𝜋_𝜃 is diffrentiable whenever it is non-zero
      and we know the gradient ∇𝜃 𝜋_𝜃(s,a)
      Likelihood ratios exploit the following identity

        ∇𝜃 𝜋_𝜃(s,a) = 𝜋_𝜃(s,a) * ( ∇𝜃 𝜋_𝜃(s,a) / 𝜋_𝜃(s,a) )
                    = 𝜋_𝜃(s,a) * ∇𝜃 log(𝜋_𝜃(s,a) * R^s_a)

      The socre function is ∇𝜃 log(𝜋_𝜃(s,a) * R^s_a)

  objective function의 gradient는 다음과 같습니다.
    E_𝜋𝜃[∇𝜃 log(𝜋_𝜃(s,a) * r)]

***

## 2. Policy Gradient Theorem

  E_𝜋𝜃[∇𝜃 log(𝜋_𝜃(s,a) * r)]

  이 식의 의미는 다음과 같습니다. p(x)는 policy라고 보시면 되는데 ~는 이 policy를 표현하는 parameter space에서의 gradient입니다. 이 때 여기에 scalar인 reward r을 곱해줌으로써 어떤 방향으로 policy를 업데이트 해줘야 하는지를 결정합니다. 따라서 그 방향으로 parameter space에서의 policy가 이동하게 됩니다.

  http://karpathy.github.io/2016/05/31/rl/  참고하세용 ^^

  이때, policy가 어디로 얼만큼 update 될 것인지의 척도가 되는 scalar function으로 immediate reward만 사용하면 그 순간에 잘했냐, 잘 못했냐의 정보밖에 모르기 때문에 제대로 학습이 되지 않을 가능성이 높습니다.

  이 immediate reward대신에 자신이 한 행동에 대한 long-term reward인 action-value function을 사용하겠다는 것이 policy gradient theorem입니다. 따라서 아래의 마지막 식을 보게되면 r 대신에 Q function이 들어간 것을 확인할 수 있습니다. 한 순간 순간의 reward를 보는 것이 아니라 지금까지 강화학습이 그래왔듯이 long-term value를 보겠다는 것입니다. 이 Theorem은 Sutton교수님의 "Policy Gradient Methods for Reinforcement Learning with Function Approximation"논문에 증명이 되어 있다고 합니다.

***

## 3. Stochastic Policy

  위의 gradient를 통해서 policy의 parameter들을 업데이트 할 것입니다. 하지만 그 전의 stochastic한 policy를 어떻게 표현할 수 있을까요? 보통 딥러닝에서 output node에서 많이 사용되는 nonlinear함수인 Sigmoid함수와 Softmax함수를 많이 사용합니다.

  - Sigmoid
    Sigmoid 함수는 다음과 같이 표현된다고 합니다.

      S(x) = 1 / (1 + e^-x) = e^x / (e^x + 1)

    이 함수는 output이 0~1 사이의 값으로 나오는 함수입니다. 따라서 stochastic 즉 확률을 나타내는데에는 좋다고 합니다.

    discrete action space의 경우 agent가 왼쪽과 오른쪽으로 갈 수 있다고 하면(action = right or left) 이 함수에서 나오는 값이 "1에 가깝다면 왼쪽으로 갈 확률이 높고 0에 가깝다면 오른쪽으로 갈 확률이 높다"라는 식으로 설정하여 stochastic 한 policy를 표현할 수 있습니다.

    또는 continuous action space일 경우에는 다른 형태로 표현할 수도 있습니다. 만약 어떤 로봇의 controller에 0부터 100까지 control input을 줄 수 있다면 sigmoid함수를 통해 0이 나오면 control input은 0, 1이 output으로 나오면 control input은 100을 주는 식으로, sigmoid 함수의 output을 normalized action으로 보고 continuous action 또한 표현할 수 있습니다.

  - Softmax
    만약 discrete action space에서 action이 3개 이상이 되면 sigmoid함수로 표현하기가 애매해집니다. 이럴 때에는 Softmax함수를 쓰는 것이 좋습니다. Softmax함수는 다음과 같이 표현할 수 있습니다.

      P_t(a) = exp(q_t(a) / 𝜏) / {i = 1 -> n} Σ exp(q_t(i) / 𝜏)

    softmax function은 value를 action probability로 변환해주는 역할을 합니다.
    이때의 q_t(a)는 알다시피 q value이고 𝜏는 temperature parameter라고 하여서, high temperature일 때는 확률이 거의 같아지게, low temperature에는 action을 고를 확률이 value에 영향을 많이 받게끔 합니다.

    웅원님 설명 : action이 i=1 부터 n까지 있을 때 action probability를 위의 함수로 표현할 수 있다고 합니다. 두 가지 이상의 action에 대해서 sigmoid가 아닌 softmax함수를 쓰는 이유라고 하고, 총 합은 1입니당.

  이렇게 stochastic한 policy를 어떻게 표현하는 지, sigmoid와 softmax에 대해서 간단히 설명 했는데 사실 이론보다는 실제로 코드로 구현할 때 해보면 더 잘 이해가 될 것이라고 합니다.

***

## 4. Monte-Carlo Policy Gradient

  여기까지 policy gradient를 통해서 학습을 할 준비는 끝냈다고 합니다. objective function을 정의했고 policy를 parameter를 통해서 나타냈을 때 그 parameter를 update 하기 위해서 objective function의 gradient를 구해야 했습니다.

  objective function의 gradient는 아래와 같이 정의 된다고 합니다.
  하지만 action value function의 값을 어떻게 알 수 있을까요? 이전에 모든 state에 대해 action value function을 알기 어려워서 approximation을 했었는데 policy자체를 updat하려니 기준이 필요하고 그러다보니 action value function을 사용해야 하는데 사실 이 값을 알 방법이 애매합니다.

  하지만 알 수 있는 방법이 있는데 그게 바로 Monte-Carlo방법입니다. episode를 가보고 받았던 reward들을 기억해 놓고 episode가 끝난 다음에 각 state에 대한 return을 계산하면 됩니다.

  return자체가 action-value function의 unbiased estimation입니다. 이러한 알고리즘은 REINFORCE라고 하며 아래와 같습니다.

    > Monte-Carlo Policy Gradient (REINFORCE)
      - Update parametres by stochastic gradient ascent
      - Using policy gradient theorem
      - Using return v_t as an unbiased sample of Q^(𝜋_𝜃)(s_t, a_t)
        ∆𝜃_t = 𝛼 * ∇𝜃 log( 𝜋_𝜃(s_t,a_t) * v_t)

    > function REINFORCE
      Initialise 𝜃 arbitrarily
      for each episode {s_1, a_1, r_2, ..., s_(T-1), a_(T-1), r_T}





































ㅁㄴㅇㄹ
