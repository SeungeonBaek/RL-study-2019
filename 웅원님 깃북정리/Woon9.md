출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Value function Approximation

## 1. Tabular Methods

  지금까지 살펴본 강화학습은 action value funciton을 Table로 만들어서 푸는 Tabular Methods입니다. 이에 대해서 Sutton교수님은 다음과 같이 말합니다. 즉, 현재의 방법은 state나 action이 많지 않을 경우에만 적용 가능하다는 것입니다. 이 Table이 점점 더 커지면 이 값들을 다 기억할 메모리도 문제지만 학습에 너무 많은 시간이 소요되기 때문에 사실상 학습이 불가능합니다. 앞에서 다뤘던 예제들도 다 gridworld같이 작은 예제였다는 것을 알 수 있습니다.

    > We haver so far assumed that our esimates of value functions are represented as a table with one entry for each
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

  이러한 단점을 극복하는 방법은 여러가지가 있지만 처음 parameter를 update하는 것을 배우는 입장에서는 간단한 개념을 알고 나중에 활욜할 때 그러한 기법들을 도입하면 될 것 같습니다.

  J(w)로 표현되는 objective 함수는 내가 원하는 대상과 자신의 error로 보통 설정하여 그 error를 최소화하는 것을 목표로 합니다. update를 하려면 어느방향으로 가야 그 error가 줄어드는지 알아야 하는데 그것을 함수의 미분(gradient)을 취해서 알 수 있습니다. gradient자체는 경사이기 때문에 곡면에서 보자면 위로 올라가는 방향이므로 -를 곱해서 그 반대 방향으로 내려감으로서(descent) 조금씩 error를 줄여나가는 것입니다.

    > Gradient Descent
      Let J(w) be a differentiable function of parameter vector w
      Define the gardient of J(w) to be
        ∇w J(w) = (𝜕J(w)/𝜕w1, 𝜕J(w)/𝜕w2, ... , 𝜕J(w)/𝜕wn)'

      To find a local minumum of J(w)
      Adjust w in direction of -ve gradient
        ∆w = -(1/2) *


















  ㅁㄴㅇㄹ
