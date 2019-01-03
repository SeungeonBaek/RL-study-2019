##/*이웅원님 Git*/

###Bellman Equation

Bellman Equation은 Dynamic programming의 기반이 되는 방정식 입니다.

이전 markdown에 정리해 놓았듯이, MDP에서  Value function에는 state-value function v(s)와
action-value function q(s,a) 두 가지가 있습니다.

Value function의 정의에서, value function은 다음과 같이 풀어 쓸 수 있습니다.

####v(s) = E[G_t | S_t = s]

= E[R_t+1 + 𝛾 * R_t+2 + 𝛾^2 * R_t+3 + ... | S_t = s]

= E[R_t+1 + 𝛾 * (R_t+2 + 𝛾 * R_t+3 + ...) | S_t = s]

= E[R_t+1 + 𝛾 * G_t+1 | S_t = s]

#### = E[R_t+1 + 𝛾 * v(S_t+1) | S_t = s]

이 중 가장 중요한 식은 마지막 식으로, 이 식은 현재 state와 다음 state사이의 value function을
관계짓는 식입니다.

이 식을 Bellman equation이라고 합니다.

이와 비슷하게 action-value function도 다음과 같이 표현할 수 있습니다.

####q(s,a) = E[R_t+1 + 𝛾 * q(S_t+1, A_t+1) | S_t = s, A_t = a]

이렇게 위와같이 expectation을 이용한 표현은 조금 추상적일 수 있으며,
다음과 같이 표현할 수 있습니다.

현재 state의 value function과 다음 state의 value function의 상관관계 식을
구하려면 그 사이에 있는 state-action pair에 대해서 그 관계를 나눠볼 필요가 있습니다.

그렇게 되면, v(s)라는 식은
𝑣_𝜋 (𝑠) = (모든 𝑎∈𝐴에 대해) ∑〖𝜋(𝑎│𝑠) 𝑞_𝜋 (𝑠,𝑎)〗

𝑞_𝜋 (𝑠,𝑎)=𝑅(𝑠,𝑎) + (모든 𝑠′∈𝑆에 대해) 𝛾∗∑〖𝑃(𝑠𝑠^′,𝑎)∗𝑣_𝜋 (𝑠^′)〗
