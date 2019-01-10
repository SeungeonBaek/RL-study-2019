출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Policy Gradient

## Monte-Carlo Policy Gradient : REINFORCE

  앞에서 살펴봤던 Finite difference policy gradient는 numerical한 방법이고 앞으로 살펴볼 Monte-Carlo Policy Gradient와 Actor-Critic은 analytic하게 gradient를 계산하는 방법입니다. analytic하게 gradient를 계산한다는 것은 objective function에 직접 gradient를 취해준다는 것입니다. 이때, policy는 미분 가능하다고 가정합니다.

  이 때 gradient를 계산하는 것을 episode마다 해주면 MC Policy Gradient이고 time-step마다 계산할 수 있으면 Actor-critic입니다. 밑에서 보면 score function이라는 것이 나옵니다. score function이란 무엇일까요?

## 1. Score function

  analytic하게 gradient를 계산하기 위해서 Objective function에 직접 gradient를 취하면 다음과 같은 식을 얻습니다. objective function으로 average reward formulation을 사용하였습니다.

  Gradient를 𝜃에 대해서 취하기 때문에 objective function의 식 중에서 policy에만 gradient를 취하면 되서 안쪽으로 들어가게 됩니다.

    J(𝜃) = E_𝜋𝜃[r] = {s ∈ S} Σ d(s) {a ∈ A} Σ 𝜋_(s,a) * R^s_a

    
