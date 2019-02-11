출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Value function Approximation

## 1. Tabular Methods

  지금까지 살펴본 강화학습은 action value funciton을 Table로 만들어서 푸는 Tabular Methods입니다. 이에 대해서 Sutton교수님은 다음과 같이 말합니다. 즉, 현재의 방법은 state나 action이 많지 않을 경우에만 적용 가능하다는 것입니다. 이 Table이 점점 더 커지면 이 값들을 다 기억할 메모리도 문제지만 학습에 너무 많은 시간이 소요되기 때문에 사실상 학습이 불가능합니다. 앞에서 다뤘던 예제들도 다 gridworld같이 작은 예제였다는 것을 알 수 있습니다.

    > We have so far assumed that our esimates of value functions are represented as a table with one entry for each
    state of for each state,action pair.
    This is particularly clear and instructive case, but of course it is limited to tasks with small numbers of
    states and actions.
    The problem is not just the memory needed for large tables, but the time and data needed to fill them accurately.
    In other words, the key issue is that of generalization!

  그러나 현실은 gridworld같이 작은 예제가 있지 않기 때문에 현재의 방식은 실용적이지 못합니다. 예를들면, 밑의 문제들을 강화학습은 풀지 못합니다. 그렇기 때문에 "Generalization"이 가능해지기 위해서는 새로운 idea가 필요합니다.

  특히나 강화학습을 실제 세상에 적용시키고 싶다고 할 경우, 실제 세상은 continuous state space이므로 사실상 state가 무한대이기 때문에 새로운 방법이 없다면 로봇이 강화학습으로 학습하기는 쉽지 않을 것입니다.

    > Large-Scale Reinforcement Learning
      Reinforcement learning can be used to solve large problems, e.g.
        Backgammon  : 10^20  states
        Computer GO : 10^170 states
        Helicopter  : continuous state space

      How can we scale up the model-free method for prediction and control from the last two lectures?

***

## 2. Parameterizing value function

  이에 대한 해답은 아래와 같습니다. table로 작성하는 것이 아니고 w라는 새로운 변수를 사용해서 value function을 함수화하는 것입니다.

  쉽게 말해 함수의 input으로 state가 들어가면, action value function이 output으로 나오고, 이때 함수의 parameter가 w인 것입니다.

  이제는 학습을 통해서 Q function을 update하는 것이 아니고, w라는 parameter를 업데이트 하게 됩니다. 이러한 functdion approximation 방법에는 여러가지가 있습니다.

    > We consider differentiable function approximators, e.g.
      Linear combinations of features
      Neural network
      Decision tree
      Nearst neighbour
      Fourier / wavelet bases

  이 중에서 저희는 위의 두 가지를 볼텐데 (1) Linear combinations of features (2) Neural network를 볼 것입니다. (2)는 특히 최근에 딥러닝의 발전으로 각광받는 방법입니다. 최근의 강화학습은 다 딥러닝을 approximator로 사용하기 때문에 보통 Deep Reinforcement Learning (DRL)이라고 부릅니다.

***

# Stochastic Gradient Descent

## 1. Gradient Descent

  이전까지 다루었던 Tabular Reinforcement learning의 단점 때문에 function approximator를 도입하게 되었고 value function을 w라는 parameter를 통해서 approximate하였습니다. 또한 이제 학습이라는 것은 이 parameter를 update하는 것이라고 했었습니다.

  그렇다면 parameter를 update하는 것은 어떻게 할 수 있을까요? 이전에 machine learning에 대해서 접해본 분이면 잘 아는 Stochastic Gradient Descent방법을 활용하여 value function의 parameter를 update하게 됩니다.

  이 방법은 간단하면서도 간단하기 때문에 프로그램 상으로 강력한 update방법입니다. 하지만 시작점이 조금만 달라져도 도착하는 local optimum이 바뀌는 특징이 있습니다. 또한, 도착한 극점이 global optimum이 아닐수도 있습니다.

  이러한 단점을 극복하는 방법은 여러가지가 있지만 처음 parameter를 update하는 것을 배우는 입장에서는 간단한 개념을 알고 나중에 활용할 때 그러한 기법들을 도입하면 될 것 같습니다.

  J(w)로 표현되는 objective 함수는 내가 원하는 대상과 자신의 error로 보통 설정하여 그 error를 최소화하는 것을 목표로 합니다. update를 하려면 어느방향으로 가야 그 error가 줄어드는지 알아야 하는데 그것을 함수의 미분(gradient)을 취해서 알 수 있습니다. gradient자체는 경사이기 때문에 곡면에서 보자면 위로 올라가는 방향이므로 -를 곱해서 그 반대 방향으로 내려감으로서(descent) 조금씩 error를 줄여나가는 것입니다.

    > Gradient Descent
      Let J(w) be a differentiable function of parameter vector w
      Define the gardient of J(w) to be
        ∇w J(w) = (𝜕J(w)/𝜕w1, 𝜕J(w)/𝜕w2, ... , 𝜕J(w)/𝜕wn)'

      To find a local minumum of J(w)
      Adjust w in direction of -ve gradient
        ∆w = -(1/2) * 𝛼 * ∇w J(w)

***

## 2. Gradient Descent on RL

  Gradient의 개념을 살펴보았습니다. 이 개념을 강화학습에 적용시켜보도록 하겠습니다. 강화학습에서는 J(w)를 어떻게 정의할까요? 바로 true value function과 approximate value vhat(s,w)와의 error로 잡습니다.

    > Value Function Approximation by Stochastic Gradient Descent
      Goal : find parameter vector w minimising mean-squared error between approximate value function vhat(s,w)
      and true value function v_𝜋(s)
        J(w) = E_𝜋[{v_𝜋(s)-vhat(s,w)}^2]

      Gradient descent finds a local minimum
        ∆w = -(1/2) * 𝛼 * ∇w J(w)
           = 𝛼 * E_𝜋[{v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)]

      Stochastic gardient descent samples the gradient
        ∆w = 𝛼 * {v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)

      Expedted update is equal to full gradient update

  Gradient Descent방법도 (1) Stochastic Gradient Descent(SGD)와 (2) Batch 방법으로 나눌 수 있는데 위와 같이 모든 state에서 true value function과의 error를 한 번에 함수로 잡아서 업데이트 하는 방식은 Batch의 방식을 활용한 것으로서 step by step으로 업데이트 하는 것이 아니고 한 번에 업데이트 하는 것입니다.

  Mean-Squared error를 gradient방식에 집어넣어서 gradient를 취해보면 다음과 같습니다.

    > Gradient descent finds a local minimum
        ∆w = -(1/2) * 𝛼 * ∇w J(w)
           = 𝛼 * E_𝜋[{v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)]

  하지만 DP에서 강화학습으로 넘어갈 때 처럼 expectation을 없애고 sampling으로 대체하면 아래와 같아집니다.

    > Stochastic gradient descent samples the gradient
      ∆w = 𝛼 * {v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)

  이전에 MC와 TD Learning에서 했듯이 True value function 부분을 여러가지로 대체할 수 있습니다. Sample return을 사용할 수도 있고 TD target을 사용할 수도 있습니다.

    > Have assumed true value function v_𝜋(s) given by superviser
      But in RL there is no supervisor, only rewards
      In practice, we substitute a target for v_𝜋(s)
        For Mc, the target is the return G_t
          ∆w = 𝛼 * {G_t-vhat(s,w)} * ∇w vhat(s,w)

        For TD(0), the target is the TD target R_(t+1) + 𝛾 * vhat(s,w)
          ∆w = 𝛼 * {R_(t+1) + 𝛾 * vhat(s,w) - vhat(s,w)} * ∇w vhat(s,w)
        For TD(𝜆), the target is the TD target R_(t+1) + 𝛾 * vhat(s,w)
          ∆w = 𝛼 * {G^𝜆_t - vhat(s,w)} * ∇w vhat(s,w)

***

# Learning with Function Approximator

## 1. Action-value function approximation

  앞에서는 state-value function을 사용했지만 model-free가 되기 위해서는 action-value function을 사용해야 합니다. 그러한 알고리즘을 그림으로 표현하자면 아래와 같습니다.

  policy evaluation은 parameter의 update로 진행하며 policy improvement는 그렇게 update된 action value function에 ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 한 action을 취함으로써 improve가 됩니다.

    > Control with Value Function Approximation
      Policy evalutation : Approximate policy evaluation, qhat(∙,∙,w) ≈ q_𝜋
      Policy improvement : ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 policy improvement

  앞에서 value function으로 했던 내용을 반복하면 아래와 같습니다.

    > Action-Value Function Approximation
      Approximate the action-value function
        qhat(S,A,w) ≈ q_𝜋(S,A)

      Minimise mean-squared error between approximate action-value function qhat(S,A,w)
      and true action-value function q_𝜋(S,A)
        J(w) = E_𝜋[{q_𝜋(S,A) - qhat(S,A,w)}^2]

      Use stochastic gradient descent to find a local minimum
        -(1/2) * ∇w J(w) =     {q_𝜋(S,A) - qhat(S,A,w)} * ∇w qhat(S,A,w)
        ∆w               = 𝛼 * {q_𝜋(S,A) - qhat(S,A,w)} * ∇w qhat(S,A,w)

      True value function을 대체하는 것도 아래와 같습니다.

      Like prediction, we muist substitute a target for q_𝜋(S,A)
        For MC, the target is the return G_t
          ∆w = 𝛼 * {G_t - qhat(S_t, A_t, w)} * ∇w qhat(S_t, A_t, w)

        For TD(0), the target is the TD target R(t+1) + 𝛾 * Q(S_(t+1), A_(t+1))
          ∆w = 𝛼 * {R_(t+1) + 𝛾 * qhat(S_(t+1), A_(t+1), w) - qhat(S_t, A_t, w)} * ∇w qhat(S_t, A_t, w)

        For forward-view TD(𝜆), target is the action-value 𝜆-return
          ∆w = 𝛼 * {q^𝜆_t - qhat(S_t, A_t, w)} * ∇w qhat(S_t, A_t, w)

        For backward-view TD(𝜆), equivalent update is
          𝛿_t = R_(t+1) + 𝛾 * qhat(S_(t+1), A_(t+1), w) - qhat(S_t, A_t, w)
          E_t = 𝛾 * 𝜆 * E_(t-1) + ∇w qhat(S_t, A_t, w)
          ∆w  = 𝛼 * 𝛿_t * E_t

***

## 2. Batch Methods

  지금까지 SGD(Stochastic Gradient Descent)를 통해서 parameter를 update하는 방법을 사용했었습니다. 하지만 이 방법은 아래와 같은 문제가 있습니다.

    > Batch Reinforcement Learning
      Gradient descent is simple and appealing
      But it is not sample efficient
      Batch methods seek to find the best fitting value function
      Given the agents's experience ("training data")

  SGD처럼 gradient를 따라서 parameter를 update하는 것이 아니고 training data(agent가 경험한 것)들을 모아서 한꺼번에 update하는 것이 "Batch Methods"입니다. 하지만 Batch방법은 한 번에 업데이트 하는 만큼 그 많은 데이터들에 가장 잘 맞는 value function을 찾기가 어렵기 때문에 SGD와 Batch방법의 중간을 사용하는 경우도 많습니다.

  예를 들면, step-by-step으로 업데이트 하는 것이 아니고 100개의 데이터가 모일 떄까지 기다렸다가 100번에 한 번씩 업데이트하는 "mini-batch"방법도 있습니다.

  위에서 말하는 SGD의 문제점인 experience data를 한 번만 사용하는 것이 비 효율적이다라고 말하는 점에 대해서는 한 번만 사용하지 않고 여러번 사용하는 것으로 문제를 해결할 수 있습니다. 하지만 어떤 방법으로 experience data를 여러번 활용할 것인가에 대해서 experience replay가 그 답을 말해줍니다.

***

## 3. Experience Replay

  Experience Replay는 아래와 같습니다. 뒤에서 설명하겠지만 Deepmind에서 Atrai Game에 사용했던 알고리즘이고 아래와 같습니다. replay memory라는 것을 만들어 놓고서 agent가 경험했던 것들을 (S_t, A_t, R_(t+1), S_(t+1))로 time-step마다 끊어서 저장해 놓습니다.

  그 후, action-value funtion의 parameter를 update하는 것은 time-step마다 하지만 하나의 transition에 대해서만 하는것이 아니라 모아놓았던 transition을 replay memory에서 100개 혹은 200개씩 꺼내서(mini-batch) 그 mini-batch에 대해 update를 진행합니다.

    > Experience Replay in Deep Q-Networks (DQN)
      DQN uses experience replay and fixed Q-targets
      - Take action a_t according to ϵ−𝑔𝑟𝑒𝑒𝑑𝑦 policy
      - Store transition (s_t, a_t, r_(t+1), s_(t+1)) in replay memory D
      - Sample random mini-batch of transitions (s,a,r,s') from D
      - Compute Q-learning targets w.r.t. old, fixed parameter w-
      - Optimise MSE between Q-network and Q-learning targets
          L_i(w_i) = E_(s,a,r,s'~ D_i) [(r + 𝛾 * {a'}max( Q(s', a'; w-_i) - Q(s, a; w_i) ))^2]

      - Using variant of stochastic gradient descent

  이렇게 할 경우에 sample efficient할 수도 있지만 또한 episode내에서 step-by-step으로 update를 하면 그 데이터들 사이의 correlation 때문에 학습이 잘 안되는 문제도 해결할 수 있습니다.
