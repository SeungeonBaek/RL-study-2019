##/*이웅원님 Git*/

###Markov Decision Process

Environment의 response인 R_t+1과 S_t+1이

Pr{R_t+1 = r, S_t+1 = s' | S_t, A_t}

이와 같이 이전 time t에만 영향을 받는 process
(time 0 ~ time (t-1)에는 영향을 받지 않음.)

Markov decision process (MDP)는 다음과 같이
tuple <S, A, P, R, gammar >로 이루어져 있습니다.

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
