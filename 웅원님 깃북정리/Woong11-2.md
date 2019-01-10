출처 : https://dnddnjs.gitbooks.io/rl/content
/*이웅원님 Git*/

# Policy Gradient

## 1. Monte-Carlo Policy Gradient : REINFORCE

  앞에서 살펴봤던 Finite difference policy gradient는 numerical한 방법이고 앞으로 살펴볼 Monte-Carlo Policy Gradient와 Actor-Critic은 analytic하게 gradient를 계산하는 방법입니다. analytic하게 gradient를 계산한다는 것은 objective function에 직접 gradient를 취해준다는 것입니다. 이때, policy는 미분 가능하다고 가정합니다.

  이 때 gradient를 계산하는 것을 episode마다 해주면 MC Policy Gradient이고 time-step마다 계산할 수 있으면 Actor-critic입니다. 밑에서 보면 score function이라는 것이 나옵니다. score function이란 무엇일까요?
