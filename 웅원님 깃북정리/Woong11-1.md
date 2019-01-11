출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Policy Gradient

## 1. Policy Gradient

  현재 강화학습에서 가장 "hot"하다고 볼 수 있는 방법이 바로 Policy Gradient입니다.

  AlphaGo의 알고리즘도 "Policy Gradient with Monte-Carlo Tree Search"라고 합니다. 또한 실제 로봇이나 헬리콥터, 드론 같은 도메인에 적용하기 적합한 방법이라고 합니다.

  이웅원님의 경우 강화학습에 관심을 가지게 된 계기가 드론의 자율주행이었기 때문에 Policy Gradient는 상당히 흥미롭게 다가왔다고 합니다.

***

## 2. Value-based RL vs Policy-based RL

  지금까지 저희가 다루어왔던 방법들은 모두 "Value-based" 강화학습입니다. 즉, Q라는 action-value function에 초점을 맞추어서 Q function을 구하고 그것을 토대로 policy를 구하는 방식입니다.

  이전에 DQN 또한 Value-based RL으로써 DNN을 이용하여 Q-function을 approximate하고 policy는 그것을 통해 만들어졌을 뿐이었습니다.

    > Value-based reinforcement learning vs Policy-based reinforcement learning

      In the last lecture we approximated the state-value or action-value function using parameters 𝜃,
        V_𝜃(s)   ≈ V_𝜋(s)
        Q_𝜃(s,a) ≈ Q_𝜋(s,a)

      A policy was generated directly from the value function
        e.g. using ϵ−𝑔𝑟𝑒𝑒𝑑𝑦

  그와 달리 Policy-based RL은 Policy 자체를 approximate해서 function approximator에서 나오는 것이 value function이 아니고 policy자체가 나옵니다.

  Policy자체를 parameterize하는 것입니다. 어떻게 보면 evolutionary 알고리즘의 개념에 더 가깝다고 할 수도 있습니다. 하지만 지금까지 저희가 살펴보았듯이 evolutionary 알고리즘과 달리 강화학습은 환경과의 상호작용이 있습니다.

    > Value-based reinforcement learning vs Policy-based reinforcement learning
        In this lecture we will directly parametrise the policy
          𝜋_𝜃(s,a) = P[a|s, 𝜃]

        We will focus again on model-free reinforcement learning

  Policy Graidient는 다음과 같은 장점과 단점을 가지고 있습니다.

  - 기존의 방법에 비해서 수렴이 더 잘되며 가능한 action이 여러개이거나(high-dimension) action자체가 연속적인 경우에 효과적입니다. 즉, 실제의 로봇 control에 적합합니다.
  - 또한 기존의 방법은 반드시 하나의 optimal한 action으로 수렴하는데 policy gradient에서는 stochastic한 policy를 배울 수 있습니다. (예를 들면 가위바위보)

  하지만 local optimum에 빠질 수 있으며 policy의 evaluate하는 과정이 비효율적이고 variance가 높습니다.

    > Policy-based reinforcement learning

      Advantage
      - Better convergence properties
      - Effective in high-dimensional or continuous action spaces
      - Can learn stochastic policies

      Disadvantage
      - Typically converge to a local rather than global optimum
      - Evaluating a policy is typically inefficient and high variance

  기존 방법의 문제를 살펴보도록 하겠습니다. Value-based RL 방식에는 두 가지 문제가 있습니다.

### Unstable
  Value-based RL에서는 Value function을 바탕으로 policy를 계산하므로 Value function이 조금만 달라지더라도, Policy자체는 좌회전에서 우회전을 하는 등의 크게 변화할 수 있는 risk를 안고 있습니다. 이러한 risk가 전체적인 알고리즘의 수렴에 불안정성을 더해줍니다.
  하지만 Policy자체가 함수화 되어버릴 경우, 학습을 하면서 조금씩 변하는 value function으로 인해서 policy또한 조금씩 변하게 되어서 안정적이고 부드럽게 수렴하게 됩니다.

### Stochastic Policy
  때로는 Stochastic Policy가 Optimal policy일 수 있습니다. 가위바위보 게임은 동등하게 가위와 바위와 보를 (1/3)씩 내는 것이 Optimal 한 Policy입니다. value-based RL에서는 Q function을 토대로 하나의 action만 선택하는 optimal policy를 학습하기 때문에 이러한 문제에는 적용시킬수가 없습니다.

***

## 3. Policy Objective Function

  이제 기존의 방법처럼 action-value function을 approximate하지 않고 policy를 바로 approximate할 것입니다. 학습은 policy를 approximate한 parameter들을 update해 나가는 것입니다. 이 parameter들을 update하려면 기준이 필요한데 DQN에서는 TD error를 사용했었습니다.
  하지만 Policy Gradient에서는 Objective function이라는 것을 정의합니다. 정의하는 방법에는 세 가지가 있습니다. state value, average value, average reward per time-step입니다.

  똑같은 state에서 시작하는 게임에서는 처음 시작 state의 value function이 강화학습이 최대로 하고자 하는 목표가 됩니다. 두 번째는 잘 사용하지 않고, 세 번째는 각 time-step마다 받는 reward들의 expectation값을 사용합니다.

  사실은 time-step마다 받는 reward들의 expectation값을 사용합니다. 사실은 time-step마다 받은 reward들을 discount시키지 않고 stationary distribution을 사용해서 어떤 행동이 좋았냐에 대한 credit assignment 문제를 풀고 있지 않나 생각됩니다.

    > Policy Objective functions

      Goal : given policy 𝜋_𝜃(s,a) which parameters 𝜃, find best 𝜃
      But how do we measure the quality of a policy 𝜋_𝜃?
      In episode environments we can use the start value
        J_1(𝜃) = V^(𝜋_𝜃)(s_1) = E_𝜋𝜃[v_1]

      In continuing environments we can use the average value
        J_avV(𝜃) = {𝜋} Σ d^(𝜋_𝜃)(s) * V^(𝜋_𝜃)(s)

      Or the average reward per time-step
        J_avR(𝜃) = {𝜋} Σ (d^(𝜋_𝜃)(s)) {a} Σ ()(s,a)*R^s_a)

      where d^(𝜋_𝜃)(s) is stationary distribution of Markov chain for 𝜋_𝜃

  Stationary distribution은 처음 접하는 개념일 수 있습니다. Sutton교수님의 policy gradient 논문에서는 stationary distribution을 다음과 같이 정의하고 있습니다.
  https://webdocs.cs.ualberta.ca/~sutton/papers/SMSM-NIPS99.pdf 읽어보시게...

  웅원님의 이해로는 각 state에 머무르는 비율로 이해했다고 합니다. 이러한 stationary distribution이 어떻게 구현되었나 궁금하다고 합니다.

  Policy Gradient에서의 목표는 이 Objective function을 최대화 시키는 policy의 parameter vector를 찾아내는 것이라고 합니다.

  그렇다면 어떻게 찾아낼까요? 바로 Gradient descent입니다. 그래서 Policy gradient라고 불리는 것입니다. 다음에서는 Objective function의 graident를 어떻게 구하는 지에 대해서 보겠습니다.

    > Find 𝜃 that maximises J(𝜃)
      J_1(𝜃)   = V^𝜋𝜃(s_1) = E_𝜋𝜃[v_1]
      J_avR(𝜃) = {𝜋} Σ (d^(𝜋_𝜃)(s)) {a} Σ ()(s,a)*R^s_a)

***

## 4. How to get gradient of objective function

  Objective function의 gradient를 구하는 방법이 핵심인데 세 가지 방법이 있습니다.

  - Finite Difference Policy Gradient
  - Monte-Carlo Policy Gradient
  - Actor-Critic Policy Gradient

  하나씩 차근 차근 살펴보도록 하겠습니다.

***

# Finite Difference Policy Gradient

## 1. Finite Difference Policy Gradient

  이 방법은 수치적인 방법으로서 가장 간단하게 objective function의 gradient를 구할 수 있는 방법입니다. 만약 parameter vector가 5개의 dimension으로 이루어져 있다고 한다면 각 parameter를 ϵ만큼 변화시켜보고 5개의 parameter에 대한 gradient를 각각 구하는 것입니다.

  parameter space가 작을 때는 간단하지만 늘어날수록 비효율적이고 noisy한 방법이라고 합니다. policy가 미분 가능하지 않더라도 사용 가능하다는 장점이 있어서 초기 policy gradient에서 사용되던 방법입니다.

    > Finitie Difference PG (Numerical Method)
      To evaluate policy gradient of 𝜋_𝜃(s,a)
      For each dimension k ∈ [1,n]
        Estimate kth partial derivative of objective function w.r.t. 𝜃
        By perturbing 𝜃 by small amount ϵ in kth dimension
          𝜕J(𝜃) / 𝜕𝜃_k ≈ {J(𝜃 + ϵ * u_k) - J(𝜃)} / ϵ

          where u_k is unit vector with 1 in kth component, 0 elsewhere
      Uses n evaluations to compute policy gradient in n dimensions
      Simple, noisy, inefficient - but sometimes effective
      Works for arbitrary policies, even if policy is not differentiable

***

## 2. Example : Training AIBO

  강화학습으로 로봇을 학습시키는 논문중의 Finite Difference Policy Gradient를 사용해서 sony의 AIBO를 학습시킨 2004년 논문이 있습니다. Silver교수님 수업에서도 아래 그림과 같이 소개되었습니다.

    > Training AIBO to Walk by Finite Difference Policy Gradient
      Goal : learn a fast AIBO walk (useful for Robocup)
      AIBO walk policy is controlled by 12 numbers (elliptical loci)
      Adapt these parameters by finite difference policy gradient
      Evaluate performance of policy by field traversal time

  http://www.sony-aibo.com/ 참고
  AIBO는 기본 적인 걸음걸이가 느리기 때문에 더 빠르게 걸음걸이(gait)을 튜닝하는데 강화학습을 사용한다고 합니다.

  다리의 궤적 자체를 parameterize했기 때문에 Policy gradient 방법이라고 할 수 있습니다. 다리의 궤적 자체를 policy로 보는 것입니다.

  따라서 가장 빠른 걸음걸이를 얻기 위해 12개의 component로 구성되어 있는 parameter vector를 학습시키는 것이 목표입니다.

  여기서 objective function은 속도가 됩니다. (따라서 사실 앞에서 언급했던 objective function에 대한 식들은 여기서는 사용하지 않습니다. => 가속도를 사용한다는 건가염?)

  ### Gradient를 구하는 방법
  (1) Parameter vector 𝜋 (directly represent the policy of AIBO)
  (2) To estimate gradient numerically generate t randomly generated policies

  즉, 12개의 parameter를 기존의 parameter보다 미세한 양을 랜덤하게 변화시킨 t개의 policy를 생성하는 것입니다. 그러면 변화가 된 t개의 policy의 objective function(속도)을 측정합니다. 12개의 parameter들 각각에 대해 average score를 계산해서 update를 하면 됩니다.

  자세한 건 논문을 참고하면 될 것 같고, 로봇의 걸음걸이 자체를 함수화 할 수 없어서 미분 불가능한 문제를 numerical하게 하나하나 해보면서 풀었던 예시라고 합니다.
  최근에 와서는 잘 사용하지 않는 방법이라고 합니다.
