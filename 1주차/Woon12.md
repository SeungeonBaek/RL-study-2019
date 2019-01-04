/*이웅원님 Git*/

1. Markov Decision Process

Environment의 response인 R_t+1과 S_t+1이

Pr{R_t+1 = r, S_t+1 = s' | S_t, A_t}

이와 같이 이전 time t에만 영향을 받는 process
(time 0 ~ time (t-1)에는 영향을 받지 않음.)

Markov decision process (MDP)는 다음과 같이 tuple <S, A, P, R, gammar >로 이루어져 있습니다.

S : 이 중 State는 agent가 인식하는 자신의 상태

A : Action은 agent가 특정 state에서 지시하는 행동이며
agent는 action을 취함으로써 자신의 state를 변화시킬 수 있습니다. agent는 controller
와 같다고 보면 될 것 같습니다.

P : transition probability matrix는 특정 state s에서 특정 action a를 취할때 s'에
도착할 확률입니다.

R : agent가 action을 취하면 그에 따른 reward를 환경이 agent에게 알려줍니다.
강화학습에서는 정답이나 환경에 대한 사전지식 없이도 이 reward를 통해서 agent가
학습을 하게 됩니다.

gamma : expected return을 계산함에 있어 현재의 reward와 미래의 reward의 가치를
정하는 factor이며, 0에서 1사이의 값을 통해 근시안 적인지, 미래 지향적인지를 정한다.

Policy : 뜻 그대로 풀이하면 정책이며, 어떤 state에서 어떤 action을 할지를 policy라고
합니다.

2. Value Function

  - Sate-Value Function

Return Gt : Gt는 total discounted reward from time-step t 입니다.

'Gt = R_t+1 + gamma * R_t+2 + ...'

Return에 대한 식은 위와 같고 이 return의 예측값(expectation)이
state-value function 입니다.

Value function v(s)는 상태 s의 long-term value이며 다음과 같이 정의됩니다.

v(s) = E[G_t | S_t = s]

즉, 어떤 상태 s의 가치입니다. value function을 구하는 방법의 하나의 예를 들어보면,
마치 주사위를 던져 보듯이 계속 그 state로부터 시작되거나, 그 state를 지나가는 episode를
try해보면서 얻어진 reward들에 대한 data들로 그 value function에 점점 다가갈 수 있습니다.

대부분 강화학습의 알고리즘에서는 value function을 얼마나 잘 계산하느냐가 중요한 역할을
하고 있습니다.
"잘"이라는 의미에는 bias되지 않고, variance가 낮으며, true값에 가까우며 빠른 시간안에
수렴하는 것을 의미합니다.


  - Action-Value Function

action이란, 어떤 state에서 할 수 있는 행동들을 말하는데 보통 모든 state에서 가능한
행동은 모두 같습니다.

state value function에 대해서 생각을 해보면 사실 그 state의 value라는 것은 그 state에서
어떤 action을 했는지에 따라 달라지는 reward들에 대한 정보를 포함하고 있습니다.

또한 agent 입장에서 다음 행동을 다음 행동이 될 수 있는 state들의
value function으로 판단하는데 그러기 위해서는, 다음 state들에 대한 정보를 모두 알아야 하고,
그 state로 가려면 어떻게 해야 하는지도 알아야합니다.

따라서 state-value function말고 action에 대한 value function을 구할 수 있는데 그것이 바로
action-value funcdtion입니다.

action value function을 사용하면 state value function과는 달리 단지 어떤 행동을 할지
action value function의 값을 보고 판단하면 되기 때문에 다음 state들의 value function을 알고
어떤 행동을 했을 때 거기에 가게 될 확률도 알아야 하는 일이 사라집니다.

action - value function의 정의는 다음과 같습니다.

'q(s,a) = E[G_t | S_t = s, A_t = a]'

이는 어떤 state s 에서 action a를 취할 경우의 받을 return에 대한 기대값으로써 어떤
행동을 했을 때 얼마나 좋을 것인가에 대한 값입니다.
위에서 언급했던 이유로 앞으로 Value function이 아닌 action-value function을 사용할 것입니다.
Action-value function은 다른 말로 Q-value 로써, q-learning이나 deep q - network에서 사용되는
q라는 것이 이것을 의미합니다.
