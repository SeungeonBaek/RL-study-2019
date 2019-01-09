출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/ DQN

# Neural Network

## 1. What is DQN

  강화학습에서 agent는 environment를 MDP를 통해서 이해를 하는데 table형태로 학습을 모든 state에 대한 action-value function의 값을 저장하고 update 시켜나가는 식으로 하면 학습이 상당히 느려집니다. 따라서 approximation을 하게 되고, 그 approximation방 중에서 nonlinear function approximator로 deep neural network가 있습니다. 따라서 action-value function(q-value)를 approximate하는 방법으로 ㅇeep neural network를 택한 reinforcement learning방법이 Deep Rienforcement Learning(deepRL)입니다. 또한 action value function뿐만 아니라 policy 자체를 approximate할 수도 있는데 그 approximator로 DNN을 사용해도 DeepRL이 됩니다.

  action value function을 approximate하는 deep neural networks를 Deep Q-Networks(DQN)이라고 하는데 그렇다면 DQN으로 어떻게 핛브할까요? DQN이라는 개념은 DeepMind의 "Playing Atari with Deep Reinforcement Learning"이라는 논문에 소개되어 있습니다.
  https://www.cs.toronto.edu/~vmnih/docs/dqn.pdf

***

## 2. Artificial Neural Networks (ANN)

  http://sanghyukchun.github.io/74/
  http://arxiv.org/pdf/cs/0308031.pdf
  http://www.slideshare.net/imanog/artificial-neural-network-48027460
  http://stackoverflow.com/questions/2480650/role-of-bias-in-neural-networks
  이웅원 님은 다음의 reference를 통해서 깃북을 작성했다고 합니다.

  DeepRL을 이해하기 위해서는 딥러닝의 기본적인 개념에 대해서 알 필요가 있습니다. 강화학습이 사람의 행동방식을 모방했다라고 한다면, artificial neural networks는 사람의 뇌의 구조를 모방했습니다.

  인공지능이 사람의 뇌를 모방하게 된 것에는 컴퓨터가 계산과 같은 일에는 사람보다 뛰어난 performance를 내지만 개와 고양이를 구별하는 사람이라면 누구나 간단하게 하는 일은 컴퓨터는 하지 못했기 때문입니다.

  따라서 이미 뇌의 구조에 대해서는 수많으 뉴런들과 시냅스로 구성되어 있다는 것을 알고 그것을 수학적 모델로 만들어서 컴퓨터의 알고리즘에 적용시키는 방법을 택한 것입니다.

  neural networks의 수학적 모델은 실제 뉴런의 구조 및 화학적 원리를 기반으로 만들어 졌습니다. 각 Neuron들은 synapse를 통해서 signal을 받습니다. 만약 signal이 어떤 특정한 threshold를 넘어간다면 neruon이 activate되고 그 뉴런은 axon을 통해서 signal을 다른 synapse로 보냅니다.

  또한 보통 뉴런은 여러개의 input이 들어와서 여러개의 output이 나가는 구조이며, 그 input과 output은 뉴런사이의 연결을 통해서 전달이 됩니다.

  예를 들어 뉴런의 시냅스가 10개라고 가정하게 되면 이 시냅스를 통해서 10개의 다른 input들이 들어오게 됩니다. 또한 neuron의 process에 들어가는 값은 이 10개의 input들의 linear combination입니다. 이 process를 거친 y값은 다시 다른 뉴런들의 synapse의 input으로 들어가게 됩니다. 이러한 사람의 뉴런의 구조를 모방해서 인공신경망을 구성하게 되면, 각 neuron은 node가 되고 synapse를 통해서 들어오는 signal은 input이 되고 각각 다른 synapse를 통해서 들어오는 signal들의 중요도가 다를 수 있으므로 weight를 곱해줘서 들어오게 됩니다.

  이 signal들이 wiehgt와 곱해진 것이 바로 net input signal(알짜 입력 신호)입니다. 그 net input signal을 식으로 표현하게 되면 다음과 같습니다.

    > Net input signal received through synaptic junctions is
      net = b + Σ w_i * x_i = b + W^T * x

      Wieght vector : W = [w_1, w_2, ... , w_m]'

      Input vector  : X = [x_1, x_2, ... , x_m]'

      Each output is a function of the net stimulus signal(f is called the activation function)

        y = f(net) = f(b + W^T * x)

  시냅스로 들어오는 각각의 input을 vector로 표현하고 그 input에 각각 곱해지는 weight 또한 그에 따라 vector로 만들어서 두 vector를 곱해서 input과 weight의 linear combination을 만들어 줍니다. 여기서 새로운 개념이 나타나는데, b로 써지는 bias입니다.

  Bias가 linear combination에 더해져서 net input signal로 들어가는 이유는 간단하게 말하자면 다음과 같습니다. 좌표평면에서 (0,0)과 (5,5)를 어떠한 선을 기준으로 구분하고 싶다고 가정해 봅시다.

  bias가 없는 y = ax같은 함수의 경우에는 두 점을 구분할 수 있는 방법이 전혀 없습니다. (0,0)이 직선 위에 있기 때문이죠. 하지만, y = ax + b의 함수는 이 두점을 구분할 수 있습니다.

  또한 다른 식으로 bias의 필요성을 설명한 stackoverflow의 댓글이 있습니다.

    > Role of bias in neural networks
      Modification of neuron WEIGHTS alone only serves to manipulate the shape/curvature of your transfer function, and not its equilibrium/zero crossing points.
      The introduction of BIAS neurons allows you to shift the transfer function curve horizontally (left/right) along the input axis while leaving the shape/curvature unaltered.
      This will allow the network to produce arbitrary outputs differnet from the defaults and hence you can customize/shift the input to output mapping to suit your particular needs.

  즉, 노드로 들어가는 input들에 곱해지는 weight(학습시키려는 대상)을 변화시키면 함수의 모양만 변화시킬 수 있지, 왼쪽/오른쪽으로 이동시켜서 0이 되는 point를 변형 시킬수는 없다는 것입니다.

  따라서 bias를 사용하면 요구에 따라 그래프를 이동 및 변형시켜서 학습할 수가 있다는 것입니다.

  Input signal들과 weight이 곱해지고 bias가 더해진 net input signal이 node를 activate시키는데 그 형식을 function으로 정의할 수 있습니다. 그러한 함수를 activation function이라 합니다.

  위 위의 식에서 f로 표현한 activation function의 가장 간단한 형태는 들어온 input들의 합이 어떤 threshold보다 높으면 1이 나오고 낮으면 0이 나오는 형태일 것입니다. 하지만 이런 형태의 activation function의 경우에는 미분이 불가능 하다는 단점이 있습니다. 그럴 경우 gradient descent를 통한 최적화를 진행하지 못 하기 때문에, 그 이외의 미분가능한 함수를 사용합니다.

  그 중에서 가장 간단한 activation function은 sigmoid function입니다. sigmoid function이란 무엇일까요? f(x) = 1 / (1 + e^-ax)로 표현되며, [0 1]사이의 값을 가지는 함수입니다.

  activation function의 예시에는 sigmoid 말고도 세 가지 다른 함수들이 있는데 이 함수들은 모두 non-linear합니다. 그 이유는 activation function이 linear할 경우에는 아무리 많은 neuron layer를 쌓는다 하더라도 그것이 결국 하나의 layer로 표현이 되기 때문입니다.

  - sigmoid function
  - tanh function
  - absolute function
  - ReLU function

  가장 실용적인 activation function은 ReLU function이라고들 합니다. ReLU란 어떤 함수일까요?

  ReLU 함수는 x가 0보다 작거나 같을때는 y가 0이 나오고, x가 0보다 클 경우에는 y = x의 형태를 띄는 함수입니다.

  사실 딥러닝이 최근에 갑자기 급 부상한 이유에는 엄청나게 혁신적인 변화가 있었다기 보다는 Computation time의 감소와 더불어 activation function을 sigmoid에서 ReLU로 바꾸는 등의 작은 변화들이 중첩되며 일어났기 때문입니다.

  sigmoid 함수에 비해 ReLU가 가지고 있는 장점은 어떤 것이 있는지 알아보겠습니다. ReLU의 직선적이 형태와 sigmoid함수 처럼 수렴하는 형태가 아닌 점이 ReLU의 stochastic gradient descent가 더 잘 수렴하게 해줍니다. 또한 상대적으로 sigmoid함수에 비해서 계산량이 줄어든다는 장점도 있습니다.

  장점이 있으면 단점도 있는 법입니다. 단점은 다음과 같습니다. Learning rate에 따라서 중간에 최대 40%의 network가 "die"할 수 있다고 합니다. 단, learning rate를 잘 조절하면 이 문제는 그렇게 크지 않다고 합니다.

***

## 3. Stochastic Gradient Descent(SGD) and Back-Propagation

### (1) SGD

  지금까지는 deep neural network가 무엇인지에 대해서 살펴보았습니다. 다시 이글의 청므으로 돌아가서 DQN이란 action-value function을 deep neural network로 approximation 한 것을 말합니다. 강화학습의 목표는 optimal policy를 구하는 것이고 각 state에서 optimal한 action value fucntion을 알고 있으면 q 값이 큰 action을 취하면 되는 것이므로 결국은 q-value를 구하면 강화학습 문제를 풀게 됩니다.

  이 q-value는 DNN(deep neural networks)를 통해서 나오게 되는데 결국 DNN을 학습시키는 것이 목표가 되게 됩니다.

  따라서 approximation하지 않았을 때와 다른 것은 q-table을 만들어서 각각의 q-value를 update하는 것이 아니고 DNN안의 weight와 bias를 update하게 됩니다. 그렇다면 어떻게 update할까요?

  이 때 이전에 배웠떤 Stochastic Gradient Descent가 사용됩니다. 정리하자면 graidnet descent라는 것은 w를 parameter로 가지는 J라는 objective funciton을 minimize 하는 방법중의 하나로써 w에 대한 J의 gradient 반대 방향으로 w를 update하는 방식을 말합니다.

    > Gradient descent
        ∆w = -(1/2) * 𝛼 * ∇w J(w)
           = 𝛼 * E_𝜋[{v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)]

      Stochastic Gradient descent samples the gradient
        ∆w = 𝛼 * {v_𝜋(s)-vhat(s,w)} * ∇w vhat(s,w)

  이런 식으로 update를 하게 되는데 모든 데이터에 대해서 gardient를 구해서 한 번 updat하는 것이 아니고 Sampling을 통해서 순차적으로 update를 하겠다는 gradient descent 방법이 stochastic gradient descent입니다.

  아래 페이지를 참고해보면 그렇게 할 경우 수렴하는 속도가 훨씬 빠르며 online으로도 학습할 수 있다는 장점이 있습니다. 또한 하나 중요한 점은 gradient descent방법이 local optimum으로 갈 수 있다는 단점이 있는 최적화 방법이라는 것을 기억 해야 합니다.

### (1) Back-Propagation


















asdf
